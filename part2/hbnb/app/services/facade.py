from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.amenity_repo = InMemoryRepository()


    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.list_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None
        amenity.name = amenity_data['name']
        self.amenity_repo.update(amenity)
        return amenity

