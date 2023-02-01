#!/usr/bin/python3
"""
This module counts  all top posts based on keyword searches
for a specific subreddit using reddit's api
"""
import requests


def count_words(subreddit, word_list, after=None, stats={}):
    """
    prints the count for all hot posts recursively
    for a list of word_list
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
        posts = data.get("data").get("children")
        for post in posts:
            title = (post.get("data").get("title"))
            title = title.lower()
            for word in word_list:
                word = word.lower()
                w_count = title.count(word)
                if w_count > 0:
                    stats[word] = stats.get(word, 0) + w_count
        new_after = data.get("data").get("after")
        if new_after is not None:
            count_words(subreddit, word_list, after, stats)
        if after is None:
            sorted_stat = {}
            largest = []
            for k, v in stats.items():
                if sorted_stat.get(v):
                   sorted_stat[v].append(k)
                else:
                    sorted_stat[v] = []
            
            numbers = sorted(list(sorted_stat.keys()),
                             reverse=True)
            for num in numbers:
                entries = sorted_stat[num]
                sorted_entries = sorted(entries)
                for entry in sorted_entries:
                    print("{}: {}".format(entry, num))


    except requests.exceptions.JSONDecodeError:
        return None
