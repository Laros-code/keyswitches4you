from modules.data.database_service import DatabaseService

class LogicController:
    def __init__(self, data_service: DatabaseService):
        self.data = data_service

    def get_message(self):
        # Logica kan later complexer worden
        return self.data.get_message()
    
    def get_stockprice(self, item: int) -> float:
        return self.data.get_price(item)
