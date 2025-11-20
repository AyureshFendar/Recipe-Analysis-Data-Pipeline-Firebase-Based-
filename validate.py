import pandas as pd
import os

# ---------------- CONFIG ----------------
DATA_DIR = r"C:\Users\DELL\OneDrive\Desktop\ThinkBridge\New_Task\data"
REPORT_DIR = "validation_report"
os.makedirs(REPORT_DIR, exist_ok=True)
SUMMARY_FILE = os.path.join(REPORT_DIR, "validation_summary.csv")

# ---------------- HELPER FUNCTIONS ----------------
def log_invalid(df, reasons, filename):
    df_copy = df.copy()
    df_copy["validation_error"] = reasons
    df_copy.to_csv(os.path.join(REPORT_DIR, filename), index=False)

def validate_required(df, columns):
    return df[columns].notna().all(axis=1)

def validate_positive_numeric(df, columns):
    return (df[columns] >= 0).all(axis=1)

def validate_non_empty_array(df, column):
    return df[column].apply(lambda x: isinstance(x, str) and len(x.strip()) > 0)

def validate_difficulty(df, column="difficulty"):
    allowed = ["Easy", "Medium", "Hard"]
    return df[column].isin(allowed)

# ---------------- VALIDATION PROCESS ----------------
summary = []

# --- Recipes ---
recipes = pd.read_csv(os.path.join(DATA_DIR, "recipe.csv"))
invalid_reasons = []
required_mask = validate_required(recipes, ["recipeId", "title", "category", "difficulty", "cookTimeMinutes"])
invalid_reasons.append(~required_mask)
positive_mask = validate_positive_numeric(recipes, ["cookTimeMinutes"])
invalid_reasons.append(~positive_mask)
difficulty_mask = validate_difficulty(recipes, "difficulty")
invalid_reasons.append(~difficulty_mask)
invalid_mask = pd.concat(invalid_reasons, axis=1).any(axis=1)
valid_recipes = recipes[~invalid_mask]
invalid_recipes = recipes[invalid_mask]
log_invalid(invalid_recipes, "Invalid fields", "invalid_recipes.csv")
valid_recipes.to_csv(os.path.join(REPORT_DIR, "valid_recipes.csv"), index=False)
summary.append({"collection": "recipes", "valid": len(valid_recipes), "invalid": len(invalid_recipes)})

# --- Ingredients ---
ingredients = pd.read_csv(os.path.join(DATA_DIR, "ingredients.csv"))
invalid_reasons = []
required_mask = validate_required(ingredients, ["recipeId", "ingredient"])
invalid_reasons.append(~required_mask)
non_empty_mask = validate_non_empty_array(ingredients, "ingredient")
invalid_reasons.append(~non_empty_mask)
invalid_mask = pd.concat(invalid_reasons, axis=1).any(axis=1)
valid_ingredients = ingredients[~invalid_mask]
invalid_ingredients = ingredients[invalid_mask]
log_invalid(invalid_ingredients, "Invalid fields", "invalid_ingredients.csv")
valid_ingredients.to_csv(os.path.join(REPORT_DIR, "valid_ingredients.csv"), index=False)
summary.append({"collection": "ingredients", "valid": len(valid_ingredients), "invalid": len(invalid_ingredients)})

# --- Steps ---
steps = pd.read_csv(os.path.join(DATA_DIR, "steps.csv"))
invalid_reasons = []
required_mask = validate_required(steps, ["recipeId", "stepNumber", "instruction"])
invalid_reasons.append(~required_mask)
positive_mask = steps["stepNumber"].apply(lambda x: isinstance(x, (int,float)) and x > 0)
invalid_reasons.append(~positive_mask)
non_empty_mask = validate_non_empty_array(steps, "instruction")
invalid_reasons.append(~non_empty_mask)
invalid_mask = pd.concat(invalid_reasons, axis=1).any(axis=1)
valid_steps = steps[~invalid_mask]
invalid_steps = steps[invalid_mask]
log_invalid(invalid_steps, "Invalid fields", "invalid_steps.csv")
valid_steps.to_csv(os.path.join(REPORT_DIR, "valid_steps.csv"), index=False)
summary.append({"collection": "steps", "valid": len(valid_steps), "invalid": len(invalid_steps)})

# --- User Interactions ---
interactions = pd.read_csv(os.path.join(DATA_DIR, "interactions.csv"))
invalid_reasons = []
required_mask = validate_required(interactions, ["interactionId", "userId", "recipeId"])
invalid_reasons.append(~required_mask)
positive_mask = validate_positive_numeric(interactions, ["avg_rating", "cook_attempts", "number_of_likes", "number_of_views"])
invalid_reasons.append(~positive_mask)
invalid_mask = pd.concat(invalid_reasons, axis=1).any(axis=1)
valid_interactions = interactions[~invalid_mask]
invalid_interactions = interactions[invalid_mask]
log_invalid(invalid_interactions, "Invalid fields", "invalid_interactions.csv")
valid_interactions.to_csv(os.path.join(REPORT_DIR, "valid_interactions.csv"), index=False)
summary.append({"collection": "user_interactions", "valid": len(valid_interactions), "invalid": len(invalid_interactions)})

# ---------------- SAVE SUMMARY CSV ----------------
summary_df = pd.DataFrame(summary)
summary_df.to_csv(SUMMARY_FILE, index=False)
print(f"Validation summary saved to {SUMMARY_FILE}")
