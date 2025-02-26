#!/usr/bin/python3
"""Recursive function to query the Reddit API and return all hot article titles."""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): The list to store the titles of hot articles. Defaults to None.
        after (str, optional): The 'after' parameter for pagination. Defaults to None.

    Returns:
        list: A list of all hot article titles for the given subreddit.
        None: If the subreddit is invalid.
    """
    # Initialize the hot_list if it's None
    if hot_list is None:
        hot_list = []

    # Define the URL for the Reddit API endpoint
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "custom-script:v1.0 (by /u/InteractionBitter899)"
    }

    # Define parameters for pagination
    params = {"limit": 100}  # Fetch up to 100 posts per request
    if after:
        params["after"] = after

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if the response status code indicates a valid subreddit
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the list of posts from the 'data.children' field
            posts = data.get("data", {}).get("children", [])

            # Add the titles of the current page's posts to the hot_list
            for post in posts:
                title = post.get("data", {}).get("title")
                if title:
                    hot_list.append(title)

            # Check if there are more pages to fetch
            after_value = data.get("data", {}).get("after")
            if after_value:
                # Recursively call the function with the 'after' parameter
                return recurse(subreddit, hot_list, after=after_value)
            else:
                # No more pages, return the completed hot_list
                return hot_list
        elif response.status_code == 404:
            # If the subreddit is invalid, return None
            return None
        else:
            # For any other status code, return None as a fallback
            return None

    except requests.RequestException:
        # Handle any request-related exceptions (e.g., network issues)
        return None
