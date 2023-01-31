import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class ShopItem(db.Model):
    __tablename__ = "shopItems"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    price = db.Column(db.Float(2))
    image_title = db.Column(db.String(100))
    image_url = db.Column(db.String(500))

    def __init__(self, name, price, description, image_title, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.image_title = image_title
        self.image_url = image_url
