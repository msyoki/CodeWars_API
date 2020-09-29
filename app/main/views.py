from . import main
from flask import render_template


@main.route('/')
def index():
    hello='Hello World'
    return render_template('index.html',hello=hello)