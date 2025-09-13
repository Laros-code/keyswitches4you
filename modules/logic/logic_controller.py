from modules.data.database_service import DatabaseService


class LogicController:
    def __init__(self, data_service: DatabaseService):
        self.data = data_service

    def get_message(self):
        # Logica kan later complexer worden
        return self.data.get_message()

    def get_stockprice(self, item: int) -> float:
        return self.data.get_price(item)

    def get_page_content(self, page_name: str) -> str:
        page = self.data.get_page_by_name(page_name)
        return page.content if page else "Geen content gevonden"