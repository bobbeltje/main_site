
from flask import Flask, render_template, url_for

app = Flask(__name__)

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

# to run the app without setting environmental variables
if __name__ == '__main__':
    app.run(debug=True)
