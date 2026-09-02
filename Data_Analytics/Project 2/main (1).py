import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# ==============================================================================
# SCENARIO 1: Data Loading & Preprocessing
# ==============================================================================

# 1. Load dataset using pandas
data = pd.read_csv("ign.csv")

print("Displaying the first 5 rows of data:")
print(data.head())
print("------------------------------------------------------------------------------")

print("Displaying the last 5 rows of data:")
print(data.tail())
print("------------------------------------------------------------------------------")

print("The shape of the dataset is: ")
print(data.shape)
print("------------------------------------------------------------------------------")

# 3. Remove unnecessary column
data.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')
print("Removed the column Unnamed: 0 (if present)!!")
print("------------------------------------------------------------------------------")

# 4. Check missing values before handling
missing_values = data[['score', 'genre', 'platform']].isnull().sum()
print("Total missing values before handling:\n", missing_values)
print("------------------------------------------------------------------------------")

# 5. Handle missing values & convert numeric data
data['score'] = pd.to_numeric(data['score'], errors='coerce')
average_score = data['score'].mean()
data['score'] = data['score'].fillna(average_score)

if not data['genre'].mode().empty:
    data['genre'] = data['genre'].fillna(data['genre'].mode()[0])

if not data['platform'].mode().empty:
    data['platform'] = data['platform'].fillna(data['platform'].mode()[0])

print("Replaced missing values correctly!!")
print("------------------------------------------------------------------------------")

# 6. Ensure correct data types
data = data.astype({
    'score': 'float64',
    'release_year': 'int32',
    'release_month': 'int32',
    'release_day': 'int32'
})

print("Changed column types to their respective formats.")
print("------------------------------------------------------------------------------")


# ==============================================================================
# SCENARIO 2: Line Graph (Score Trend) + Save
# ==============================================================================

grouped_year = data.groupby('release_year')['score'].mean()

print("The average score for respective years is:")
print(grouped_year)
print("------------------------------------------------------------------------------")

# Convert to NumPy arrays
years = grouped_year.index.to_numpy()
avg_scores = grouped_year.values

# Plot line graph
plt.figure()
plt.plot(years, avg_scores, marker='o')
plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("avg_score_trend.png")
plt.show()


# ==============================================================================
# SCENARIO 3: Filtering + Bar Chart + Save
# ==============================================================================

# Filter dataset where score > 7
filtered_data = data[data['score'] > 7]

# Count high-rated games per platform
top_rated_games = filtered_data.groupby('platform')['title'].count()
top_10 = top_rated_games.sort_values(ascending=False).head(10)

print("Top 10 Platforms by High-Rated Games count:")
print(top_10)
print("------------------------------------------------------------------------------")

# Convert to NumPy arrays
platforms = top_10.index.to_numpy()
counts = top_10.values

# Plot bar chart
plt.figure()
plt.bar(platforms, counts)
plt.title("Top 10 Platforms by High-Rated Games")
plt.xlabel("Platform")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_platforms_bar.png")
plt.show()


# ==============================================================================
# SCENARIO 4: Aggregation + Pie Chart + Save
# ==============================================================================

# Count games per genre
genre_counts = data['genre'].value_counts()
top_5 = genre_counts.head(5)

print("Top 5 Genres:")
print(top_5)
print("------------------------------------------------------------------------------")

# Prepare labels and values
genres = top_5.index.to_numpy()
genre_values = top_5.values

# Plot pie chart
plt.figure(figsize=(8, 6))
plt.pie(genre_values, labels=genres, autopct='%1.1f%%', startangle=140)
plt.title("Genre Distribution")
plt.tight_layout()
plt.savefig("genre_distribution.png")
plt.show()


# ==============================================================================
# SCENARIO 5: Advanced Analysis + Multiple Graphs
# ==============================================================================

# Part 1: Feature Engineering
data['score_category'] = np.where(
    data['score'] >= 9, "Excellent",
    np.where(data['score'] >= 7, "Good", "Average")
)

data['editors_choice'] = data['editors_choice'].map({'Y': 1, 'N': 0}).fillna(0).astype(int)

# Part 2: NumPy Analysis
yearly_avg = data.groupby('release_year')['score'].mean()
years = yearly_avg.index.to_numpy()
avg_scores = yearly_avg.values
score_growth = np.diff(avg_scores)

print("Yearly Score Differences (NumPy diff):")
print(score_growth)
print("------------------------------------------------------------------------------")

# Part 3: Visualizations

# 1. Line Graph (Score Trend)
plt.figure()
plt.plot(years, avg_scores, marker='o')
plt.title("Average Score Trend Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("score_trend.png")
plt.show()

# 2. Stacked Bar Chart (Score Category per Year)
category_counts = data.pivot_table(
    index='release_year',
    columns='score_category',
    aggfunc='size',
    fill_value=0
)
category_counts.plot(kind='bar', stacked=True)
plt.title("Score Category Distribution per Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("score_category_stacked.png")
plt.show()

# 3. Histogram (Score Distribution)
plt.figure()
plt.hist(data['score'], bins=20, edgecolor='black')
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.show()

# Part 5: Insights
max_year = yearly_avg.idxmax()
max_score = yearly_avg.max()

print(f"Year with highest average score: {max_year} ({max_score:.2f})")

if len(score_growth) > 0 and score_growth.mean() > 0:
    print("Overall trend: Scores are increasing over time")
else:
    print("Overall trend: Scores are decreasing or fluctuating")

editors_avg = data.groupby('editors_choice')['score'].mean()
print("\nAverage score based on editors_choice:")
print(editors_avg)

if 1 in editors_avg and 0 in editors_avg and editors_avg[1] > editors_avg[0]:
    print("Editors' Choice games generally have higher scores")
else:
    print("Editors' Choice does not strongly correlate with higher scores")