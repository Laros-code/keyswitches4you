from flask import Flask
from modules.data.database_service import DatabaseService
from modules.data.models import db
from modules.logic.logic_controller import LogicController
from modules.ui.webapp import WebappController
from flask_sqlalchemy import SQLAlchemy

def main():
    # create app
    app = Flask(__name__)
    #init pg16 database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:Welkom01@localhost:5432/keyswitches4you-db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # connect to database
    db.init_app(app)

    db_service = DatabaseService()
    logic_controller = LogicController(db_service)
    webapp_interface = WebappController(logic_controller)
    webapp_interface.register_routes(app)

    app.run(debug=True)


if __name__ == "__main__":
    main()
