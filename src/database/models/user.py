from database.db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(88), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    vehicle_licenses = db.relationship("VehicleLicenseModel", back_populates="user", lazy="dynamic",cascade="all, delete")  
    
    