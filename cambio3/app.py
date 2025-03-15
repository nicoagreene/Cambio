from flask import Flask, render_template, request, jsonify, session # request offeres a simple and convient way to acess JSON
from gameLogic.Game import Game
from gameLogic.Player import Player
from gameLogic.Bot import Bot
import json

app = Flask(__name__) #Flask constructor
app.secret_key = 'your-secret-key-here'  # Required for session management

#Decorator used to tell the application which URL is ascociated function
@app.route('/')
def home():
    return render_template('index.html')# when web page opens  this function will be rendered, targeting our html document


if __name__ == '__main__':#This is what makes app actually run 
    app.run(debug=True)


"""
Notes on flask:
    -In flask a function becomes a page when there is the @app.route() decorator
    -with app.route("/<>) whatever is inside comparisons can be passed in and used by user
    -redirect function can help to redirect the page user is on 

Templates: How to have flask interact with html, css, javascript
    -import render_template is necesarry to render separate html as template for flask app 
    -inside of html code you can actually write python code: must be between {% %} -- I think this is jinja2 thing
Adding template inheritace(base template):
    -Lets say you want to add a template that will persist throughout ur pages but wont be rendered alone (heade for example)
HTTP methods, get and post:
    -get -- insecure way of getting information, most commonly used 
    -post -- secure way of getting information
    -forms are a way of sending information to server. Put stuff you want to send inside the form tags
        -<form action = # method = 'post'> # means stay on page     
            input tags in here
        </form> 
Sessions:
    -something you load in when user on website and use to store data about user while they are on the page.
    -when user leaves data is gone but when theyu come back it reloads. It appears main application of sessions is for login/accounts
    -session in flask stores data as a dictionary

JSON -- Javscript Object Notation



GOAL: By the end of the week (2.9)  have significant work done on implementation of play, draw card and cambio

"""