from flask import Flask

app = Flask(__name__)

from routes.health_blueprint import health_blueprint
from routes.email_validatation_blueprint import email_validation_blueprint
from routes.ip_validation_blueprint import ip_validation_blueprint

app.register_blueprint(health_blueprint)
app.register_blueprint(email_validation_blueprint)
app.register_blueprint(ip_validation_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    # app.run(debug=True)
