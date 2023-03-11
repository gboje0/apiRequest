import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
response.raise_for_status()
print(response.json())
data = response.json()
iss_location = data["iss_position"]
print(iss_location)
iss_lat = iss_location["latitude"]
iss_log = iss_location["longitude"]
iss_position = (iss_log, iss_lat)
print(iss_position)
