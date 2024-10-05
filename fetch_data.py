# Setting Up Vultr API for fetching data
import requests

API_KEY = '  our_vultr_api_key'
url = 'https://api.vultr.com/v2/ our_endpoint'
headers = {
    'Authorization': f'Bearer {API_KEY}'
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    air_quality_data = response.json()  # Air quality data
    print("Data fetched successfully:", air_quality_data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
