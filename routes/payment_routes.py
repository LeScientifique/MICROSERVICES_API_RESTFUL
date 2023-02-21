from app import app
from config import db
from models.Order import Order
from models.Payment import Payment
from flask import Flask, request, jsonify, render_template

from flask import Blueprint
payment_bp = Blueprint('payment', __name__)


#---------------------------------------------------------------------------------------------------------
#======================================================PAYMENT===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


#Methode d'ajout payment

@app.route('/payment/add', methods = ['POST'])
def payment_add():
    try:
        json = request.json
        print(json)
        amount = json['amount']
        payment_mode = json['payment_mode']
        orderId = json['orderId']

        if amount and request.method == 'POST':
           
            print("******************")
            payments = Payment(amount = amount, payment_mode = payment_mode)

            if orderId :
                order = Order.query.filter_by(id = orderId).first()
                print(order)
                payments.order = order

            db.session.add(payments)
            db.session.commit()
            resultat = jsonify('New Payment add')
            return resultat

    except Exception as e :
        print(e)
        resultat = e
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

#======================================================GET===============================================

#Methode GET pour payment

@app.route('/payment', methods = ['GET'])
def get_payments():
    try:
        paymentsx = Payment.query.all()
        data = [
                {
                    "id":payments.id, 
                    "amount":payments.amount,
                    "payment_mode" : payments.payment_mode, 
                    "orderId" : payments.orderId
                } 
                for payments in paymentsx
                ]

        resultat = jsonify({"status_code":200, "Payment" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


