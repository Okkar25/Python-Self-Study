import requests

url = "https://www.youtube.com"

response = requests.get(url)
# print(response.text)
# print(response.url)

# The requests module allows you to send HTTP requests using Python.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).


# delete(url, args)     	     Sends a DELETE request to the specified url
# get(url, params, args)	     Sends a GET request to the specified url
# head(url, args)	             Sends a HEAD request to the specified url
# patch(url, data, args)	     Sends a PATCH request to the specified url
# post(url, data, json, args)	 Sends a POST request to the specified url
# put(url, data, args)	         Sends a PUT request to the specified url
# request(method, url, args)	 Sends a request of the specified method to the specified url


import requests
from pprint import pprint

url = "https://fakestoreapi.com/products/1"

# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     pprint(data)
# else:
#     print(f"Error: {response.status_code}")


base_url = "https://pokeapi.co/api/v2"
pokemon_name = "pikachu"
pokemon_name = "charizard"

def get_pokemon_data(name):
    url = f"{base_url}/pokemon/{name}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data : ", {response.status_code})
    

pokemon_info = get_pokemon_data(pokemon_name)

# if pokemon_info:
#     print(f"Name : {pokemon_info["name"].capitalize()}")
#     print(f"Id : {pokemon_info["id"]}")
#     print(f"Height : {pokemon_info["height"]}")
#     print(f"Weight : {pokemon_info["weight"]}")




