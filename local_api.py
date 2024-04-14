import json

import requests

#Send a GET using the URL http://127.0.0.1:8000
u = 'http://127.0.0.1:8000'
r = requests.get(url = u)

# Print Status Code
print("Status Code:", r.status_code)

# Prints Message
msg = list(r.json().values())
print('Welcome to the next level of AI-Devops! McPolygon:', msg[0])


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

#Send a POST using the data above
r = requests.post(url = 'http://127.0.0.1:8000/data/', data = json.dumps(data))

#Print the status code
print("Status Code:", r.status_code)

#Print the results
msg = list(r.json().values())
print("Results:", msg[0])