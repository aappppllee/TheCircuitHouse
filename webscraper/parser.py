from bs4 import BeautifulSoup
from webscraper.utils import fetch_with_retry, extract_numbers
import logging

def parse_product_details(pid,product_url, product_price):
    response = fetch_with_retry(product_url)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
        brand, price, rating, rating_count, review_count = extract_product_details(soup, product_price)
        return pid,brand, price, rating, rating_count, review_count, product_url
    return pid,None, None, None, None, None, product_url

def extract_product_details(soup, product_price):
    try:
        # Attempt to extract brand
        brand_element = soup.find('td', attrs={'class': "Izz52n col col-9-12"}).find("ul").find("li",attrs={'class': ["HPETK2"]})
        brand = brand_element.get_text(strip=True) if brand_element else None

        price_element = soup.find("div", attrs={"class": "UOCQB1"}).find("div", attrs={"class": "hl05eU"}).find("div", attrs={"class": ["Nx9bqj", "CxhGGd"]})
        price = price_element.get_text(strip=True) if price_element else product_price
        price = int(extract_numbers(price))

        # Attempt to extract rating
        rating_element = soup.find("div", attrs={'class': "XQDdHH"})
        rating = float(rating_element.text) if rating_element and rating_element.text else None

        ratings_count = None
        reviews_count = None

        rating_review_count_span = soup.find('span', class_='Wphh3N')

        # Check if the element was found (i.e., it is not None)
        if rating_review_count_span is not None:
            # Proceed to find the inner span
            rating_review_count_span = rating_review_count_span.find("span")

            if rating_review_count_span is not None:
                # Element was found, you can now proceed with extracting text
                span_elements = rating_review_count_span.find_all('span')
                
                # Assuming the span elements exist and have the expected structure
                if len(span_elements) >= 3:
                    rating_count_text = span_elements[0].get_text(strip=True)
                    review_count_text = span_elements[2].get_text(strip=True)

                    # Extract numbers from the text
                    ratings_count = int(extract_numbers(rating_count_text)) if rating_count_text else None
                    reviews_count = int(extract_numbers(review_count_text)) if review_count_text else None

        # Ensure all values are returned, even if they are None
        return brand, price, rating, ratings_count, reviews_count

    except Exception as e:
        logging.error(f"Unexpected error occurred while extracting details: {e}")
        return None, None, None, None, None
    pass

def get_next_page(url):
    response = fetch_with_retry(url)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
    try:
        next_button = soup.find_all('a', class_='_9QVEpD')[-1]  
        if next_button and next_button.find('span').text.strip().lower() == "next":
            return 'https://www.flipkart.com' + next_button.get('href')
    except Exception as e:
        return None
    return None
