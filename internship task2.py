import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://timesofindia.indiatimes.com/"

# Send a request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and print all headlines and their corresponding links
    for headline in soup.find_all('h2'):
        title = headline.get_text(strip=True)
        link = headline.find('a')['href'] if headline.find('a') else None
        if link and not link.startswith("http"):
            link = url + link  # Handle relative URLs
        print(f"Headline: {title}")
        print(f"Link: {link}\n")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
