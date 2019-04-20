from src import db


class Ticket(db.Model):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer(), primary_key=True)
    status = db.Column(db.String(20), nullable=False)
    type_id = db.Column(db.Integer(), db.ForeignKey('types.id'))
    order_id = db.Column(db.Integer(), db.ForeignKey('orders.id'))

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Type, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.id} Ticket type is {self.name}."
