#!/usr/bin/python3
"""
This module fetches the top posts
for a specific subreddit using reddit's api
"""
import requests


def top_ten(subreddit):
    """
    Returns the first ten hot posts
    of the particular  subreddit
    """
    headers = {"User-Agent": "alx(api_practice)"}
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    resp = requests.get(url, headers=headers, allow_redirects=False)
    try:
        data = resp.json()
        posts = data.get("data").get("children")
        for index, post in enumerate(posts):
            if index >= 10:
                break
            print(post.get("data").get("title"))
    except requests.exceptions.JSONDecodeError:
        print(None)
