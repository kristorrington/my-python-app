import requests
import utils

def fetch_data():
    print("Fetching data from the API...")
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if response.status_code == 200:
        print("Data fetched successfully!")
        return response.json()
    else:
        print("Failed to fetch data.")
        return None

if __name__ == "__main__":
    data = fetch_data()
    print(data)
