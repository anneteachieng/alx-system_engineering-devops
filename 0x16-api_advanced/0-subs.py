#!/usr/bin/python3
"""
This module is for getting the number of subscribers of a certain subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ function to get subscriber count"""
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
                "user-agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0
        results = response.json().get("data")
        return results.get("subscribers")
