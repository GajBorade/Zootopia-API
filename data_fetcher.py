"""
data_fetcher.py

Fetches animal data from the API. Returns a list of animals
with their details in a consistent dictionary format.

Functions:
- load_data(animal_name): Sends request to API and returns raw response.
- get_animal_data(): Prompts for an animal name and returns its data.

Usage:
    import data_fetcher
    name, data = data_fetcher.get_animal_data()
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")
REQUEST_URL = f"https://api.api-ninjas.com/v1/animals?name="
HEADERS = {"X-Api-Key": API_KEY}


def load_data(animal_name):
    """
    loads the data from the api

    :param animal_name: name of the animal
    :return:list of nested dictionaries representing animal data
    """
    res = requests.get(REQUEST_URL + animal_name, headers=HEADERS)
    if res.status_code != 200:
        print(f"Request failed with status code {res.status_code}")
    else:
        return res.json()
    return []


def fetch_data():
    """
    Prompts the user to enter an animal name and fetches data from the API once.

    This function does not attempt retries or provide a default animal.
    The returned list may be empty if the API does not find the animal.
    :return: list of dictionaries containing animal data
    """
    animal_name = input("Enter animal name: ").strip().lower()
    animals_data = load_data(animal_name)
    return animal_name, animals_data
