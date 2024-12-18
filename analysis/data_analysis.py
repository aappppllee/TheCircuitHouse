import pandas as pd
import numpy as np
from database.manage_db import fetch_query
from analysis.sql_queries import sku_count_per_brand, price_distribution

def analyze_sku_count():
    query = sku_count_per_brand()
    results = fetch_query(query)
    df = pd.DataFrame(results, columns=['Brand_Name', 'SKU_Count'])
    return df

def analyze_price_distribution():
    query = price_distribution()
    results = fetch_query(query)
    df = pd.DataFrame(results, columns=['Price_Band', 'SKU_Count'])
    return df
