from flask import Blueprint, render_template, request, Flask
from modules.logic.logic_controller import LogicController


class WebappController:
    def __init__(self, logic_controller: LogicController):
        self.logic = logic_controller
        self.bp = Blueprint("ui", __name__)
        self.bp.add_url_rule("/", "home", self.home, methods=["GET", "POST"])
        self.bp.add_url_rule("/products", "products", self.products)
        self.bp.add_url_rule("/about", "about", self.about)
        self.bp.add_url_rule("/contact", "contact", self.contact)

    def home(self) -> str:
        about_str = self.logic.get_about_small_text()
        return render_template("index.html", about_data=about_str)

    def products(self) -> str:
        return render_template("products.html")

    def about(self) -> str:
        return render_template("about.html")

    def contact(self) -> str:
        return render_template("contact.html")

    def register_routes(self, app: Flask) -> None:
        app.register_blueprint(self.bp)
