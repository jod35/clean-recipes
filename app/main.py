from flask import Flask,render_template,redirect
import requests

app=Flask(__name__)

@app.route('/')
def index():
    context={
        'results':""
    }
    return render_template('index.html',**context)

@app.route('/details')
def details():
    return render_template('details.html')