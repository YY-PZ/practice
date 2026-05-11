import requests
from bs4 import BeautifulSoup
import json

def scrape_quotes(url):
    print(f"Відправляємо запит до {url}...")
    response = requests.get(url)

    response.raise_for_status() 

    soup = BeautifulSoup(response.text, 'lxml')

    quotes_data = []
    quotes_blocks = soup.find_all('div', class_='quote')

    for block in quotes_blocks:
        text = block.find('span', class_='text').get_text(strip=True)

        author = block.find('small', class_='author').get_text(strip=True)

        author_link = block.find('a')['href']
        full_author_url = f"http://quotes.toscrape.com{author_link}"

        tags_container = block.find('div', class_='tags')
        tags = []
        if tags_container:
            tag_elements = tags_container.find_all('a', class_='tag')
            tags = [tag.get_text(strip=True) for tag in tag_elements]

        quotes_data.append({
            'quote': text,
            'author': author,
            'author_url': full_author_url,
            'tags': tags
        })

    return quotes_data

if __name__ == '__main__':
    target_url = 'http://quotes.toscrape.com/'

    scraped_data = scrape_quotes(target_url)

    print("\nРезультат Парсингу")
    print(json.dumps(scraped_data, indent=4, ensure_ascii=False))
    print(f"\nУспішно зібрано {len(scraped_data)} цитат.")
