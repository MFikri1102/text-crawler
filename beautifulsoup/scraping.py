import requests
from bs4 import BeautifulSoup
import json

base_url = "https://www.alomedika.com"
start_url = base_url + "/"

def scrape_articles(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the elements containing the article links and content
    article_elements = soup.select("ul.alomedika-recent > li")

    articles = []
    for article_element in article_elements:
        link = article_element.select_one("div.text > a.recent-link")
        if link:
            article_url = base_url + link.get("href")
            article_title = link.text.strip()
            article_content = article_element.select_one("div.text > a.recent-link > p").text.strip()

            articles.append({
                "url": article_url,
                "title": article_title,
                "content": article_content
            })

    # Find the "Next" link
    next_link = soup.select_one("span.next > a")

    return articles, next_link

# Start scraping from the first page
all_articles = []
current_url = start_url
next_link = None

while current_url:
    page_articles, next_link = scrape_articles(current_url)
    all_articles.extend(page_articles)

    if next_link:
        current_url = base_url + next_link.get("href")
    else:
        current_url = None

# Save the articles to a JSON file
with open("articles.json", "w", encoding="utf-8") as json_file:
    json.dump(all_articles, json_file, ensure_ascii=False, indent=4)