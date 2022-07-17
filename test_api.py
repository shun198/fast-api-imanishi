import requests
import json


def main():
    url = "http://127.0.0.1:8000/items/"
    body = {
        "name": "white_t_shirt",
        "description": "This is great",
        "price": 4000,
        "tax": 1.1
    }
    response = requests.post(url, json.dumps(body))
    print(response.json())


if __name__ == "__main__":
    main()
