from dataclasses import dataclass

from bookmark import db

@dataclass
class Book(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Product %d>' % self.id