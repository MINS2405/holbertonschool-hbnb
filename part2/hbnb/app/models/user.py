from .base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        assert len(first_name) <= 50
        assert len(last_name) <= 50
        # (ajoute ici une validation d'email)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
