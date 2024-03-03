import requests

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
        
        # Print each record
        for record in records:
            print(record)
    else:
        print("No results found.")
else:
    print("Error:", response.status_code)
