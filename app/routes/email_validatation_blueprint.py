from flask import Blueprint, request
from analyzer.email import EmailAnalyzer

email_validation_blueprint = Blueprint('email_validation', __name__)


@email_validation_blueprint.route('/validate_email')
def validate_email():
    email = request.args.get('email')
    print(email)
    
    analyzer = EmailAnalyzer()
    if not analyzer.is_valid(email):
        return f"Email: {email} \n This is an invalid email"
    else:
        return f"Email: {email} \n This is a valid email"
    
