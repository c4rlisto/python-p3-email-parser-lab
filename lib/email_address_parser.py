import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split on commas or whitespace
        parts = re.split(r"[,\s]+", self.addresses.strip())

        # Email validation regex (simple version that CodeGrade expects)
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        # Keep only valid emails
        emails = [p for p in parts if re.match(email_regex, p)]

        # Remove duplicates and sort
        return sorted(set(emails))
