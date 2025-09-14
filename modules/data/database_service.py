from flask import Flask
from sqlalchemy import inspect

from . import database
from modules.data.models import HomePagesServices


class DatabaseService:
    def __init__(self, app: Flask):
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            "postgresql+psycopg2://admin:Welkom01@localhost:5432/keyswitches4you-db"
        )
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        database.init_app(app)
        self.db = database

    def retrieve_all_page_content(self, page: str) -> dict[str, str]:
        if self.__list_tables(page) == "":
            raise Exception("Table not found")
        rows = HomePagesServices.query.all()
        data: dict[str, str] = {}
        for row in rows:
            data[row.key] = row.value
        return data

    def __list_tables(self, table_name: str) -> str:
        for table in inspect(self.db.engine).get_table_names():
            if table == table_name:
                return table
        return ""
