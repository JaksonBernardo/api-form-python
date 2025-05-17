from api.extensions import db

class Clients(db.Model):

    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key = True)
    company_name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    phone = db.Column(db.String(20), nullable = True)
    cnpj = db.Column(db.String(14), unique = True, nullable = False)
    status = db.Column(db.Integer, nullable = False)
    address = db.Column(db.String(255), nullable = True)
    city = db.Column(db.String(100), nullable = True)
    state = db.Column(db.String(20), nullable = True)
    cep = db.Column(db.String(9), nullable = True)
    company_id = db.Column(db.Integer, db.ForeignKey("companys.id"), nullable = False)

    company = db.relationship("Company", back_populates = "clients")

    def __repr__(self):
        return f"<Clients {self.company_name}>"