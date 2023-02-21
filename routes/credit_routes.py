from app import app
from config import db
from models.Credit import Credit
from flask import Flask, request, jsonify, render_template

from flask import Blueprint
credit_bp = Blueprint('credit', __name__)



#---------------------------------------------------------------------------------------------------------
#======================================================CREDIT===============================================
#---------------------------------------------------------------------------------------------------------


#======================================================POST===============================================


#Methode d'ajout credit

@app.route('/credit/add', methods = ['POST'])
def credit_add():
    try:
        json = request.json
        print(json)
        number = json['number']
        types = json['types']
        expireDate = json['expireDate']
        amount = json['amount']
        payment_mode = json['payment_mode']
        orderId = json['orderId']

        if number and types and expireDate and request.method == 'POST':
           
            print("******************")

            credit = Credit(number = number, types = types, expireDate = expireDate, amount = amount, payment_mode = payment_mode, orderId = orderId)

            db.session.add(credit)
            db.session.commit()
            resultat = jsonify('New Credit add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#======================================================GET===============================================

#Methode GET pour Credit

@app.route('/credit', methods = ['GET'])
def get_credits():
    try:
        creditx = Credit.query.all()
        data = [
                {
                    "id":credit.id, 
                    "number":credit.number, 
                    "types":credit.types, 
                    "expireDate":credit.expireDate
                } 
                for credit in creditx
                ]

        resultat = jsonify({"status_code":200, "Credit" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


