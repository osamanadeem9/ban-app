from flask import Blueprint, request
from analyzer.ip_addr import IPAddressAnalyzer

ip_validation_blueprint = Blueprint('ip_validation', __name__)


@ip_validation_blueprint.route('/validate_ip')
def validate_ip():
    ip = request.args.get('ip')
    print(ip)
    
    analyzer = IPAddressAnalyzer(ip)
    return analyzer.get_ip_details()
    
@ip_validation_blueprint.route('/check_proxy')
def check_proxy():
    ip = request.args.get('ip')
    print(ip)
    
    analyzer = IPAddressAnalyzer(ip)
    return {"proxy": analyzer._is_proxy()}
