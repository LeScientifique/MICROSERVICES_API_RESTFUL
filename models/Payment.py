from config import db

class Payment (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float, nullable = False)

    ## OneToMany de Order vers payment
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True)
    order = db.relationship('Order', foreign_keys = [orderId])

    ## Methode pour rendre la classe Mere(Heritage)
    _mapper_args_ = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': 'payment_mode'
    }
