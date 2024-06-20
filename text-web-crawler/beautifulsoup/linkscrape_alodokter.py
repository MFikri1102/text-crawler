import requests
from bs4 import BeautifulSoup
import json

base_url = "https://www.alodokter.com"
start_url = base_url + "/page/"

def scrape_articles(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the elements containing the article links
    article_cards = soup.find_all("card-post-index")
    
    # Extract the article URLs and titles
    articles = []
    for card in article_cards:
        article_url = base_url + card.get("url-path")
        article_title = card.get("title")
        articles.append({"url": article_url, "title": article_title})

    return articles

# Start scraping from the first page
articles = []
page_number = 1

while True:
    current_url = start_url + str(page_number)
    page_articles = scrape_articles(current_url)
    
    # If no articles are found, break the loop
    if not page_articles:
        break
    
    articles.extend(page_articles)
    page_number += 1

# Save the article URLs and titles to a JSON file
with open("articles_alodokter.json", "w", encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)
