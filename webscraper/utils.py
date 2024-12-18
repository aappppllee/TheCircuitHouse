import requests
import logging
import time
import re
from config.config import HEADERS

def fetch_with_retry(url, retries=10, backoff_factor=2):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url=url, headers=HEADERS)
            if response.status_code == 200:
                return response
            else:
                logging.warning(f"Unexpected status code {response.status_code}. Retrying...")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}. Retrying...")
        
        attempt += 1
        sleep_time = backoff_factor ** attempt
        logging.info(f"Retrying in {sleep_time} seconds...")
        time.sleep(sleep_time)
    
    logging.error("Failed to fetch the URL after multiple attempts.")
    return None


def extract_numbers(text):
    # Use regular expression to find all digits in the text
    numbers = re.findall(r'\d+', text)
    # Join the list of numbers into a single string (if needed)
    result = ''.join(numbers)
    return result