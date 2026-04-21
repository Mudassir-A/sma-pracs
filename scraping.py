# Install required libraries (run once in terminal)
# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL of the website
url = "http://quotes.toscrape.com/"

# Send HTTP request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

print("Extracted Quotes:\n")

# Find all quote elements
quotes = soup.find_all("span", class_="text")

# Loop through and print quotes
for q in quotes:
    print(q.text)