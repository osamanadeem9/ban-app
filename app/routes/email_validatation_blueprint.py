from flask import Blueprint, request
from analyzer.email import EmailAnalyzer

email_validation_blueprint = Blueprint('email_validation', __name__)


@email_validation_blueprint.route('/validate_email')
def validate_email():
    email = request.args.get('email')
    print(email)
    
    analyzer = EmailAnalyzer()
    is_valid = analyzer.is_valid(email, first_check=True)
    
    return {
        "email": email,
        "is_valid": is_valid
    }