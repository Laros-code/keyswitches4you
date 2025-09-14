from . import database

class HomePagesServices(database.Model):
    __tablename__ = 'homepage'

    id = database.Column(database.Integer, primary_key=True)
    key = database.Column(database.String(50), nullable=False, unique=True)
    value = database.Column(database.Text, nullable=False)
