import uuid
from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner, amenities=None, id=None):
        super().__init__()
        assert len(title) <= 100, "Title must be 100 characters or less"
        assert price > 0, "Price must be positive"
        assert -90.0 <= latitude <= 90.0, "Latitude must be between -90 and 90"
        assert -180.0 <= longitude <= 180.0, "Longitude must be between -180 and 180"
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  # Should be a User object
        self.amenities = amenities if amenities is not None else []  # List of Amenity objects
        self.reviews = []  # List of Review objects (if needed later)

    def add_review(self, review):
        """Add a review to this place"""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to this place"""
        self.amenities.append(amenity)

    def to_dict(self):
        """Return main data for POST response"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner.id if self.owner else None
        }

    def to_summary_dict(self):
        """Return summary data for GET /places/ (list)"""
        return {
            "id": self.id,
            "title": self.title,
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    def to_detail_dict(self):
        """Return detailed data for GET /places/<place_id>"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": self.get_owner_dict(),
            "amenities": [a.to_dict() for a in self.amenities]
        }

    def get_owner_dict(self):
        """Return the owner's details (adapt if needed)"""
        if not self.owner:
            return None
        return {
            "id": self.owner.id,
            "first_name": self.owner.first_name,
            "last_name": self.owner.last_name,
            "email": self.owner.email
        }
