
from flask import render_template, url_for, flash, redirect
from flask_login import login_user, logout_user, login_required
from main_site.forms import LoginForm
from main_site.models import User
from main_site import app, bcrypt

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/pydash')
@login_required
def pydash():
    return render_template('dash.html', title='Dash')

@app.route('/shiny')
@login_required
def shiny():
    return render_template('shiny.html', title='Shiny')

@app.route('/tmp')
@login_required
def tmp():
    return redirect('tmp/')

@app.route('/weather')
def weather():
    return render_template('weather.html', title='Weather')
   
@app.route('/about')
def about():
    return render_template('about.html', title='About time')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User()
        cond_1 = form.username.data == user.username
        cond_2 = bcrypt.check_password_hash(user.password, form.password.data)
        if cond_1 and cond_2:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
