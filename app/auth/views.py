from flask import render_template,redirect,url_for
from .forms import *
from app import bcrypt

#views
@auth.route('/')
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        
        # mail_message('Welcome to personal blog','email/welcome_user',user.email, user=user)
        return redirect(url_for('auth.signIn'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in creating the user:(err_msg)')
    
    return render_template('auth/signUp.html', form= form)


@auth.route('/signIn', methods=['GET', 'POST'])
def signIn():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form=LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('auth/signIn.html', title = 'Login', form= form)
