Here’s a revised version with improved clarity and grammar: The code provided below is intended solely for educational purposes, specifically to assist in learning web scraping or research techniques. It is not intended for commercial use or profit. You can find the source code here:
[Learn Python: Web Scraping Reddit Posts](https://learnpython.com/blog/python-webscraping-reddit-posts/)

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the subreddit page
url = 'https://www.reddit.com/r/Python/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully accessed the subreddit.")
else:
    print(f"Failed to access subreddit. Status code: {response.status_code}")

# Parse the HTML data (optional, not used in final output)
html_data = BeautifulSoup(response.text, 'html.parser')
h1_headings = html_data.find_all('h1')

# Print the first h1 heading if available
if h1_headings:
    print(h1_headings[0].text.strip())

# Fetch subreddit posts in JSON format
base_url = 'https://www.reddit.com'
subreddit = '/r/python'
sort_by = '/hot'
url = base_url + subreddit + sort_by + '.json'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})  # Set a user agent

# Check if the request was successful
if response.status_code == 200:
    json_data = response.json()
    print("Successfully fetched posts.")
else:
    print(f"Failed to fetch posts. Status code: {response.status_code}")

# Extract post data
posts = [post['data'] for post in json_data['data']['children']]

# Create a DataFrame and save to Excel
df = pd.DataFrame(posts)
df.to_excel('r-python_posts.xlsx', index=False)  # Save without row indices

print("Data saved to r-python_posts.xlsx")




## Example: Search for 'tofu'
pip install openpyxl # Required for conversion to xslx 
pip install --upgrade pip # if necessary

# Necessary python libraries
import requests
import pandas as pd

# Define and fetch the Reddit search results for "tofu"
search_query = 'tofu'
url = f'https://www.reddit.com/search.json?q={search_query}'

# Fetch the search results from the constructed URL
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})  # Set a user agent

## To fetch from a specific Subreddit search
"""
subreddit = 'ENTER_THE_SUBREDDIT'  # Replace with the desired subreddit
search_query = 'ENTER_QUERY'
url = f'https://www.reddit.com/r/{subreddit}/search.json?q={search_query}&restrict_sr=1'
"""
# Check if the request was successful
if response.status_code == 200:
    json_data = response.json() # Parse the response as JSON
    print("Successfully fetched search results.") 
else:
    print(f"Failed to fetch search results. Status code: {response.status_code}")

# Extract post data from JSON
posts = [post['data'] for post in json_data['data']['children']] # Create a list of post data dictionaries

# Create a new  'pandas' DataFrame and save to Excel
df = pd.DataFrame(posts)
df.to_excel('tofu_reddit_posts.xlsx', index=False)  # Save without row indices

print("Data saved to tofu_reddit_posts.xlsx")
