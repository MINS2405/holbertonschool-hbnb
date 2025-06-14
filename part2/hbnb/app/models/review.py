from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        assert 1 <= rating <= 5
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
