from src import db


class Type(db.Model):

    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey(
        'events.id', onupdate='CASCADE', ondelete='CASCADE'))
    price: db.Column(db.Integer, default=0)
    total_amount: db.Column(db.Integer, default=0)
    left_amount: db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Type, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.id} Ticket type is {self.name}."
