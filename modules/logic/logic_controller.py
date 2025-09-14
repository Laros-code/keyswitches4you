from modules.data.database_service import DatabaseService


class LogicController:
    def __init__(self, data_service: DatabaseService):
        self.data = data_service

    def get_header_intro_text(self) -> str:
        return "Kaasboer"

    def get_header_intro_text_extend(self) -> str:
        return "Met spek!"

    # def get_page_content(self, page_name: str) -> str:
    #     page = self.data.get_page_by_name(page_name)
    #     return page.content if page else "Geen content gevonden"

    def some_message(self) -> str:
        return "dit is gewoon een bericht"

    def load_home_page_context(self) -> dict:
        return {
            "header_intro_text": self.get_header_intro_text(),
            "header_intro_text_extend": self.get_header_intro_text_extend(),
            "home_data": self.some_message()
        }