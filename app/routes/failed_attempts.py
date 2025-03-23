from flask import Blueprint, request, jsonify
from monitor.failed_attempts import FailedAttemptsMonitor
from monitor.failed_orders import FailedOrdersMonitor

failed_attempts_blueprint = Blueprint('failed_attempts', __name__)

# Initialize monitors
failed_attempts_monitor = FailedAttemptsMonitor()
failed_orders_monitor = FailedOrdersMonitor()

@failed_attempts_blueprint.route('/failed-attempts', methods=['GET'])
def get_failed_attempts():
    """Get recent failed attempts"""
    user_id = request.args.get('user_id')
    email = request.args.get('email')
    ip = request.args.get('ip')
    attempts = failed_attempts_monitor.get_recent_failed_attempts(user_id, email, ip)
    return jsonify(attempts)

@failed_attempts_blueprint.route('/failed-orders', methods=['GET'])
def get_failed_orders():
    """Get recent failed orders"""
    link = request.args.get('link')
    attempts = failed_orders_monitor.get_attempts(link)
    return {'attempts': attempts,
            'link': link}
    # return jsonify(attempts)

@failed_attempts_blueprint.route('/record-failed-attempt', methods=['POST'])
def record_failed_attempt():
    """Record a failed attempt"""
    data = request.json
    user_id = data.get('user_id')
    email = data.get('email')
    ip = data.get('ip')
    failed_attempts_monitor.record_failed_attempt(user_id, email, ip)
    return jsonify({'message': 'Failed attempt recorded'})

@failed_attempts_blueprint.route('/record-failed-order', methods=['POST'])
def record_failed_order():
    """Record a failed order"""
    data = request.json
    link = data.get('link')
    failed_orders_monitor.add_attempt(link)
    return jsonify({'message': 'Failed order recorded'})