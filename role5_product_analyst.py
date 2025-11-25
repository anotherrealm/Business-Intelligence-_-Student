import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- SETUP (REQUIRED FOR STANDALONE EXECUTION) ---

FILE_PATH = 'cleaned_superstore.csv'
IMAGE_DIR = 'images'
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

try:
    df = pd.read_csv(FILE_PATH)
    # No date conversion needed for these charts, but load must succeed
except Exception as e:
    print(f"Error loading data for Role 5: {e}")
    exit()

sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (10, 6)
print("Role 5: Product Analyst script loaded successfully.")

# --- CHART 3: Total Profit by Sub-Category ---

# Identify the top 3 money-losing products (Tables, Supplies, etc.)
subcategory_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False).reset_index()

# Define colors: Red for loss, Green for profit
colors = ['#d73027' if p < 0 else '#1a9850' for p in subcategory_profit['Profit']]

plt.figure(figsize=(10, 8))
sns.barplot(data=subcategory_profit, y='Sub-Category', x='Profit', palette=colors)

plt.axvline(0, color='black', linestyle='-', linewidth=0.5)

plt.title('Chart 3: Total Profit by Sub-Category (Identifying Losers)', fontsize=14)
plt.xlabel('Total Profit (USD)', fontsize=12)
plt.ylabel('Sub-Category', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(IMAGE_DIR, 'Chart_3_Profit_by_Sub_Category.png'))
plt.close()
print("-> Chart 3 saved: images/Chart_3_Profit_by_Sub_Category.png")


# --- CHART 4: Product Cost vs. Customer Demand (Price vs Quantity) ---

# Group by product name to get aggregate demand (Quantity) and average price (Unit Cost)
product_data = df[df['Quantity'] > 0].groupby('Sub-Category').agg(
    Avg_Unit_Cost=('Unit Cost', 'mean'),
    Total_Quantity=('Quantity', 'sum')
).reset_index()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=product_data, x='Avg_Unit_Cost', y='Total_Quantity', 
                alpha=0.6, hue='Total_Quantity', size='Avg_Unit_Cost', sizes=(20, 300), 
                palette='coolwarm', legend=False)

# Log scale helps visualize the wide range of product costs
plt.xscale('log') 

plt.title('Chart 4: Sub-Category vs. Customer Demand (Avg. Unit Cost vs. Total Quantity)', fontsize=14)
plt.xlabel('Average Sub-Category Unit Cost (USD) [Log Scale]', fontsize=12)
plt.ylabel('Total Quantity Sold', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(IMAGE_DIR, 'Chart_4_Price_vs_Quantity.png'))
plt.close()
print("-> Chart 4 saved: images/Chart_4_Price_vs_Quantity.png")
