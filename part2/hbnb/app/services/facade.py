from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_users(self):
        return self.user_repo.list_all()

    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        if not user:
            return None
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        self.user_repo.update(user)
        return user
