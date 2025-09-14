from flask import Flask
from modules.data.database_service import DatabaseService
from modules.logic.logic_controller import LogicController
from modules.ui.webapp import WebappController

def main():
    app = Flask(__name__)
    db_service = DatabaseService(app)
    logic_controller = LogicController(db_service)
    webapp_interface = WebappController(logic_controller)
    webapp_interface.register_routes(app)
    app.run(debug=True)

if __name__ == "__main__":
    main()
