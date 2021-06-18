"""
Main app starting point.

https://flask.palletsprojects.com/en/1.1.x/quickstart
"""
import os
from flask import Flask
from app.main_page import main_page
from app.auth import login, register

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Blueprints
app.register_blueprint(main_page)
app.register_blueprint(login)
app.register_blueprint(register)

if __name__ == "__main__":
    app.run(debug=True)
