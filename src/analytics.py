import pandas as pd

# Load data
recipes = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\ThinkBridge\New_Task\data\recipe.csv")
interactions = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\ThinkBridge\New_Task\data\interactions.csv")


# 1. Most common ingredients
ingredients = recipes.explode('ingredients')
most_common_ingredients = ingredients['ingredients'].value_counts()
print("Most Common Ingredients:\n", most_common_ingredients.head(10))

# 2. Average preparation time
avg_prep_time = recipes['prep_time'].mean()
print("Average Preparation Time:", avg_prep_time)

# 3. Difficulty distribution
difficulty_dist = recipes['difficulty'].value_counts()
print("Difficulty Distribution:\n", difficulty_dist)

# 4. Most frequently viewed recipes
views = interactions.groupby('recipe_name')['views'].sum().sort_values(ascending=False)
print("Most Frequently Viewed Recipes:\n", views.head(10))

# 5. Recipes with highest average likes
avg_likes = interactions.groupby('recipe_name')['likes'].mean().sort_values(ascending=False)
print("Recipes with Highest Average Likes:\n", avg_likes.head(10))

# 6. Recipes with highest cook attempts
cook_attempts = interactions.groupby('recipe_name')['cook_attempts'].mean().sort_values(ascending=False)
print("Recipes with Highest Cook Attempts:\n", cook_attempts.head(10))

# 7. Correlation between prep time and likes
merged = pd.merge(recipes, interactions.groupby('recipe_name')['likes'].mean().reset_index(), left_on='name', right_on='recipe_name')
correlation = merged['prep_time'].corr(merged['likes'])
print("Correlation between Prep Time and Likes:", correlation)

# 8. Top rated recipes (avg rating)
top_rated = interactions.groupby('recipe_name')['rating'].mean().sort_values(ascending=False)
print("Top Rated Recipes:\n", top_rated.head(10))

# 9. Ingredients with highest engagement (avg likes)
ingredients_engagement = recipes.explode('ingredients')
ingredients_engagement = pd.merge(
    ingredients_engagement, 
    interactions.groupby('recipe_name')['likes'].mean().reset_index(), 
    left_on='name', right_on='recipe_name'
)
engagement = ingredients_engagement.groupby('ingredients')['likes'].mean().sort_values(ascending=False)
print("Ingredients with Highest Engagement:\n", engagement.head(10))

# 10. Average likes by difficulty
likes_by_difficulty = merged.groupby('difficulty')['likes'].mean()
print("Average Likes by Difficulty:\n", likes_by_difficulty)
