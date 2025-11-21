import pandas as pd
import matplotlib.pyplot as plt

# ---------------- CONFIG ----------------
DATA_DIR = r"C:\Users\DELL\OneDrive\Desktop\ThinkBridge\New_Task\data"

# Load CSVs
recipes = pd.read_csv(f"{DATA_DIR}/recipe.csv")
ingredients = pd.read_csv(f"{DATA_DIR}/ingredients.csv")
interactions = pd.read_csv(f"{DATA_DIR}/interactions.csv")

# Ensure recipes have 'name' column
if 'name' not in recipes.columns:
    recipes = recipes.rename(columns={'title': 'name'})

# Merge interactions with recipe names
interactions = interactions.merge(recipes[['recipeId','name','category']], on='recipeId', how='left')

# -----------------------------------------
# NEW INSIGHT 1: Recipe Category Popularity
# -----------------------------------------
category_views = interactions.groupby('category')['number_of_views'].sum().sort_values(ascending=False)

print("Most Popular Categories (By Views):\n", category_views.head(10))

plt.figure(figsize=(10,6))
category_views.plot(kind='bar', title='Most Popular Recipe Categories (Views)', color='teal')
plt.ylabel('Total Views')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------- INSIGHT 2: Average preparation time ----------------
avg_prep_time = recipes['cookTimeMinutes'].mean()
print("Average preparation time (minutes):", avg_prep_time)
plt.hist(recipes['cookTimeMinutes'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Preparation Time')
plt.xlabel('Cook Time (minutes)')
plt.ylabel('Number of Recipes')
plt.show()

# ---------------- INSIGHT 3: Difficulty distribution ----------------
difficulty_dist = recipes['difficulty'].value_counts()
print("Difficulty distribution:\n", difficulty_dist)
difficulty_dist.plot(kind='pie', autopct='%1.1f%%', title='Difficulty Distribution')
plt.ylabel('')
plt.show()

# ---------------- INSIGHT 4: Most frequently viewed recipes ----------------
most_viewed = interactions.groupby('name')['number_of_views'].sum().sort_values(ascending=False).head(10)
print("Most frequently viewed recipes:\n", most_viewed)
most_viewed.plot(kind='bar', title='Top 10 Most Viewed Recipes')
plt.ylabel('Views')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ---------------- INSIGHT 5: Average likes per recipe ----------------
avg_likes = interactions.groupby('name')['number_of_likes'].mean().sort_values(ascending=False).head(10)
print("Recipes with highest average likes:\n", avg_likes)
avg_likes.plot(kind='bar', title='Top 10 Recipes by Average Likes')
plt.ylabel('Average Likes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ---------------- INSIGHT 6: Average cook attempts ----------------
avg_attempts = interactions.groupby('name')['cook_attempts'].mean().sort_values(ascending=False).head(10)
print("Recipes with highest cook attempts:\n", avg_attempts)
avg_attempts.plot(kind='bar', title='Top 10 Recipes by Average Cook Attempts')
plt.ylabel('Cook Attempts')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ---------------- INSIGHT 7: Correlation between prep time and likes ----------------
merged = pd.merge(
    recipes[['recipeId', 'cookTimeMinutes','name']],
    interactions[['recipeId','number_of_likes']],
    on='recipeId'
)
corr = merged['cookTimeMinutes'].corr(merged['number_of_likes'])
print("Correlation between prep time and likes:", corr)
plt.scatter(merged['cookTimeMinutes'], merged['number_of_likes'], alpha=0.7)
plt.title(f'Prep Time vs Likes (Correlation: {corr:.2f})')
plt.xlabel('Cook Time (minutes)')
plt.ylabel('Number of Likes')
plt.show()

# ---------------- INSIGHT 8: Recipes with highest avg_rating ----------------
top_rated = interactions.groupby('name')['avg_rating'].mean().sort_values(ascending=False).head(10)
print("Top rated recipes:\n", top_rated)
top_rated.plot(kind='bar', title='Top 10 Recipes by Average Rating')
plt.ylabel('Avg Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --------------------------------------------------
# NEW INSIGHT 9: Difficulty Level vs Average Cook Time
# --------------------------------------------------
diff_cook = recipes.groupby('difficulty')['cookTimeMinutes'].mean().sort_values()

print("Average Cook Time by Difficulty:\n", diff_cook)

plt.figure(figsize=(8,5))
diff_cook.plot(kind='bar', color='orchid', title='Average Cook Time by Difficulty Level')
plt.ylabel('Average Cook Time (minutes)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ---------------- INSIGHT 10: Recipes by difficulty vs average likes ----------------
difficulty_likes = pd.merge(
    recipes[['recipeId','difficulty','name']],
    interactions[['recipeId','number_of_likes']],
    on='recipeId'
)
diff_avg_likes = difficulty_likes.groupby('difficulty')['number_of_likes'].mean()
print("Average likes by difficulty:\n", diff_avg_likes)
diff_avg_likes.plot(kind='bar', title='Average Likes by Difficulty')
plt.ylabel('Average Likes')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
