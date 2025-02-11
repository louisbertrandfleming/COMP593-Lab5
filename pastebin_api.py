'''pastebin_api.py - Post a dad joke to pastebin.com, return URL
COMP 593 Scripting Applications Winter 2025 Lab 5
Louis Bertrand <louis.bertrand@flemingcollege.ca>

Usage:
Import as a module.

'''

import requests
import credentials

POST_URL = 'https://pastebin.com/api/api_post.php'

def pastebin_post(joke):
    post_params = {
        'api_dev_key': credentials.API_DEV_KEY,
        'api_option': 'paste',
        'api_paste_code': joke, # your paste text, the joke fetched from icanhazdadjoke.com
        'api_paste_private': '0',  # 0=public 1=unlisted 2=private
        'api_paste_name': 'Another Dad Joke', # name or title of your paste
        'api_paste_expire_date': '1M'  # 1M for one month; Expiry uses specific constants
    }
    resp = requests.post(POST_URL, data=post_params)
    if resp.ok:
        return resp.text  # URL of the new paste
    else:
        return ""  # no url

if __name__ == "__main__":
    print("Please import this module.")