from . import db
from . import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, completed, failed
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, completed
    created_at = db.Column(db.DateTime, default=db.func.now())

class Payment(db.Model):
    milestones = db.Column(db.JSON, nullable=True)  # e.g., [{"amount": 10, "status": "paid"}]

milestones = [{"amount": 10, "status": "pending"}, {"amount": 15, "status": "pending"}]
payment = Payment(amount=total_amount, milestones=milestones)