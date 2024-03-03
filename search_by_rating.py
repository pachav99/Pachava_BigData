import redis
import json

# Connect to Redis
r = redis.Redis(
    host='redis-11833.c322.us-east-1-2.ec2.cloud.redislabs.com',
    port=11833,
    password='7Mh7XY9gk7ruqfbzNoNaa4Hb2zXJvv6W'
)

# Initialize lists to store restaurant names and ratings
restaurant_names = []
ratings = []

# Iterate over keys in Redis
for key in r.scan_iter("restaurant:*"):
    # Get JSON data from Redis
    json_data = r.get(key)
    
    # Parse JSON data
    data = json.loads(json_data)
    
    # Extract restaurant name and rating
    restaurant_name = data.get('name')
    rating = data.get('rating', 0)  # If rating is missing, default to 0
    
    # Append data to lists
    restaurant_names.append(restaurant_name)
    ratings.append(rating)

# Search by rating range
min_rating = 4.0
max_rating = 5.0
matching_restaurants = [(name, rating) for name, rating in zip(restaurant_names, ratings) if min_rating <= rating <= max_rating]

# Print matching restaurants within rating range
print("Matching Restaurants within Rating Range:")
for restaurant in matching_restaurants:
    print(restaurant[0], "-", restaurant[1])
