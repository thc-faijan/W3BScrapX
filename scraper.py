import requests

# Fetch content from a website
url = 'http://quotes.toscrape.com'
response = requests.get(url)

if response.ok:
    print("Content fetched successfully!")
    print(response.text[:500])  # Display the first 500 characters of the webpage content
else:
    print("Failed to fetch content.")