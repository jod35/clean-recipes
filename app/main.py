from flask import Flask, render_template, redirect, request
import requests
import os


url = "https://recipe-puppy.p.rapidapi.com/"

app = Flask(__name__)


headers = {
    'x-rapidapi-host': "recipe-puppy.p.rapidapi.com",
    'x-rapidapi-key': "00d077979fmsh387d90cf6e84a47p1c658fjsn75203996af2d"
}


@app.route('/', methods=['GET', 'POST'])
def index():
    results = ""
    if request.method == "POST":
        meal = request.form['meal']

        queryString = {"q": meal}

        response = requests.get(url=url, headers=headers, params=queryString)

        results = response.json()

        # return results

    context = {
        'results': results,

    }
    return render_template('index.html', **context)


@app.route('/details')
def details():
    return render_template('details.html')
