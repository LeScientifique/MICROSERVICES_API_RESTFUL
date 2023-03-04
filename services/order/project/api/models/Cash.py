from project.__init__ import db
from project.api.models import Payment


class Cash (Payment):
    
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    cashTendered = db.Column(db.Float, nullable = False)


    _mapper_args_ = {
        'polymorphic_identity' : 'cash'
    }
    
