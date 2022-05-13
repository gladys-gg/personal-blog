from flask import render_template, redirect, url_for, request
from . import main
from .forms import *
from datetime import datetime


#views
@main.route('/')
def index():
    return render_template('index.html')