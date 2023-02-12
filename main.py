from app import app
from config import db
from models import Cash, Check, Credit, Customer, Item, Order, OrderDetail, OrderStatus, Payment, WireTransfer
from models.Cash import Cash
from models.Check import Check
from models.Credit import Credit
from models.Customer import Customer
from models.Item import Item
from models.Order import Order
from models.OrderDetail import OrderDetail
from models.OrderStatus import OrderStatus
from models.Payment import Payment
from models.WireTransfer import WireTransfer

from flask import Flask, request, jsonify, render_template

with app.app_context():
    # db.drop_all()
    db.create_all()

"""Methode et route"""

#---------------------------------------------------------------------------------------------------------
#======================================================CASH===============================================
#---------------------------------------------------------------------------------------------------------


#======================================================POST===============================================

#Methode d'ajout cash

@app.route('/Cash/add', methods = ['POST'])
def cash_add():
    try:
        json = request.json
        print(json)
        cashTendered = json['cashTendered']
        amount = json['amount']
        payment_mode = json['payment_mode']
        orderId = json['orderId']

        if cashTendered and request.method == 'POST':
           
            print("******************")
           
            cashs = Cash(cashTendered = cashTendered, amount = amount, payment_mode = payment_mode, orderId = orderId)
            
            db.session.add(cashs)
            db.session.commit()
            resultat = jsonify('New Cash add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Une erreur s'est produite" }
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

#======================================================GET===============================================

#Methode GET pour Cash

@app.route('/cash', methods = ['GET'])
def get_cashs():
    try:
        cashsx = Cash.query.all()
        data = [
                {
                    "id":cashs.id, 
                    "cashTendered":cashs.cashTendered
                } 
                for cashs in cashsx
                ]

        resultat = jsonify({"status_code":200, "Cash" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()



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





#---------------------------------------------------------------------------------------------------------
#======================================================CUSTOMER===============================================
#---------------------------------------------------------------------------------------------------------


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
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()



#======================================================GET===============================================

#Methode GET pour Customer

@app.route('/customers', methods = ['GET'])
def get_customers():
    try:
        customersx = Customer.query.all()
        data = [
                {
                    "id":customers.id, 
                    "name":customers.name, 
                    "deliveryAddress":customers.deliveryAddress, 
                    "contact":customers.contact, 
                    "active":customers.active
                } 
                for customers in customersx
                ]

        resultat = jsonify({"status_code":200, "Customer" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()





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





#---------------------------------------------------------------------------------------------------------
#======================================================ORDER===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


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
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

#======================================================GET===============================================

#Methode GET pour Cash

@app.route('/order', methods = ['GET'])
def get_orders():
    try:
        ordersx = Order.query.all()
        data = [
                {
                    "id":orders.id, 
                    "createDate":orders.createDate, 
                    "customerId":orders.customerId, 
                } 
                for orders in ordersx
                ]

        resultat = jsonify({"status_code":200, "Order" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


#---------------------------------------------------------------------------------------------------------
#======================================================ORDER DETAIL===============================================
#---------------------------------------------------------------------------------------------------------

#======================================================POST===============================================


#Methode d'ajout orderDetail

@app.route('/orderDetail/add', methods = ['POST'])
def orderdetail_add():
    try:
        json = request.json
        print(json)
        qty = json['qty']
        taxStatus = json['taxStatus']
        orderId = json['orderId']
        itemId = json['itemId']

        if qty and taxStatus and request.method == 'POST':
           
            print("******************")

            orderDetail = OrderDetail(qty = qty, taxStatus = taxStatus)

            if orderId :
                order = Order.query.filter_by(id = orderId).first()
                print(order)
                orderDetail.order = order

            if itemId :
                item = Item.query.filter_by(id = itemId).first()
                print(item)
                orderDetail.item = item

            db.session.add(orderDetail)
            db.session.commit()
            resultat = jsonify('New Order Detail add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 400, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


#======================================================GET===============================================

#Methode GET pour orderDetail

@app.route('/orderDetail', methods = ['GET'])
def get_orderdetails():
    try:
        order_detailsx = OrderDetail.query.all()
        data = [
                {
                    "id":orderDetail.id, 
                    "qty":orderDetail.qty, 
                    "taxStatus":orderDetail.taxStatus, 
                    "orderId" : orderDetail.orderId,
                    "itemId" : orderDetail.itemId
                } 
                for orderDetail in order_detailsx
                ]

        resultat = jsonify({"status_code":200, "Order details" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 400, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()




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





if(__name__ == '__main__'):
    app.run(debug=True, host= "0.0.0.0", port= 2000)
