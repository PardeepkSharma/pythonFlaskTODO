# Creating a model for tasks
from ..extentions import db

class User(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(20),nullable=False)
    email= db.Column(db.String(20),nullable=False)
    password= db.Column(db.String(20),nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }
    def __repr__(self):
        return f"{self.id}-{self.username}-{self.email}={self.password}"


