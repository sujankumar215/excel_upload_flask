from flask import Flask
from cricket.main import main
from cricket.batsmen import batsman
from cricket.bowler import bowler

def create_app():
    app= Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(bowler)
    app.register_blueprint(batsman)
    return app
