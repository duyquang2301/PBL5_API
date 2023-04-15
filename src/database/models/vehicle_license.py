from database.db import db

class VehicleLicenseModel(db.Model):
    __tablename__ = 'vehicle_license'

    id = db.Column(db.Integer, primary_key=True)
    supply_date = db.Column(db.Date,nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id") , unique=False, nullable=False)
    vehicle_id = db.Column(db.String(12), db.ForeignKey('vehicles.id'), nullable=False)
    vehicle = db.relationship('VehicleModel', back_populates='vehicle_license', uselist=False)

    user = db.relationship("UserModel", back_populates="vehicle_licenses")
