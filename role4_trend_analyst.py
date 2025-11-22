import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.dates import DateFormatter

# --- SETUP (REQUIRED FOR STANDALONE EXECUTION) ---

FILE_PATH = 'cleaned_superstore.csv'
IMAGE_DIR = 'images'
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

try:
    df = pd.read_csv(FILE_PATH)
    # Ensure date columns are proper datetime objects
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    # Recreate the Order_Month_Start for time-series aggregation
    df['Order_Month_Start'] = pd.to_datetime(df['Order Year'].astype(str) + '-' + df['Order Month'].astype(str).str.zfill(2) + '-01')
except Exception as e:
    print(f"Error loading data for Role 4: {e}")
    exit()

sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (10, 6)
print("Role 4: Trend Analyst script loaded successfully.")

# --- CHART 1: Monthly Sales and Profit Trend Analysis ---

# Aggregate data monthly
monthly_trends = df.groupby('Order_Month_Start').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum')
).reset_index()

plt.figure(figsize=(14, 6))
sns.lineplot(data=monthly_trends, x='Order_Month_Start', y='Total_Sales', label='Total Sales (USD)', linewidth=2, color='#2c7bb6')
sns.lineplot(data=monthly_trends, x='Order_Month_Start', y='Total_Profit', label='Total Profit (USD)', linewidth=2, color='#fdae61')

# Zero line for profit/loss reference
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)

# Format the X-axis for better readability
date_form = DateFormatter("%b %Y")
plt.gca().xaxis.set_major_formatter(date_form)
plt.xticks(rotation=45, ha='right')

plt.title('Chart 1: Monthly Sales and Profit Trend Analysis (Identifying Seasonality)', fontsize=14)
plt.xlabel('Order Month', fontsize=12)
plt.ylabel('Amount (USD)', fontsize=12)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig(os.path.join(IMAGE_DIR, 'Chart_1_Sales_Profit_Monthly.png'))
plt.close()
print("-> Chart 1 saved: images/Chart_1_Sales_Profit_Monthly.png")


# --- CHART 2: Average Delivery Time by Shipping Mode ---

# Calculate mean delivery days by ship mode
delivery_analysis = df.groupby('Ship Mode')['Delivery Days'].mean().sort_values(ascending=False).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=delivery_analysis, x='Ship Mode', y='Delivery Days', palette='viridis')

plt.title('Chart 2: Average Delivery Time by Shipping Mode', fontsize=14)
plt.xlabel('Ship Mode', fontsize=12)
plt.ylabel('Average Delivery Days', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(IMAGE_DIR, 'Chart_2_Delivery_Days_by_Ship_Mode.png'))
plt.close()
print("-> Chart 2 saved: images/Chart_2_Delivery_Days_by_Ship_Mode.png")