from flask import Flask, jsonify, Blueprint
from application.models import Customer
from datetime import datetime
apiCustomers = Blueprint('apiCustomers',__name__,url_prefix='/api/customers')

@apiCustomers.route('/')
def customers():
  allCustomers= Customer.get_all_customers()
  customers = []
  for customer in allCustomers:
        
    customers.append({"id":customer.id, "date": customer.date,"gender":customer.gender,"age":customer.age})
    
  return jsonify({"sucess":True, "data":allCustomers})

@apiCustomers.route('/addCustomer')
def add_customers():
    now=datetime.utcnow()
    id=2
    Customer.add_customer(id,now,"gender","12")