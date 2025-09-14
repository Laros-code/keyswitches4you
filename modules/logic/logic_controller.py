from modules.data.database_service import DatabaseService


class LogicController:
    def __init__(self, data_service: DatabaseService):
        self.data = data_service

    def _get_home_page_content(self) -> dict:
        content = self.data.retrieve_all_page_content("homepage")
        if not content:
            raise Exception("No content found")
        return content

    def load_home_page_context(self) -> dict:
        home_page_data = self._get_home_page_content()
        return home_page_data
