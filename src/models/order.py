from src import db


class Order(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer(), primary_key=True)
    coupon = db.Column(db.String(20), default=0)
    total_bill = db.Column(db.Integer(), default=0)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    event_id = db.Column(db.Integer(), db.ForeignKey('events.id'))

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Type, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.id} Order id"
