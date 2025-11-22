import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# --- Dynamically construct paths ---
# This makes the script runnable from any directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# The data file is located one level above the project root
data_file_dir = os.path.dirname(project_root)
FILE_PATH = os.path.join(data_file_dir, 'cleaned_superstore.csv') # <-- Corrected filename and path
IMAGE_DIR = os.path.join(project_root, 'images')
# --- End of path construction ---

if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

try:
    df = pd.read_csv(FILE_PATH)
except Exception as e:
    print(f"Error loading data for Role 6: {e}")
    exit()

sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (10, 6)
print("Role 6: Profit Hunter script loaded successfully.")

# ------------------------------------------------------
# --- CHART 5: Discount Impact on Profitability ---
# ------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x='Discount',
    y='Profit',
    alpha=0.5,
    hue=(df['Profit'] < 0),
    palette={True: '#d73027', False: '#4575b4'},
    size='Sales',
    sizes=(10, 250),
    legend='full'
)

# Reference lines
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(0.20, color='red', linestyle=':', linewidth=2, label='20% Discount Threshold')

plt.title('Chart 5: Discount Impact on Profitability', fontsize=14)
plt.xlabel('Discount Percentage', fontsize=12)
plt.ylabel('Profit (USD)', fontsize=12)
plt.legend(title='Is Loss?', loc='lower left')
plt.tight_layout()

# Save output
chart5_path = os.path.join(IMAGE_DIR, 'Chart_5_Discount_vs_Profit.png')
plt.savefig(chart5_path)
plt.close()

print(f"-> Chart 5 saved: {chart5_path}")

# ------------------------------------------------------
# --- CHART 6: Top 15 States with the Largest Loss ---
# ------------------------------------------------------

state_profit = (
    df.groupby('State')['Profit']
      .sum()
      .sort_values()
      .head(15)
      .reset_index()
)

colors_state = ['#d73027' for _ in state_profit['State']]  # all red = loss

plt.figure(figsize=(10, 7))
sns.barplot(
    data=state_profit,
    x='Profit',
    y='State',
    palette=colors_state
)

plt.axvline(0, color='black', linestyle='-', linewidth=0.8)
plt.title('Chart 6: Top 15 States with the Largest Cumulative Profit Loss', fontsize=14)
plt.xlabel('Total Profit (USD)', fontsize=12)
plt.ylabel('State', fontsize=12)
plt.tight_layout()

chart6_path = os.path.join(IMAGE_DIR, 'Chart_6_Profit_by_State.png')
plt.savefig(chart6_path)
plt.close()

print(f"-> Chart 6 saved: {chart6_path}")
