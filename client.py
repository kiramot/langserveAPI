import requests

response = requests.post("http://localhost:8000/essay/invoke",
                         json={'input': {'topic': "my best friend"}})

try:
    json_response = response.json()
    print(json_response)
except ValueError as e:
    print("Error decoding JSON:", e)
