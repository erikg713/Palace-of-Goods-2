@payment_bp.route('/webhook', methods=['POST'])
def payment_webhook():
    data = request.get_json()
    payment_id = data.get('identifier')
    status = data.get('status')

    if not payment_id or not status:
        return jsonify({"msg": "Invalid webhook payload"}), 400

    # Update payment in your database
    payment = Payment.query.filter_by(identifier=payment_id).first()
    if payment:
        payment.status = status
        db.session.commit()
    return jsonify({"msg": "Webhook processed"}), 200