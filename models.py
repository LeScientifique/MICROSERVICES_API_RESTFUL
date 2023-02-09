from config import db

class Order (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    createDate = db.Column(db.Date, nullable = False)

    ## OneToMany de Customer vers Order
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = True)
    customer = db.relationship('Customer', foreign_keys = [customerId])


class Customer (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    deliveryAddress = db.Column(db.String(120), nullable = False)
    contact = db.Column(db.String(120), nullable = True)
    active = db.Column(db.Boolean, nullable = False)

class OrderStatus (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    CREATE = db.Column(db.Integer, nullable = False)
    SHIPPING = db.Column(db.Integer, nullable = False)
    DELIVERED = db.Column(db.Integer, nullable = False)
    PAID = db.Column(db.Integer, nullable = False)

class Item (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    weight = db.Column(db.Float, nullable = False)
    description = db.Column(db.String(255), nullable = False)

class OrderDetail (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    qty = db.Column(db.Integer, nullable = False)
    taxStatus = db.Column(db.String(120), nullable = False)

    ## OneToMany de Item vers OrderDetail
    itemId = db.Column(db.Integer, db.ForeignKey('item.id'), nullable = True)
    item = db.relationship('Item', foreign_keys = [itemId])

    ## OneToMany de Order vers OrderDetail
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True)
    order = db.relationship('Order', foreign_keys = [orderId])

class Payment (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float, nullable = False)

    ## OneToMany de Order vers payment
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True)
    order = db.relationship('Order', foreign_keys = [orderId])






class Credit (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.String(120), nullable = False)
    types = db.Column(db.String(120), nullable = False)
    expireDate = db.Column(db.Date, nullable = False)


class Cash (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cashTendered = db.Column(db.Float, nullable = False)

class Check (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    bankID = db.Column(db.String(120), nullable = False)

class WireTransfer (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    bankID = db.Column(db.String(120), nullable = False)
    bankName = db.Column(db.String(120), nullable = False)
