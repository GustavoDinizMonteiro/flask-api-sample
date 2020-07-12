from dataclasses import dataclass

from bookmark import db

@dataclass
class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(255))
    password: str = db.Column(db.String(255))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Password %d>' % self.id