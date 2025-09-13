from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # wordt later in main() gekoppeld aan app

class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)