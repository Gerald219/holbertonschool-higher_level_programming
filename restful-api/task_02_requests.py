#!/usr/bin/env python3
"""fetch posts and print/save."""


import requests
import csv

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts() -> bool:
    """ Get posts, show the HTTP status and every title.
    Returns True when it works, False when it fails.
    """

    try:
        resp = requests.get(BASE_URL, timeout=10)
        print(f"Status Code: {resp.status_code}")
        
        if not (200 <= getattr(resp, "status_code", 0) < 300):
            return False


        for post in resp.json():
            print(post.get("title"))
        return True
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return False

def fetch_and_save_posts(filename: str = "posts.csv") -> bool:
    """
    GET posts and save id/title/body to a CSV called posts.cs    v .
    Returns True on success, False otherwise.
    """
    try:
        resp = requests.get(BASE_URL, timeout=10)
        if not (200 <= getattr(resp, "status_code", 0) < 300):
            return False

        posts = resp.json()
        rows = [
            {"id": p.get("id"), "title": p.get("title"), "body": p.get("body")}
            for p in posts
        ]

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
        return True
    except (requests.RequestException, OSError) as e:
        print(f"Error: {e}")
        return False


