from flask import render_template,redirect,url_for
from .forms import *

#views
@auth.route('/')
@auth.route()
def register():
    return render_template('signUp.html', form= form)

