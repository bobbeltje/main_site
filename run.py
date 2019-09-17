
from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/pydash')
def pydash():
    return render_template('dash.html', title='Dash')

@app.route('/shiny')
def shiny():
    return render_template('shiny.html', title='Shiny')

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
        user = form.username.data
        password = form.password.data
        if user == 'bobbel' and  password == 'testing':
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
