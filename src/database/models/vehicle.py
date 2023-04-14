from database.db import db

class VehicleModel(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") , unique=False, nullable=False)

    user = db.relationship("UserModel", back_populates="vehicles")
    error_papers = db.relationship("ErrorPaperModel", back_populates="vehicle", lazy="dynamic",cascade="all, delete")  