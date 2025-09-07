from modules.data.database_service import DatabaseService


class LogicController:
    def __init__(self, data_service: DatabaseService):
        self.data = data_service

    def get_message(self):
        # Logica kan later complexer worden
        return self.data.get_message()

    def get_stockprice(self, item: int) -> float:
        return self.data.get_price(item)

    def get_about_small_text(self) -> dict:
        return {
            "title": "Looking for the best products?",
            "description": "This template is free to use for your business websites. However, you have no permission to redistribute the downloadable ZIP file on any template collection website.",
            "list_items": [
                "Lorem ipsum dolor sit amet",
                "Consectetur an adipisicing elit",
                "Itaquecorporis nulla aspernatur",
                "Corporis, omnis doloremque",
                "Non cum id reprehenderit",
            ],
        }
