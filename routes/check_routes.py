from app import app
from config import db
from models.Check import Check
from flask import Flask, request, jsonify, render_template

from flask import Blueprint
check_bp = Blueprint('check', __name__)




#---------------------------------------------------------------------------------------------------------
#======================================================CHECK===============================================
#---------------------------------------------------------------------------------------------------------



#======================================================POST===============================================


#Methode d'ajout check

@app.route('/check/add', methods = ['POST'])
def check_add():
    try:
        json = request.json
        print(json)
        name = json['name']
        bankID = json['bankID']
        amount = json['amount']
        payment_mode = json['payment_mode']
        orderId = json['orderId']

        if name and bankID and request.method == 'POST':
           
            print("******************")
            
            checks = Check(name = name, bankID = bankID, amount = amount, payment_mode = payment_mode, orderId = orderId)

            db.session.add(checks)
            db.session.commit()
            resultat = jsonify('New Check add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#======================================================GET===============================================

#Methode GET pour Check

@app.route('/check', methods = ['GET'])
def get_checks():
    try:
        checksx = Check.query.all()
        data = [
                {
                    "id":checks.id, 
                    "name":checks.name, 
                    "bankID":checks.bankID 
                } 
                for checks in checksx
                ]

        resultat = jsonify({"status_code":200, "Check" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


