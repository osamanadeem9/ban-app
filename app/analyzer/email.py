from pyisemail import is_email
import re

class EmailAnalyzer:
    def __init__(self):
        with open('app/lists/disposable_email_blocklist.conf') as f:
            self.disposable_domains = set(line.strip() for line in f)

    def is_valid(self, email, first_check=False):
        return (self._validate_format(email) and 
                self._validate_dns(email, check_dns=first_check) and 
                not self._is_disposable(email))

    def _validate_format(self, email):
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

    def _validate_dns(self, email, check_dns):
        return is_email(email, check_dns=check_dns)

    def _is_disposable(self, email):
        domain = email.split('@')[-1]
        return domain in self.disposable_domains

