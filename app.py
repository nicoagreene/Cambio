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


#deleted notes on flask 