#!/usr/bin/env python3
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Create a user
user = User(email="user@example.com", password="password")
storage.new(user)
storage.save()

# Create a state
state = State(name="California")
storage.new(state)
storage.save()

# Create a city
city = City(name="San Francisco", state_id=state.id)
storage.new(city)
storage.save()

# Create amenities
amenity1 = Amenity(name="Wi-Fi")
amenity2 = Amenity(name="Pool")
storage.new(amenity1)
storage.new(amenity2)
storage.save()

# Create a place
place = Place(user_id=user.id, city_id=city.id, name="Cool Apartment", number_rooms=2, number_bathrooms=1, max_guest=3, price_by_night=100)
place.amenities.append(amenity1)
place.amenities.append(amenity2)
storage.new(place)
storage.save()

# Create a review
review = Review(place_id=place.id, user_id=user.id, text="Great place to stay!")
storage.new(review)
storage.save()

print("Database has been seeded with sample data!")
