from flask import Flask
from modules.data.database_service import DatabaseService
from modules.logic.logic_controller import LogicController
from modules.ui.home import UiHandler

def main():
    # Initieer lagen
    data_layer = DatabaseService()
    logic_layer = LogicController(data_layer)
    ui_layer = UiHandler(logic_layer)

    # Start Flask app
    app = Flask(__name__)
    ui_layer.register_routes(app)

    app.run(debug=True)

if __name__ == "__main__":
    main()
