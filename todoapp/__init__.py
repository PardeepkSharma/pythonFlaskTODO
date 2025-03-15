from flask import Flask
import os
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    # Use an absolute path to the SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'todo.db')
    app.config['SQLALCHEMY_ECHO'] = True  # Enable logging of SQL statements
    app.config['SECRET_KEY'] = 'mysession'  # Needed for Flask sessions
    app.config['JWT_SECRET_KEY']="mysecretkey123"
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=1)  # Token expiration

    return app









