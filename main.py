import requests

def upload_property_to_ota(api_key, property_name, description, amenities, location, images):
    """
    Function to upload lodging details to a website like sunlightbreeze.com.
    """
    # Replace with the OTA's actual API endpoint
    api_url = "https://sunlightbreeze.com/"  # Ensure this is the correct API endpoint
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "name": property_name,
        "description": description,
        "amenities": amenities,
        "location": location,
        "images": images
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        
        # Check the status code and print relevant information for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        
        if response.status_code == 201:
            print(f"Property '{property_name}' successfully uploaded!")
            return response.json()  # If successful, return the response data
        else:
            print(f"Failed to upload property. Status Code: {response.status_code}")
            # Printing the response text to help debug
            print("Response:", response.text)
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    API_KEY = "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"  # Replace with your actual API key

    # Property details
    property_name = "Luxury Villa Sunlightbreeze"
    description = """
    Discover the charm of Luxury Villa Sunlightbreeze, a modern and luxurious accommodation in the heart of Crete.
    Ideal for families, couples, or small groups seeking an unforgettable Mediterranean escape.
    """
    amenities = [
        "Free Wi-Fi",
        "Air-conditioning",
        "Fully equipped kitchen",
        "Flat-screen TV",
        "Spacious bedroom with built-in wardrobe"
    ]
    location = {
        "address": "Crete, Greece",
        "latitude": 35.2401,
        "longitude": 24.8093
    }
    images = [
        {"url": "https://sunlightbreeze.com/images/Luxury%20villa%20Sunlightbreeze%20main%20entrance.jpg", "caption": "Luxury Villa Chania is Valuable Reservation"},
        {"url": "https://sunlightbreeze.com/images/Luxury%20villa%20Sunlightbreeze%20patio%20swimming%20pool.jpg", "caption": "Luxury Villa Chania Crete Accommodation"}
    ]

    upload_property_to_ota(API_KEY, property_name, description, amenities, location, images)