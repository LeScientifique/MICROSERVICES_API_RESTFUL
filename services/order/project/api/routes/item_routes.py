from project import db
from project.api.models import Item
from flask import request, jsonify
from flask import Blueprint

item_bp = Blueprint('item', __name__)


#---------------------------------------------------------------------------------------------------------
#======================================================ITEM===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


#Methode d'ajout item

@item_bp.route('/item/add', methods = ['POST'])
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

@item_bp.route('/item', methods = ['GET'])
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


#====================================================== UPDATE ===============================================


@item_bp.route('/item/update', methods = ['POST', 'GET'])
def item_update():
    try:
        data = request.json
        id = data["id"]
        weight = data['weight']
        description = data['description']

        items = Item.query.filter_by(id=id).first()
        
        if id and weight and description and request.method == 'POST':

            items.weight = weight
            items.description = description
            db.session.commit()
            resultat = jsonify('item is update')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()


#====================================================== DELETE ===============================================

###DELETE de item
@item_bp.route('/item/delete', methods = ['POST'])
def delete_item():
    try:
        json = request.json
        id = json['id']

        item = Item.query.filter_by(id=id).first()
        
        db.session.delete(item)
        db.session.commit()
        resultat = jsonify('Item is successfully deleted')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 400, "message": 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()
