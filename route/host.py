from flask import Blueprint

host = Blueprint('host', __name__)

@host.route('/host')
def customer_index():
    return 'Hello, host!'