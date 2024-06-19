import requests
from bs4 import BeautifulSoup

base_url = "https://www.alomedika.com"
start_url = base_url + "/"

def scrape_articles(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the elements containing the article links
    article_links = soup.select("ul.alomedika-recent > li > div.text > a.recent-link")

    # Extract the article URLs and titles
    articles = []
    for link in article_links:
        article_url = base_url + link.get("href")
        article_title = link.text.strip()
        articles.append({"url": article_url, "title": article_title})

    # Find the "Next" link
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

# Print the article URLs and titles
for article in articles:
    print("URL:", article["url"])
    print("Title:", article["title"])
    print()