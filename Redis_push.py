import requests
import redis
import json

# Google Places API endpoint
endpoint = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# API key
api_key = "AIzaSyA06SgM4Fdob2QiJ_kdoI96JoJjJd57kIE"

# Query parameters
params = {
    "query": "restaurants",  # Example query (you can change this)
    "key": api_key,
}

# Send GET request to Google Places API
response = requests.get(endpoint, params=params)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # Check if there are results
    if "results" in data:
        # Extract first 20 records (if available)
        records = data["results"][:20]
        
        # Connect to Redis
        r = redis.Redis(
            host='redis-11833.c322.us-east-1-2.ec2.cloud.redislabs.com',
            port=11833,
            password='7Mh7XY9gk7ruqfbzNoNaa4Hb2zXJvv6W'
        )

        # Store each record in Redis
        for record in records:
            # Convert record to JSON string
            record_json = json.dumps(record)
            
            # Set record in Redis with a unique key (e.g., using the restaurant name)
            redis_key = f"restaurant:{record['name']}"
            r.set(redis_key, record_json)
            
            print(f"Inserted record for {record['name']} into Redis")
    else:
        print("No results found.")
else:
    print("Error:", response.status_code)
