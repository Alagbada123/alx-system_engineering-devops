#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers.
"""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "custom-script:v1.0 (by /u/InteractionBitter899)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    try:
        data = response.json()
        return data["data"]["subscribers"]
    except (KeyError, ValueError):
        return 0
