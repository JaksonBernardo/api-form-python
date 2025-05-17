from api.extensions import db

class Equipament(db.Model):

    __tablename__ = "equipaments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companys.id"), nullable=False)

    company = db.relationship("Company", back_populates="equipaments")

    def __repr__(self):
        return f"<Equipament {self.name}>"