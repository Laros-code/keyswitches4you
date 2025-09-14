from modules.data.database_service import DatabaseService


class LogicController:
    def __init__(self, data_service: DatabaseService):
        self.data = data_service

    def get_header_intro_text(self) -> str:
        page = self.data.retrieve_page("header_intro_text")
        return page.value if page else "empty"

    def get_header_intro_text_extend(self) -> str:
        page = self.data.retrieve_page("header_intro_text_extend")
        return page.value if page else "empty"

    def some_message(self) -> str:
        return "dit is gewoon een bericht"

    def load_home_page_context(self) -> dict:
        return {
            "header_intro_text": self.get_header_intro_text(),
            "header_intro_text_extend": self.get_header_intro_text_extend(),
            "home_data": self.some_message()
        }