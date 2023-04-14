from database.db import db

class ErrorPaperModel(db.Model) :
    __tablename__ = 'error_papers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(88), nullable=False)
    error_description = db.Column(db.String(200), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id") , unique=False, nullable=False)

    vehicle = db.relationship("VehicleModel", back_populates="error_papers")

