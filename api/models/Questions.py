from api.extensions import db

class Questions(db.Model):

    __tablename__ = "questions"
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    type_question = db.Column(db.String(30), nullable=False)
    form_id = db.Column(db.Integer, db.ForeignKey("forms.id"), nullable=False)

    form = db.relationship("Form", back_populates="questions")
    options = db.relationship("Options", back_populates="question")

    def __repr__(self):
        return f"<Question {self.text}>"