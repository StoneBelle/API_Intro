import pip._vendor.requests as requests

# Insert API Endpoint as string in url argument 
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) # Returns a response code 
print(response.status_code) # Returns just the status code

response.raise_for_status()

# 	Response code meanings:
# 		○ 1XX: Hold On, loading/this is not final
# 		○ 2XX: Successful
# 		○ 3XX: You don’t have permission
# 		○ 4XX: You screwed up or doesn’t exist 
# 		○ 5XX: Server screwed up/server/site is down

# Tap into API data
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_pos = (longitude, latitude)
# data = response.json()['iss_position']['latitude']
print(data)
print(f"{longitude}")
print(f"{latitude}")
print(iss_pos)
