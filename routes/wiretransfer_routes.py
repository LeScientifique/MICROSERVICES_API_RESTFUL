from app import app
from config import db
from models import WireTransfer
from models.WireTransfer import WireTransfer

from flask import Flask, request, jsonify, render_template

from flask import Blueprint
wireTransfer_bp = Blueprint('wireTransfer', __name__)

#---------------------------------------------------------------------------------------------------------
#======================================================WIRE TRANSFER===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


#Methode d'ajout wireTransfer

@app.route('/wiretransfer/add', methods = ['POST'])
def wiretransfer_add():
    try:
        json = request.json
        print(json)
        bankID = json['bankID']
        bankName = json['bankName']
        amount = json['amount']
        payment_mode = json['payment_mode']
        orderId = json['orderId']

        if bankID and bankName and request.method == 'POST':
           
            print("******************")
            
            wiretransfer = WireTransfer(bankID = bankID, bankName = bankName, amount = amount, payment_mode = payment_mode, orderId = orderId)

            db.session.add(wiretransfer)
            db.session.commit()
            resultat = jsonify('New Wire Transfer add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()



#======================================================GET===============================================

#Methode GET pour wireTransfer

@app.route('/wireTransfer', methods = ['GET'])
def get_wiretransfers():
    try:
        wiretransferx = WireTransfer.query.all()
        data = [
                {
                    "id":wireTransfer.id, 
                    "bankID":wireTransfer.bankID, 
                    "bankName":wireTransfer.bankName, 
                } 
                for wireTransfer in wiretransferx
                ]

        resultat = jsonify({"status_code":200, "Wire Transfer" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()



