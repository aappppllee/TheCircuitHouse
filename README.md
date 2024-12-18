# Data scraping/cleaning
Evaluating a potential entry in the Smart lock market. Since this is a fairly new
category there are very few estimates present in terms of market size and key players. One way
to estimate the key players is by looking at major brands on online portals. The task assigned to
is to scrape online portals (Flipkart or Amazon, you can choose any one portal) and create a
database of key products. Below are the fields required in the database.

Brand name     - String
Price          - Integer
Rating         - Float
Rating count   - Integer
Review count   - Integer
Ranking(where does the product appear in
the search)    -Integer
URL            -String

Based on your collected data analyze the below
a. Number of brands in the segment
b. Count of SKUs per brand
c. Relative ranking: Create a formula to rank brands based on the rank of the SKUs in the
   search results. E.g.: Brand A has 4 SKUs in the search results and Brand B has 6 SKUs in
   the search results, below are their ranking in search results
d. Relative rating: Use same logic as above to calculate the relative rating (not count) of a
   brand.
e. Price distribution of SKUs

Please see pdf for presentation 

# Run the ingestion code 
python3 main.py
