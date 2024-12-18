from webscraper.scraper import scrape_website
from webscraper.parser import get_next_page
from database.create_db import create_database, create_tables, insert_query
from database.manage_db import *
from analysis.data_visualization import plot_sku_count, plot_price_distribution

def main():
    #Step 1: Set up the database
    create_database()
    create_tables()

    SEARCH_ITEM = "Smart Lock"
    page = 20
    # Step 2: Scrape the website and insert data into the database
    search_url = f'https://www.flipkart.com/search?q={SEARCH_ITEM}'

    while page > 0:
        products = scrape_website(search_url)
        for product in products:
            print(product)
            execute_query(insert_query,product)
            
        search_url = get_next_page(search_url)
        if not search_url:
            break
        page -= 1
    # Step 3: Run analysis and generate visualizations
    plot_sku_count()
    plot_price_distribution()

if __name__ == "__main__":
    main()
