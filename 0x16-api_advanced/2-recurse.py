#!/usr/bin/python3
"""
This module fetches the all top posts
for a specific subreddit using reddit's api
"""
import json
import requests


def recurse(subreddit, after=None):
    """
    Returns the all hot posts recursively
    of the particular  subreddit
    """
    headers = {"User-Agent": "alx/com.reddit"}
    if after is not None:
        url = "https://api.reddit.com/r/{}/hot?after={}".format(
              subreddit, after)
    else:
        url = "https://api.reddit.com/r/{}/hot".format(
              subreddit)
    resp = requests.get(url, headers=headers, allow_redirects=False)
    try:
        data = resp.json()
        if data.get('error'):
            return None
        posts = data.get("data").get("children")
        hot_list = []
        for post in posts:
            hot_list.append((post.get("data").get("title")))
        new_after = data.get("data").get("after")
        if new_after is not None:
            more_posts = recurse(subreddit, new_after)
            hot_list += more_posts
        return hot_list

    except json.decoder.JSONDecodeError:
        return None
