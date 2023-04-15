from database.db import db

class VehicleModel(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.String(12), primary_key=True)
    vehicle_license = db.relationship('VehicleLicenseModel', back_populates='vehicle')

    error_papers = db.relationship("ErrorPaperModel", back_populates="vehicle", lazy="dynamic",cascade="all, delete")  