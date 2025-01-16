payment = Payment.query.filter_by(pi_payment_id='unique_payment_id').first()
if payment:
    payment.status = 'COMPLETED'  # Update status
    payment.completed_at = db.func.current_timestamp()  # Save completion timestamp
    db.session.commit()
