from app import app
from flask import render_template
from models import order
from models.order_list import orders

@app.route('/')
def start():
    return "Welcome to Jamie's Shoe Shop!"

@app.route('/orders')
def index():
    return render_template('index.html', title='Orders', orders=orders)

@app.route('/orders/<index>')
def specific_order(index):
    order = orders[int(index)]
    return render_template('order.html', title='Specific', order=order(index))
