from config import db

class OrderStatus (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    CREATE = db.Column(db.Integer, nullable = False)
    SHIPPING = db.Column(db.Integer, nullable = False)
    DELIVERED = db.Column(db.Integer, nullable = False)
    PAID = db.Column(db.Integer, nullable = False)
