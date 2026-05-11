import pytest
from bs4_script import scrape_quotes
from selenium_script import scrape_dynamic_content


def test_scrape_quotes(requests_mock):
    mock_html = """
    <html>
        <body>
            <div class="quote">
                <span class="text">"Тестова цитата"</span>
                <span>by <small class="author">Тестовий Автор</small>
                <a href="/author/Test-Author">(about)</a>
                </span>
                <div class="tags">
                    <a class="tag" href="/tag/test1/page/1/">test1</a>
                    <a class="tag" href="/tag/test2/page/1/">test2</a>
                </div>
            </div>
        </body>
    </html>
    """
    
    test_url = 'http://fake-url.com'
    requests_mock.get(test_url, text=mock_html, status_code=200)
    
    result = scrape_quotes(test_url)
    
    assert len(result) == 1, "Парсер мав знайти рівно одну цитату"
    assert result[0]['quote'] == '"Тестова цитата"'
    assert result[0]['author'] == 'Тестовий Автор'
    assert result[0]['author_url'] == 'http://quotes.toscrape.com/author/Test-Author'
    assert result[0]['tags'] == ['test1', 'test2']



def test_selenium_dynamic_content():    
    result = scrape_dynamic_content()
    
    assert result == "Hello World!", f"Очікували 'Hello World!', а отримали '{result}'"