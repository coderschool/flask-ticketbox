from src import db


class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # owner = db.relationship('Owner',backref='event',uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Event name is {self.name}."
