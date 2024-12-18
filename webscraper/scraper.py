import requests
from bs4 import BeautifulSoup
from webscraper.utils import fetch_with_retry
from webscraper.parser import parse_product_details
from urllib.parse import urlparse, parse_qs

def scrape_website(search_url):
    response = fetch_with_retry(search_url)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = get_all_products(soup)
        return products
    return []

def extract_pid(url):
    # Parse the URL
    parsed_url = urlparse(url)
    # Extract the query parameters
    query_params = parse_qs(parsed_url.query)
    # Get the 'pid' parameter
    pid = query_params.get('pid', [None])[0]
    
    return pid


def get_all_products(soup):
    all_products = soup.find_all('div', attrs={'class': 'slAVV4'})
    print(len(all_products))
    products = []
    for product in all_products:
        product_url = 'https://www.flipkart.com' + product.find('a', attrs={'class': 'wjcEIp'}).get("href")
        product_price = product.find('div', attrs={'class': 'Nx9bqj'}).get_text(strip=True) if product.find('div', attrs={'class': 'Nx9bqj'}) else None
        pid = extract_pid(product_url)
        print(pid)
        product_details = parse_product_details(pid, product_url, product_price)
        products.append(product_details)
    return products
