import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()

to_do = {
    "userID": 1,
    "title": 'Wash Car',
    "completed": True
}
response = requests.put(api_url, json=to_do)
print(response.json())
print(response.status_code)