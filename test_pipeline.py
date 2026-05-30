import os
import requests
from dotenv import load_dotenv

# 1. Load the custom named environment file
load_dotenv(dotenv_path="atlas_keys.env")
CENSUS_KEY = os.getenv("CENSUS_API_KEY")

print("--- DEBT ATLAS DEBUGGING HANDSHAKE ---")

# 2. Fire a simplified test handshake to a guaranteed base endpoint
url = f"https://api.census.gov/data/2021/acs/acs1?get=NAME&for=state:*&key={CENSUS_KEY}"

response = requests.get(url)

print(f"Server Status Code: {response.status_code}")

try:
    # Try to print clean JSON data
    data = response.json()
    print("\n✅ SUCCESS! Handshake established.")
    print(f"Sample response: {data[1]}")
except Exception:
    # If it fails, print the raw text from the government server
    print("\n❌ SERVER BLOCKED ACCESS. Here is the raw message from the Census Bureau:\n")
    print("-" * 60)
    print(response.text.strip())
    print("-" * 60)