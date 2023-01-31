#!/usr/bin/python3
"""
This module fetches the number of subscribers
for a specific subreddit using reddit's api
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of
    subscribers of the particular  subreddit
    """
    headers = {"User-Agent": "alx(api_practice)"}
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    resp = requests.get(url, headers=headers, allow_redirects=False)
    try:
        data = resp.json()
        return int(data.get("data").get("subscribers"))
    except requests.exceptions.JSONDecodeError:
        return 0
