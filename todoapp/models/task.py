# Creating a model for tasks

from ..extentions import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.id}-{self.task}-{self.desc}"
    
