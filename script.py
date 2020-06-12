import requests

url = "https://community-food2fork.p.rapidapi.com/search"

querystring = {"q":"shredded chicken"}

headers = {
    'x-rapidapi-host': "community-food2fork.p.rapidapi.com",
    'x-rapidapi-key': "00d077979fmsh387d90cf6e84a47p1c658fjsn75203996af2d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)