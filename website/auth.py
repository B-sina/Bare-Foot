import flask
from website.models import User
from . import db
from flask import Blueprint, render_template, request, flash, redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask.helpers import flash

from flask_login import login_user, login_required, logout_user, current_user

# blueprint for our flask application to organize our application
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in successfully!', category='success')
                login_user(user)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect pasword, try again.', category='error')
        else:
            flash('Email does not exist.', category='error' )  
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect( url_for('auth.login') )


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fullName = request.form.get('fullName')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')

        elif len(email) < 4:
            flash('Email has to be greater than three charactors', category='error')
        elif len(fullName) < 3:
            flash('The fullName has to greater than two charactors', category='error')
        elif password != confirmPassword:
            flash('The passwords doesn\'t much', category='error')
        elif len(password) < 7:
            flash('the minimum password has to be  more than 7', category='error')
        else:
            new_user = User(email = email, full_name= fullName,  password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user)
            flash('Account is created! ', category='success')
            # note
            # change it to :- redirect(url_for('views.home'))
            return redirect(url_for('views.home'))


    return render_template("signUp.html", user=current_user)
