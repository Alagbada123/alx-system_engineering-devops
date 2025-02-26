#!/usr/bin/python3
"""Recursive function to query the Reddit API and
count occurrences of keywords in hot article titles."""
import requests


def count_words(subreddit, word_list, results=None, after=None):
    """
    Recursively queries the Reddit API,
    counts occurrences of keywords in hot article titles,
    and prints the results.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count in the titles.
        results (dict, optional): A dictionary
        to store keyword counts. Defaults to None.
        after (str, optional): The 'after'
        parameter for pagination. Defaults to None.

    Returns:
        None: This function does not return anything;
        it prints the results directly.
    """
    # Initialize the results dictionary if it's None
    if results is None:
        results = {}

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
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        # Check if the response status code indicates a valid subreddit
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the list of posts from the 'data.children' field
            posts = data.get("data", {}).get("children", [])

            # Process each post's title
            for post in posts:
                title = post.get("data", {}).get("title", "").lower()
                words = title.split()  # Split the title into words

                # Count occurrences of keywords in the title
                for word in word_list:
                    normalized_word = word.lower()
                    if normalized_word in results:
                        results[normalized_word] += words.count
                        (normalized_word)
                    else:
                        results[normalized_word] = words.count(normalized_word)

            # Check if there are more pages to fetch
            after_value = data.get("data", {}).get("after")
            if after_value:
                # Recursively call the function with the 'after' parameter
                count_words(subreddit, word_list, results, after=after_value)
            else:
                # No more pages, process and print the results
                print_results(results, word_list)
        elif response.status_code == 404:
            # If the subreddit is invalid, do nothing
            return
        else:
            # For any other status code, do nothing
            return

    except requests.RequestException:
        # Handle any request-related exceptions (e.g., network issues)
        return


def print_results(results, word_list):
    """
    Prints the sorted count of keywords based on the results dictionary.

    Args:
        results (dict): A dictionary containing keyword counts.
        word_list (list): The original list of keywords.

    Returns:
        None
    """
    # Filter out keywords with zero count
    filtered_results = {word.lower():results.get(word.lower(), 0)
                        for word in word_list if results.get(word.lower(), 0) > 0}

    # Sort the results by count (descending)
    # and then alphabetically (ascending)
    sorted_results = sorted(filtered_results.items(),
                            key=lambda x: (-x[1], x[0]))

    # Print the results
    for word, count in sorted_results:
        print(f"{word}: {count}")
