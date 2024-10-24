import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030/")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

# Function to make GET requests to the backend
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        params = "&".join(f"{key}={value}" for key, value in kwargs.items())
    
    request_url = f"{backend_url}{endpoint}?{params}"
    print(f"GET from {request_url}")

    try:
        response = requests.get(request_url,timeout=30)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None  # Return None or handle as appropriate

# Function to analyze review sentiments
def analyze_review_sentiments(text):
    request_url = f"{sentiment_analyzer_url}/analyze/{text}"
    print(f"Analyzing review sentiment at URL: {request_url}")  # Log the URL
    
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")
        return None



# Function to post a review
def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None