from api.extensions import db

class Company(db.Model):

    __tablename__ = "companys"

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=True)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    forms = db.relationship("Form", back_populates="company")
    users = db.relationship("User", back_populates="company")

    def __repr__(self):
        return f"<Company {self.company_name}>"
