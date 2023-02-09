from app import app
from config import db
from models import Customer, Order, OrderDetail, OrderStatus, Item, Payment, Credit, Cash, Check, WireTransfer
from flask import Flask, request, jsonify, render_template

with app.app_context():
    db.create_all()


"""Methode et route"""

#======================================================POST===============================================


#Methode d'ajout customer

@app.route('/customer/add', methods = ['POST'])
def customer_add():
    try:
        json = request.json
        print(json)
        name = json['name']
        deliveryAddress = json['deliveryAddress']
        contact = json['contact']
        active = json['active']

        if name and deliveryAddress and contact and active and request.method == 'POST':
           
            print(" ****************** ")
            customers = Customer(name = name, deliveryAddress = deliveryAddress, contact = contact, active = active)

            db.session.add(customers)
            db.session.commit()
            resultat = jsonify('Customer add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#Methode d'ajout order


@app.route('/order/add', methods = ['POST'])
def order_add():
    try:
        json = request.json
        print(json)
        createDate = json['createDate']
        customerId = json['customerId']

        if createDate and request.method == 'POST':
           
            print("******************")

            orders = Order(createDate = createDate)

            if customerId :
                customer = Customer.query.filter_by(id = customerId).first()
                print(customer)
                orders.customer = customer

            db.session.add(orders)
            db.session.commit()
            resultat = jsonify('Order add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


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
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()



#Methode d'ajout orderDetail



@app.route('/orderDetail/add', methods = ['POST'])
def orderdetail_add():
    try:
        json = request.json
        print(json)
        qty = json['qty']
        taxStatus = json['taxStatus']

        if qty and taxStatus and request.method == 'POST':
           
            print("******************")

            orderDetail = OrderDetail(qty = qty, taxStatus = taxStatus)

            db.session.add(orderDetail)
            db.session.commit()
            resultat = jsonify('New Order Detail add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()




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
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()



#Methode d'ajout paymet


@app.route('/payment/add', methods = ['POST'])
def payment_add():
    try:
        json = request.json
        print(json)
        amount = json['amount']

        if amount and request.method == 'POST':
           
            print("******************")
            payments = Payment(amount = amount)

            db.session.add(payments)
            db.session.commit()
            resultat = jsonify('New Payment add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

#Methode d'ajout Credit


@app.route('/credit/add', methods = ['POST'])
def credit_add():
    try:
        json = request.json
        print(json)
        number = json['number']
        types = json['types']
        expireDate = json['expireDate']

        if number and types and expireDate and request.method == 'POST':
           
            print("******************")

            credits = Credit(number = number, types = types, expireDate = expireDate)

            db.session.add(credits)
            db.session.commit()
            resultat = jsonify('New Credit add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#Methode d'ajout Cash


@app.route('/Cash/add', methods = ['POST'])
def cash_add():
    try:
        json = request.json
        print(json)
        cashTendered = json['cashTendered']

        if cashTendered and request.method == 'POST':
           
            print("******************")
            
            cashs = Cash(cashTendered = cashTendered)

            db.session.add(cashs)
            db.session.commit()
            resultat = jsonify('New Cash add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#Methode d'ajout check


@app.route('/check/add', methods = ['POST'])
def check_add():
    try:
        json = request.json
        print(json)
        name = json['name']
        bankID = json['bankID']

        if name and bankID and request.method == 'POST':
           
            print("******************")
            
            checks = Check(name = name, bankID = bankID)

            db.session.add(checks)
            db.session.commit()
            resultat = jsonify('New Check add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()



@app.route('/wiretransfer/add', methods = ['POST'])
def wiretransfer_add():
    try:
        json = request.json
        print(json)
        bankID = json['bankID']
        bankName = json['bankName']

        if bankID and bankName and request.method == 'POST':
           
            print("******************")
            
            wiretransfer = WireTransfer(bankID = bankID, bankName = bankName)

            db.session.add(wiretransfer)
            db.session.commit()
            resultat = jsonify('New Wire Transfer add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#======================================================GET===============================================

#Methode GET pour Customer
@app.route('/customers', methods = ['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        data = [{"id":customers.id, "name":customers.name, "deliveryAddress":customers.deliveryAddress, "contact":customers.contact, "active":customers.active} for customers in customers]

        resultat = jsonify({"status_code":200, "Customer" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()














if(__name__ == '__main__'):
    app.run(debug=True, host= "0.0.0.0", port= 2000)
