from flask import Blueprint

customer = Blueprint('customer', __name__)

@customer.route('/customer')
def customer_index():
    return 'Hello, customer!'