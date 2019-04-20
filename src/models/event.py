from src import db
from datetime import datetime


class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    description = db.Column(db.Text(), nullable=False)
    image_url: db.Column(db.Text(), nullable=False)
    address: db.Column(db.Text(), nullable=False)
    time: db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    ticket_types = db.relationship('types', backref='event')

    def __init__(self, name, description, image_url, price, address, time):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.price = price
        self.address = address
        self.time = time

    def __repr__(self):
        return f"{self.id} Event name is {self.name}."
