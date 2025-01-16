from app import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    pi_payment_id = db.Column(db.String(255), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    memo = db.Column(db.String(255))
    metadata = db.Column(db.JSON)
    status = db.Column(db.String(50), default='PENDING')  # PENDING, COMPLETED, FAILED
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    completed_at = db.Column(db.DateTime, nullable=True)
