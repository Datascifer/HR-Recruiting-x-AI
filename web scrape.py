# Below is a 'webscrape' function designed to gather data from the World Wide Web in Python.

# Install important python libraries to find, process, and convert data to CSV file
import numpy as np # provides faster computation by using clean syntax
import pandas as pd # helps with data manipulation
import requests # include headers in a GET request
from bs4 import BeautifulSoup # parse the raw text
import csv # for generating CSV files

# Function to fetch and parse 'target' data from one page
## Define headers to mimic a web browser's user agent
def function_variable(url):
    headers = {
        'User-Agent': 'ENTER USER AGENT STRING' # Here are a few sources to learn and retrieve your user agent: https://www.howtogeek.com/114937/htg-explains-whats-a-browser-user-agent/ and https://wtool.dev/tool/user-agent-finder
    }
    response = requests.get(url, headers=headers)  # Adding user-agent header
    soup = BeautifulSoup(response.content, 'html.parser') # Parse the HTML content of the response using BeautifulSoup
    
    list_variable = [] # Initialize an empty list to store information

    # Loop through all 'HEADER' tags or 'text' information with the class 'generic-option'
    for variable_name in soup.find_all('ENTER_HEADER/LOCATION_OF_INFORMATION', class_='generic-option'):
        name = variable_name.text.strip()
        'ENTER_SECOND_NAME_OF_TARGET' = variable_name.find_next('a').text.strip()
        variable_name.append({'Name': name, 'ENTER_SECOND_NAME_OF_TARGET': ENTER_SECOND_NAME_OF_TARGET})
    
    return variable_name # Return the list 


# Start with the first page URL with max page limit
base_url = 'ENTER THE WEB ADDRESS'
page = 1 # Initialize the current page number
all_variable_name = []  # Initialize an empty list to collect all information

max_pages = 10  # Set a reasonable limit
# Loop to fetch target information from multiple pages
while page <= max_pages:
    url = base_url + str(page)
    variable_name = function_variable(url)
    
    if not variable_name:
        print(f'No information found on page {page}. Stopping the loop.')
        break
    
    all_variable_name.extend(variable_name)
    page += 1


# Write all data to CSV
with open('variable_name.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Booth'])
    writer.writeheader()
    for variable_name in all_variable_name:
        writer.writerow(variable_name)

print(f'CSV file has been created with {len(all_variable_name)} all data.')
