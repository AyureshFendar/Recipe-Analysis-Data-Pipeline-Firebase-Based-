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
interactions = interactions.merge(recipes[['recipeId','name']], on='recipeId', how='left')

# Fix ingredients: if they are stored as strings or lists, explode them
if 'ingredient' not in ingredients.columns and 'ingredients' in recipes.columns:
    ingredients = recipes[['recipeId','ingredients']].copy()
    # Convert stringified lists to actual lists if necessary
    ingredients['ingredients'] = ingredients['ingredients'].apply(lambda x: eval(x) if isinstance(x, str) and x.startswith('[') else x)
    ingredients = ingredients.explode('ingredients')
    ingredients = ingredients.rename(columns={'ingredients':'ingredient'})

# Remove generic placeholder names (like 'Ingredient 1') if present
ingredients = ingredients[ingredients['ingredient'].notna() & ~ingredients['ingredient'].str.contains('Ingredient', case=False)]

# Strip whitespace from ingredient names
ingredients['ingredient'] = ingredients['ingredient'].str.strip()

# ---------------- INSIGHT 1: Most common ingredients ----------------
common_ingredients = ingredients['ingredient'].value_counts().head(10)
print("Most common ingredients:\n", common_ingredients)
plt.figure(figsize=(10,6))
common_ingredients.plot(kind='bar', title='Top 10 Most Common Ingredients', color='skyblue')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ---------------- INSIGHT 9: Ingredients associated with high engagement ----------------
ingredient_engagement = pd.merge(ingredients, interactions[['recipeId','number_of_likes']], on='recipeId')
engagement_by_ingredient = ingredient_engagement.groupby('ingredient')['number_of_likes'].mean().sort_values(ascending=False).head(10)
print("Ingredients with highest engagement:\n", engagement_by_ingredient)
plt.figure(figsize=(10,6))
engagement_by_ingredient.plot(kind='bar', title='Top 10 Ingredients by Engagement', color='salmon')
plt.ylabel('Average Likes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()