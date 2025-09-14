from flask import Flask
from . import database
from modules.data.models import HomePagesServices


class DatabaseService:
    def __init__(self, app: Flask):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:Welkom01@localhost:5432/keyswitches4you-db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        database.init_app(app)
        self.db = database

    def get_database_object(self):
        return self.db

    def retrieve_page(self, key: str) -> HomePagesServices:
        return HomePagesServices.query.filter_by(key=key).first()