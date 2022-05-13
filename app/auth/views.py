from flask import render_template,redirect,url_for
from . import auth 
from .forms import *


#views
@auth.route('/')
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    
    return render_template('auth/signUp.html', form= form)


@auth.route('/signIn', methods=['GET', 'POST'])
def signIn():
    
    return render_template('auth/signIn.html', title = 'Login', form= form)
