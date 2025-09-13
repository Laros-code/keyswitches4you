from modules.data.models import Page

class DatabaseService:
    def __init__(self):
        pass  # geen db nodig hier, we gebruiken gewoon het model

    def get_message(self) -> str:
        return "Hello World"

    def get_price(self, item: int) -> float:
        if not item:
            return 22.0
        return 44.0

    def get_page_by_name(self, page_name: str) -> Page | None:
        return Page.query.filter_by(page_name=page_name).first()
