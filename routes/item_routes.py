from app import app
from config import db
from models.Item import Item
from flask import Flask, request, jsonify, render_template

from flask import Blueprint
item_bp = Blueprint('item', __name__)


#---------------------------------------------------------------------------------------------------------
#======================================================ITEM===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


#Methode d'ajout item

@app.route('/item/add', methods = ['POST'])
def item_add():
    try:
        json = request.json
        print(json)
        weight = json['weight']
        description = json['description']

        if weight and description and request.method == 'POST':
           
            print("******************")

            item = Item(weight = weight, description = description)

            db.session.add(item)
            db.session.commit()
            resultat = jsonify('New Item add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#======================================================GET===============================================

#Methode GET pour Item

@app.route('/item', methods = ['GET'])
def get_items():
    try:
        itemsx = Item.query.all()
        data = [
                {
                    "id":item.id, 
                    "weight":item.weight, 
                    "description":item.description
                } 
                for item in itemsx
                ]

        resultat = jsonify({"status_code":200, "Item" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


