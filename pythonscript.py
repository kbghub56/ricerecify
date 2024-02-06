import requests

def get_place_details(api_key, place_id):
    base_url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "key": api_key,
    }

    response = requests.get(base_url, params=params)
    place_details = response.json()

    return place_details

# Replace 'YOUR_API_KEY' with your actual API key
api_key = "YOUR_API_KEY"

# Replace 'YOUR_PLACE_ID' with the place ID of the Rice Recreation Center or any other place
place_id = "YOUR_PLACE_ID"

# Get place details including popular times
place_details = get_place_details(api_key, place_id)

# Extract and print popular times information
if 'result' in place_details:
    result = place_details['result']
    if 'populartimes' in result:
        popular_times = result['populartimes']
        print("Popular Times:")
        for day in popular_times:
            print(f"{day['name']}: {day['data']}")
    else:
        print("No popular times information available.")
else:
    print("Error fetching place details.")
