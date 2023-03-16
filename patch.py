import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"

to_do = {"title": "Mow lawn"}
response = requests.patch(api_url, to_do)
print(response.json())
