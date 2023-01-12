from flask import abort, jsonify
from flask_restful import Resource
from sqlalchemy import func

from bmw_backend.models import CarSale


class CarSaleSummaryResource(Resource):
    def get(self):
        fuel = CarSale.query.with_entities(CarSale.fuel, func.count(CarSale.fuel)).group_by(CarSale.fuel).all() or abort(204)
        paint_color = CarSale.query.with_entities(CarSale.paint_color, func.count(CarSale.paint_color)).group_by(CarSale.paint_color).all() or abort(204)
        return jsonify({
            "fuel": dict(fuel),
            "paint_color": dict(paint_color),
        })
