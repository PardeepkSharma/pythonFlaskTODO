from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager,create_access_token

db=SQLAlchemy()
jwt= JWTManager()
