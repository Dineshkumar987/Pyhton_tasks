import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Automatically get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "kc_house_data.csv")

# Load the dataset
df = pd.read_csv(csv_path)

# Create output folder for graphs
os.makedirs("graphs/q4", exist_ok=True)

# ==========================================
# Scenario 1: Data Loading & Basic Cleaning
# ==========================================
print("=" * 60)
print("Q4 - Scenario 1: Data Loading & Basic Cleaning")
print("=" * 60)

# 1. Load dataset
df = pd.read_csv("kc_house_data.csv")

# 2. Display head & columns
print("First 5 Rows:\n", df.head())
print("\nColumns:", df.columns.tolist())

# 3, 4 & 5. Check, fill missing values & convert to numeric
num_cols = ["bedrooms", "bathrooms", "sqft_living", "price"]
for c in num_cols:
  df[c] = pd.to_numeric(df[c], errors="coerce")

df["bedrooms"] = df["bedrooms"].fillna(df["bedrooms"].mode()[0])
df["bathrooms"] = df["bathrooms"].fillna(df["bathrooms"].mean())
df["sqft_living"] = df["sqft_living"].fillna(df["sqft_living"].mean())
df["price"] = df["price"].fillna(df["price"].mean())

print("\nMissing values after cleaning:\n", df[num_cols].isnull().sum())

# ==========================================
# Scenario 2: Line Graph + Save
# ==========================================
print("\n" + "=" * 60)
print("Q4 - Scenario 2: Line Graph (First 10 House Prices)")
print("=" * 60)

# 1, 2 & 3. Select columns, first 10 rows, convert to NumPy
sample_prices = df["price"].head(10).to_numpy()

# 4, 5 & 6. Plot line graph & save
plt.figure(figsize=(9, 4.5))
plt.plot(
    range(10),
    sample_prices,
    marker="o",
    color="#2563eb",
    linewidth=2,
    markersize=6,
)
plt.title("House Prices for First 10 Records", fontsize=12, fontweight="bold")
plt.xlabel("Index (0-9)")
plt.ylabel("Price ($)")
plt.xticks(range(10))
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q4/house_prices_line.png", dpi=300)
plt.show()
print("Graph saved -> graphs/q4/house_prices_line.png")

# ==========================================
# Scenario 3: Filtering + Bar Chart + Save
# ==========================================
print("\n" + "=" * 60)
print("Q4 - Scenario 3: Expensive Houses Bar Chart (Price > 1,000,000)")
print("=" * 60)

# 1, 2 & 3. Filter price > 1000000, count by bedrooms, select top
exp_houses = df[df["price"] > 1_000_000]
bed_counts = exp_houses["bedrooms"].value_counts().head(6)

# 4. Convert to NumPy
beds_np = bed_counts.index.astype(str).to_numpy()
counts_np = bed_counts.values

# 5, 6 & 7. Plot bar chart and save
plt.figure(figsize=(9, 4.5))
plt.bar(beds_np, counts_np, color="#7c3aed", width=0.55)
plt.title(
    "Count of Expensive Houses (> $1,000,000) by Bedroom Category",
    fontweight="bold",
)
plt.xlabel("Bedrooms")
plt.ylabel("Count of Houses")
plt.tight_layout()
plt.savefig("graphs/q4/expensive_houses_bar.png", dpi=300)
plt.show()
print("Graph saved -> graphs/q4/expensive_houses_bar.png")

# SCENARIO 3: Filtering + Bar Chart + Save
 
# �� Tasks:
# 1. Filter houses where:
# ○ price > 1000000
# 2. Count number of houses per:
# ○ bedrooms
# 3. Select top bedroom categories.
# 4. Convert results to NumPy arrays.
# 5. Plot a bar chart:
# ○ X-axis → Bedrooms
# ○ Y-axis → Count
# 6. Rotate labels if needed.
# 7. Save graph: plt.savefig("expensive_houses_bar.png")
 
#Cleaning data
df["price"] = pd.to_numeric(df["price"], errors = "coerce") # Convert the "price" column into numeric values invalid value replace it with NaN
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors = "coerce") # Convert the "bedrooms" column into numeric values invalid values replace it with nan
df["bedrooms"] = df["bedrooms"].round().astype(int)  # Round is used to round decimal values Example: 3.7 → 4, 2.3 → 2Convert the result into integer type
expensive_houses = df[df["price"] > 1000000] #filter whose price is greater than 1,000,000
bedrooms_counts = expensive_houses["bedrooms"].value_counts() #Counting number of houses per bedrooms
top_bedrooms = bedrooms_counts.head(5)
#Converting results to NumPy arrays
x = top_bedrooms.index.to_numpy()
y = top_bedrooms.values
#Bar plot
plt.figure(figsize = (8,5))
plt.bar(x,y, color = "skyblue",edgecolor = "navy") # colour = bar fill color,edgecolor = border color of bars
plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.title("Expensive Houses by Bedrooms")
plt.xticks(rotation = 0)
plt.tight_layout()
plt.savefig("graphs/expensive_houses_bar.png")
plt.show()
 
# SCENARIO 4: Pie Chart (Region Distribution) + Save
# �� Tasks:
# 1. Count number of houses by:
# ○ bedrooms
# 2. Select top 5 bedroom categories.
# 3. Prepare:
# ○ Labels
# ○ Values
# 4. Plot a pie chart.
# 5. Add percentage labels.
# 6. Save graph: plt.savefig("bedroom_distribution.png")
 
bedroom_counts = df['bedrooms'].value_counts() #count number of houses has bedroom
top_5_bedrooms = bedroom_counts.head(5) #select top5 bedrooms count
# 3. Prepare: Labels and Values
labels = [f"{int(b)} Bedrooms" for b in top_5_bedrooms.index] # Convert bedroom numbers into readable labels Example: 3 becomes "3 Bedrooms"
values = top_5_bedrooms.values
plt.figure(figsize=(10, 7))
plt.pie(values,labels=labels,shadow = True,autopct='%1.1f%%',startangle=140)
# Adding details for clarity
plt.title('Top 5 Bedroom Categories', pad = 20)
plt.axis('equal')  # Ensures the pie chart is a circle
plt.legend()
# 6. Save graph
plt.savefig("graphs/bedroom_distribution.png")
plt.show()
print("Pie chart successfully generated and saved as 'bedroom_distribution.png'")
# ==========================================
# Scenario 5: Advanced Analysis + Multiple Graphs
# ==========================================
print("\n" + "=" * 60)
print("Q4 - Scenario 5: Advanced House Price Analysis")
print("=" * 60)


# Part 1: Feature Creation
def categorize_price(p):
  if p >= 1_000_000:
    return "Luxury"
  elif p >= 500_000:
    return "Mid Range"
  return "Affordable"


df["Price Category"] = df["price"].apply(categorize_price)

# Part 2: NumPy Usage
prices_np = df["price"].to_numpy()
price_diffs = np.diff(prices_np)

# Part 3 & 4: Visualizations & Saving
# Line Graph
plt.figure(figsize=(10, 4.5))
plt.plot(range(len(prices_np)), prices_np, color="#475569", alpha=0.7)
plt.title("Price Trend for All Houses", fontweight="bold")
plt.xlabel("House Index")
plt.ylabel("Price ($)")
plt.tight_layout()
plt.savefig("graphs/q4/price_trend.png", dpi=300)
plt.savefig("graphs/q4/price_trend.png", dpi=300)
plt.show()

# Stacked Bar Chart
top_beds_list = df["bedrooms"].value_counts().head(5).index
filtered_df = df[df["bedrooms"].isin(top_beds_list)]
stacked_price = (
    filtered_df.groupby(["bedrooms", "Price Category"])
    .size()
    .unstack(fill_value=0)
)

stacked_price.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 5),
    color=["#10b981", "#3b82f6", "#f59e0b"],
)
plt.title("Price Category Count per Bedroom Category", fontweight="bold")
plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.legend(title="Price Category")
plt.tight_layout()
plt.savefig("graphs/q4/price_category_stacked.png", dpi=300)
plt.show()

# Histogram
plt.figure(figsize=(9, 4.5))
plt.hist(
    prices_np[prices_np < 3_000_000],
    bins=30,
    color="#059669",
    edgecolor="black",
    alpha=0.8,
)
plt.title("Distribution of House Prices (Up to $3M)", fontweight="bold")
plt.xlabel("Price ($)")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("graphs/q4/price_histogram.png", dpi=300)
plt.show()

# Part 5: Insights
print("\n--- Insights ---")
print(
    "1. Most expensive houses bedroom category: 4 bedrooms (followed by 3 & 5"
    " bedrooms)."
)
print(
    f"2. Most common price category: {df['Price Category'].value_counts().idxmax()} ({df['Price Category'].value_counts().max()} houses)."
)
print(
    "3. Price distribution pattern: Strongly Right-skewed and concentrated in"
    " the lower/affordable tier (< $500k)."
)