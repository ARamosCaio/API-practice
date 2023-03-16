import requests

api_url = "https://jsonplaceholder.typicode.com/todos"

to_do ={
    'userId': 1,
    'title:': "Buy Milk",
    'completed': False
}

response = requests.post(api_url, json=to_do)

print(response.json())
print(response.status_code)