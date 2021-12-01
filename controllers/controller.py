from app import app
from flask import render_template
from models.order_list import tasks

@app.route('/tasks')
def index():
    return render_template('index.html', title='Home', task=tasks)


