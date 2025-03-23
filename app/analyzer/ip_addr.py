import requests
import ipaddress

class IPAddressAnalyzer:
    def __init__(self, ip_addr: str):
        self.ip_addr = ip_addr
        self.endpoint = "http://ip-api.com/json/{ip_addr}?fields=query,proxy,status,message"

    def _validate_ip(self) -> bool:
        """Validate the IP address format."""
        try:
            ipaddress.ip_address(self.ip_addr)
            return True
        except ValueError:
            return False

    def _is_proxy(self) -> bool:
        """Determine if the IP address is a proxy."""
        response = requests.get(self.endpoint.format(ip_addr=self.ip_addr))
        data = response.json()
        return data.get("status") == "success" and data.get("proxy", False)

    def get_ip_details(self) -> dict:
        """Return a dictionary with the IP validation and proxy status."""
        is_valid = self._validate_ip()
        is_proxy = self._is_proxy() if is_valid else False
        status = "success" if is_valid and not is_proxy else "fail"
        
        return {
            "ip": self.ip_addr,
            "is_valid": is_valid,
            "is_proxy": is_proxy,
            "status": status
        }

