payment = Payment(
    user_id=user_id,
    amount=amount,
    memo=memo,
    metadata=metadata
)
db.session.add(payment)
db.session.commit()
