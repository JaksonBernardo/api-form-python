from api.extensions import db

class Form(db.Model):

    __tablename__ = "forms"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    id_company = db.Column(db.Integer, db.ForeignKey("companys.id"), nullable=False)

    company = db.relationship("Company", back_populates="forms")

    def __repr__(self):
        return f"<Form {self.title}>"