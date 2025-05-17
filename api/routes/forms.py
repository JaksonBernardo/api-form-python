from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from api.models.Form import Form
from api.models.Questions import Questions
from api.models.Options import Options
from api.models.User import User
from api.extensions import db, jwt
from flask_jwt_extended import jwt_required, get_jwt_identity

form_bp = Blueprint("form_bp", __name__, url_prefix = "/form")

@form_bp.route("/my-forms", methods = ["GET"])
@jwt_required()
def my_forms():

    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    company = user.company
    forms = company.forms
    forms_list = []

    for form in forms:

        forms_list.append({
            "id": form.id,
            "title": form.title,
            "type": form.type
        })
    
    return jsonify({"forms": forms_list}), 200

@form_bp.route("/create-form", methods = ["POST"])
@jwt_required()
def create_form():

    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    company = user.company
    data = request.get_json()

    title = data.get("title")
    questions = data.get("questions")
    type_questions = data.get("type-questions")
    options = data.get("options")
    type_form = data.get("type-form")

    if not title or not type_form:

        return jsonify({"msg": "Título do formulário são obrigatórios"}), 400

    form = Form(title=title, type=type_form, company=company)
    for i in range(len(questions)):

        question = questions[i]
        type_question = type_questions[i]

        if type_question == "SELE_UNICA" or type_question == "SELE_MULTIPLA":
            options_list = options[i]
            question_obj = Questions(text=question, type_question=type_question, form=form)
            db.session.add(question_obj)
            db.session.commit()

            for opt in options_list:
                option_obj = Options(text=opt, id_question=question_obj.id)
                db.session.add(option_obj)
                db.session.commit()
        else:
            question_obj = Questions(text=question, type_question=type_question, form=form)
            db.session.add(question_obj)
            db.session.commit()
        
    db.session.add(form)
    db.session.commit()

    return jsonify({"msg": "Formulário criado com sucesso"}), 201

@form_bp.route("/my-form/<int:form_id>", methods = ["GET"])
@jwt_required()
def get_form(form_id):

    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    company = user.company
    form = Form.query.filter_by(id=form_id, company=company).first()

    if not form:

        return jsonify({"msg": "Formulário não encontrado"}), 404

    return jsonify({
        "id": form.id,
        "title": form.title,
        "id_questions": [form.questions[i].id for i in range(len(form.questions))],
        "questions": [form.questions[i].text for i in range(len(form.questions))],
        "type_questions": [form.questions[i].type_question for i in range(len(form.questions))],
        "options": [
            [form.questions[i].options[j].text for j in range(len(form.questions[i].options))]
            for i in range(len(form.questions))
        ],
    }), 200


@form_bp.route("/delete-form/<int:form_id>", methods = ["DELETE"])
@jwt_required()
def delete_form(form_id):

    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    company = user.company
    form = Form.query.filter_by(id=form_id, company=company).first()

    questions = form.questions

    for i in range(len(questions)):

        options = questions[i].options
        for opt in options:
            db.session.delete(opt)
            db.session.commit()

        db.session.delete(questions[i])
        db.session.commit()

    db.session.delete(form)
    db.session.commit()

    return jsonify({"msg": "Formulário deletado com sucesso"}), 200


@form_bp.route("/update-form/<int:form_id>", methods = ["PUT"])
@jwt_required()
def update_form(form_id):

    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    company = user.company
    form = Form.query.filter_by(id=form_id, company=company).first()

    if not form:

        return jsonify({"msg": "Formulário não encontrado"}), 404

    data = request.get_json()

    title = data.get("title")
    type_form = data.get("type-form")
    questions = data.get("questions")
    type_questions = data.get("type-questions")
    options_list = data.get("options")

    if not title or not type_form:

        return jsonify({"msg": "Título do formulário são obrigatórios"}), 400
    
    questions_list = form.questions

    for i in range(len(questions_list)):

        options = questions_list[i].options
        for opt in options:
            db.session.delete(opt)
            db.session.commit()

        db.session.delete(questions_list[i])
        db.session.commit()

    for i in range(len(questions)):

        question = questions[i]
        type_question = type_questions[i]

        if type_question == "SELE_UNICA" or type_question == "SELE_MULTIPLA":
            options_question = options_list[i]
            question_obj = Questions(text=question, type_question=type_question, form=form)
            db.session.add(question_obj)
            db.session.commit()

            for opt in options_question:
                option_obj = Options(text=opt, id_question=question_obj.id)
                db.session.add(option_obj)
                db.session.commit()
        else:
            question_obj = Questions(text=question, type_question=type_question, form=form)
            db.session.add(question_obj)
            db.session.commit()

    form.title = title
    form.type = type_form

    db.session.commit()

    return jsonify({"msg": "Formulário atualizado com sucesso"}), 200
