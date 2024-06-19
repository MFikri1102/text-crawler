import requests
from bs4 import BeautifulSoup
import json

def scrape_content(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract the main content
    content_div = soup.find("div", class_="entry-content")
    
    if content_div:
        # Join the text of all paragraphs within the entry-content div
        content = "\n".join([p.get_text(strip=True) for p in content_div.find_all("p")])
        return content
    return ""

# Read the article URLs and titles from the JSON file
with open("articles.json", "r") as f:
    articles = json.load(f)

# Scrape the content for each article
for article in articles:
    article_url = article["url"]
    article_content = scrape_content(article_url)
    article["content"] = article_content

# Save the articles with content to a new JSON file with UTF-8 encoding
with open("articles_with_content.json", "w", encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)
