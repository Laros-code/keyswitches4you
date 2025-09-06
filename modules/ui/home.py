from flask import Blueprint, render_template, request
from modules.logic.logic_controller import LogicController

class UiHandler:
    def __init__(self, logic_controller: LogicController):
        self.logic = logic_controller
        self.bp = Blueprint("ui", __name__)

        # Routes registreren
        self.bp.add_url_rule("/", "home", self.home, methods=["GET", "POST"])

    def home(self):
        message = ""
        stock_message = ""
        if request.method == "POST":
            if "hello_btn" in request.form:
                message = self.logic.get_message()
            elif "check_price" in request.form:
                stock_message = str(self.logic.get_stockprice(0))
            elif "clear_btn" in request.form:
                message = ""
                stock_message = ""
        return render_template("index.html", message=message, stock_message=stock_message)

    def register_routes(self, app: Blueprint):
        app.register_blueprint(self.bp)
