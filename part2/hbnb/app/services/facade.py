from app.models.place import Place
from app.models.user import User
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.place_repo = InMemoryRepository()
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_place(self, data):
        # Validation
        if data['price'] < 0:
            raise ValueError("Price must be positive")
        if not (-90 <= data['latitude'] <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if not (-180 <= data['longitude'] <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        # Check if owner exists
        owner = self.user_repo.get(data['owner_id'])
        if not owner:
            raise ValueError("Owner not found")
        # Check amenities
        amenities = []
        for amenity_id in data['amenities']:
            amenity = self.amenity_repo.get(amenity_id)
            if amenity:
                amenities.append(amenity)
        # Create the place
        place = Place(
            title=data['title'],
            description=data.get('description', ''),
            price=data['price'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            owner_id=data['owner_id'],
            amenities=amenities
        )
        self.place_repo.add(place)
        return place

    def get_all_places(self):
        return self.place_repo.list_all()

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def update_place(self, place_id, data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        # Update fields
        if 'title' in data:
            place.title = data['title']
        if 'description' in data:
            place.description = data['description']
        if 'price' in data:
            if data['price'] < 0:
                raise ValueError("Price must be positive")
            place.price = data['price']
        if 'latitude' in data:
            if not (-90 <= data['latitude'] <= 90):
                raise ValueError("Latitude must be between -90 and 90")
            place.latitude = data['latitude']
        if 'longitude' in data:
            if not (-180 <= data['longitude'] <= 180):
                raise ValueError("Longitude must be between -180 and 180")
            place.longitude = data['longitude']
        self.place_repo.update(place)
        return place
