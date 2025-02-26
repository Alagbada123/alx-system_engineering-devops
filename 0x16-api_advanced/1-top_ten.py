#!/usr/bin/python3
"""Function to query the Reddit API and print the titles of the first 10 hot posts."""
import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: If the subreddit is invalid.
    """
    # Define the URL for the Reddit API endpoint
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "custom-script:v1.0 (by /u/InteractionBitter899)"
    }
    
    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code indicates a valid subreddit
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the list of posts from the 'data.children' field
            posts = data.get("data", {}).get("children", [])
            
            # Print the titles of the first 10 hot posts
            for i, post in enumerate(posts[:10], start=1):
                title = post.get("data", {}).get("title", "No Title")
                print(f"{i}. {title}")
        elif response.status_code == 404:
            # If the subreddit is invalid, print None
            print(None)
        else:
            # For any other status code, print None as a fallback
            print(None)
    
    except requests.RequestException:
        # Handle any request-related exceptions 
        print(None)
