import re
from .base_model import BaseModel

def is_valid_email(email):
    # Simple regex for email validation
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        if not first_name or len(first_name) > 50:
            raise ValueError("First name is required and must be at most 50 characters")
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name is required and must be at most 50 characters")
        if not email or not is_valid_email(email):
            raise ValueError("A valid email is required")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
