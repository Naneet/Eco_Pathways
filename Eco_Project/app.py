from flask import Flask, render_template, request

app = Flask(__name__)

@app. route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/login')
def contact():
    return render_template('login.html')

@app.route('/register')
def contact():
    return render_template('register.html')