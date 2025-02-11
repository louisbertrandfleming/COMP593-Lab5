'''dadjokes_api.py - Request a dad joke from icanhazdadjoke.com
COMP 593 Scripting Applications Winter 2025 Lab 5
Louis Bertrand <louis.bertrand@flemingcollege.ca>

Usage:
Import as a module.

'''

import requests

URL = "https://icanhazdadjoke.com/search"

def fetch_joke(subject):
    get_parameters = {
        "term": subject,
        "limit": "1"
    }
    get_headers = {
        "Accept": "application/json"
    }
    resp = requests.get(URL, headers=get_headers, params=get_parameters)
    if resp.ok:
        jokes = resp.json()["results"]
        return jokes[0]["joke"]
    else:
        return ""

if __name__ == "__main__":
    print("Please import this module.")