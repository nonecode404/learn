import requests

params = {
    "code": 0,
    "data": {
    "rooms": [
      {
        "begin": "string",
        "encrypted": "true",
        "end": "string",
        "invitation": "string",
        "name": "string",
        "password": "string",
        "roomID": 0,
        "show_name": "string"
      }
    ]
    },
    "message": "string"
}
response = requests.get()