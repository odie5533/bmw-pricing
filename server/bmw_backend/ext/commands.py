import click
import csv
from datetime import datetime

from bmw_backend.ext.auth import create_user
from bmw_backend.ext.database import db
from bmw_backend.models import CarSale


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    # Read the csv file bmw_pricing_challenge.csv and populate the database
    # by creating a CarSale object for each row in the csv file
    def parse_date(date):
        return datetime.strptime(date, "%Y-%m-%d")
    data = []
    with open("bmw_pricing_challenge.csv") as csv_file:
        # skip the header
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            data.append(
                CarSale(
                    maker_key=row[0],
                    model_key=row[1],
                    mileage=row[2],
                    engine_power=row[3],
                    registration_date=parse_date(row[4]),
                    fuel=row[5],
                    paint_color=row[6],
                    car_type=row[7],
                    price=row[16],
                    sold_at=parse_date(row[17]),
                )
            )
    db.session.bulk_save_objects(data)
    db.session.commit()
    return CarSale.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option("--username", "-u")
    @click.option("--password", "-p")
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
