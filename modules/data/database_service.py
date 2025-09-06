class DatabaseService:
    def get_message(self):
        # Simpele data return
        return "Hello World"

    def get_price(self, item: int) -> float:
        if not item:
            return 22.0
        return 44.0
