from api.extensions import db

class Options(db.Model):

    __tablename__ = "options"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    id_question = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)

    question = db.relationship("Questions", back_populates="options")

    def __repr__(self):
        return f"<Option {self.text}>"