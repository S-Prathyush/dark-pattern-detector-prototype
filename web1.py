# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://supersimple.dev/exercises/youtube'

# List of spam words
spam_words = ['spam', 'unwanted', 'advertisement','100% more','100% free','additional income','be your own boss','best','price','free',' gifts','promises','cash','pure','save','click','become','winner']  # Add more spam words as needed

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find and extract text content from paragraphs and headers (h1 to h6)
    text_elements = soup.find_all(['div','button','p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    # Check for spam words in text elements
    found_spam = False
    for element in text_elements:
        element_text = element.text.lower()  # Convert text to lowercase for case-insensitive matching
        for spam_word in spam_words:
            if spam_word in element_text:
                found_spam = True
                break  # Exit inner loop if any spam word is found
        if found_spam:
            break  # Exit outer loop if any spam word is found
    
    # Print "Spam" if any spam word is found
    if found_spam:
        print("Dark pattern detected")
    else:
        print("No dark pattern detected")
else:
    print('Failed to retrieve webpage')
