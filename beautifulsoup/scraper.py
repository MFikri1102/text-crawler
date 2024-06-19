from bs4 import BeautifulSoup
import requests

def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Get the title of the page
        page_title = soup.title.string
        print(f"Page Title: {page_title}")

        # Get all text from paragraphs
        paragraphs = soup.find_all('p')
        for idx, para in enumerate(paragraphs):
            print(f"Paragraph {idx+1}: {para.get_text()}")

        # Get all article links
        article_list = soup.find('ul', {'class': 'alomedika-recent'})
        if article_list:
            article_links = article_list.find_all('a', {'class': 'recent-link'})
            for link in article_links:
                article_url = link.get('href')
                print(f"Article URL: {article_url}")
                scrape_page(article_url)

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Start scraping from the main Alomedika page
scrape_page('https://www.alomedika.com')