import matplotlib.pyplot as plt
import seaborn as sns
from analysis.data_analysis import analyze_sku_count, analyze_price_distribution

def plot_sku_count():
    df = analyze_sku_count()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='SKU_Count', y='Brand_Name', palette='viridis')
    plt.title('SKU Count per Brand')
    plt.xlabel('SKU Count')
    plt.ylabel('Brand Name')
    plt.show()

def plot_price_distribution():
    df = analyze_price_distribution()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='SKU_Count', y='Price_Band', palette='magma')
    plt.title('Price Distribution of SKUs')
    plt.xlabel('SKU Count')
    plt.ylabel('Price Band')
    plt.show()
