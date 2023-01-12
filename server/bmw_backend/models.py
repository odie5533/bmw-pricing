from sqlalchemy_serializer import SerializerMixin

from bmw_backend.ext.database import db
from sqlalchemy.ext.declarative import DeclarativeMeta

BaseModel: DeclarativeMeta = db.Model


class CarSale(BaseModel, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    maker_key = db.Column(db.String(140))
    model_key = db.Column(db.String(140))
    mileage = db.Column(db.Integer)
    engine_power = db.Column(db.Integer)
    registration_date = db.Column(db.Date)
    fuel = db.Column(db.String(140))
    paint_color = db.Column(db.String(140))
    car_type = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    sold_at = db.Column(db.Date)

class User(BaseModel, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
