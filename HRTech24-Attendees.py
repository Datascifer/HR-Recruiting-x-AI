# Below is a 'webscraping' function that I've created to help gather data from the 2024 HR tech conference.

# Install important libraries to find, process, and convert data top CSV file
import numpy as np # provides faster computation by using clean synthax
import pandas as pd # helps with data manipulation
import requests # include headers in a GET request
from bs4 import BeautifulSoup # parse the raw text
import csv # for generating CSV files

# Function to fetch and parse exhibitor data from one page
def get_exhibitors_from_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)  # Adding user-agent header
    soup = BeautifulSoup(response.content, 'html.parser')
    
    exhibitors = []
    for exhibitor in soup.find_all('h5', class_='generic-option'):
        name = exhibitor.text.strip()
        booth = exhibitor.find_next('a').text.strip()
        exhibitors.append({'Name': name, 'Booth': booth})
    
    return exhibitors


# Start with the first page URL with max page limit
base_url = 'https://hrtech2024.smallworldlabs.com/exhibitors?page='
page = 1
all_exhibitors = []

max_pages = 10  # Set a reasonable limit
while page <= max_pages:
    url = base_url + str(page)
    exhibitors = get_exhibitors_from_page(url)
    
    if not exhibitors:
        print(f'No exhibitors found on page {page}. Stopping the loop.')
        break
    
    all_exhibitors.extend(exhibitors)
    page += 1


# Write all exhibitors data to CSV
with open('exhibitors.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Booth'])
    writer.writeheader()
    for exhibitor in all_exhibitors:
        writer.writerow(exhibitor)

print(f'CSV file has been created with {len(all_exhibitors)} exhibitors.')
