import requests
from bs4 import BeautifulSoup
import json

base_url = "https://www.alodokter.com"
start_url = base_url + "/"

def scrape_articles(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the elements containing the article links
    article_cards = soup.select("div.card-post-index-view")
    
    # Extract the article URLs and titles
    articles = []
    for card in article_cards:
        link_tag = card.find("a", href=True)
        if link_tag:
            article_url = base_url + link_tag["href"]
            title_tag = card.find("h4")
            article_title = title_tag.text.strip() if title_tag else "No title"
            articles.append({"url": article_url, "title": article_title})

    # Find the "Next" link (Assuming there is a pagination system similar to the previous example)
    next_link = soup.select_one("span.next > a")

    return articles, next_link

# Start scraping from the first page
articles = []
current_url = start_url
next_link = None

while current_url:
    page_articles, next_link = scrape_articles(current_url)
    articles.extend(page_articles)

    if next_link:
        current_url = base_url + next_link.get("href")
    else:
        current_url = None

# Save the article URLs and titles to a JSON file
with open("articles_alodokter.json", "w", encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)
