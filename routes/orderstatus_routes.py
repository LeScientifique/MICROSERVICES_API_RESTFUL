from app import app
from config import db
from models.OrderStatus import OrderStatus
from flask import Flask, request, jsonify, render_template

from flask import Blueprint
orderStatus_bp = Blueprint('orderStatus', __name__)


#---------------------------------------------------------------------------------------------------------
#======================================================ORDER STATUS===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


#Methode d'ajout orderStatus

@app.route('/orderStatus/add', methods = ['POST'])
def orderstatus_add():
    try:
        json = request.json
        print(json)
        CREATE = json['CREATE']
        SHIPPING = json['SHIPPING']
        DELIVERED = json['DELIVERED']
        PAID = json['PAID']

        if CREATE and SHIPPING and DELIVERED and PAID and request.method == 'POST':
           
            print("******************")

            orderStatus = OrderStatus(CREATE = CREATE, SHIPPING = SHIPPING, DELIVERED = DELIVERED, PAID = PAID)

            db.session.add(orderStatus)
            db.session.commit()
            resultat = jsonify('Order Status add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#======================================================GET===============================================

#Methode GET pour orderStatus

@app.route('/orderStatus', methods = ['GET'])
def get_orderstatus():
    try:
        orderstatusx = OrderStatus.query.all()
        data = [
                {
                    "id":orderStatus.id, 
                    "CREATE":orderStatus.CREATE, 
                    "SHIPPING":orderStatus.SHIPPING, 
                    "DELIVERED":orderStatus.DELIVERED, 
                    "PAID":orderStatus.PAID
                } 
                for orderStatus in orderstatusx
                ]

        resultat = jsonify({"status_code":200, "Order status" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

