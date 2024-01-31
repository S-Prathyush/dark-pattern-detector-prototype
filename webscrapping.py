# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://mailmeteor.com/spam-checker'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find and extract text content from specific HTML elements
    # For example, if you want to extract text from all paragraphs ('p' tags) on the webpage:
    paragraphs = soup.find_all('div')
    
    # Print the text extracted from paragraphs
    for paragraph in paragraphs:
        print(paragraph.text)
else:
    print('Failed to retrieve webpage')
