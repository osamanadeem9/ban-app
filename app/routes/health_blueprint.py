from flask import Blueprint

health_blueprint = Blueprint('/', __name__)

@health_blueprint.route('/')
def health():
    return 'OK'