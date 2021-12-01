from app import app
from flask import render_template
from models.stock_list import tasks

@app.route('/')
def index():
    return render_template("Welcome to Jamie's shoe shop")