# ---------------------------------------------------------
# Firestore Seeder (NO subcollections, 30 interactions only)
# ---------------------------------------------------------
import random
import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# ---------------------------------------------------------
# 1. FIREBASE INITIALIZATION
# ---------------------------------------------------------
cred = credentials.Certificate(
    r"C:\Users\DELL\OneDrive\Desktop\ThinkBridge\New_Task\service_account.json"
)
firebase_admin.initialize_app(cred)
db = firestore.client()


# ---------------------------------------------------------
# 2. REAL PANEER TIKKA MASALA (Detailed)
# ---------------------------------------------------------
paneer_steps = [
    "Turn gas ON to medium flame and place a heavy-bottom pan on the stove.",
    "Measure 200 grams paneer and cut into 2 cm cubes; keep cubes on a plate.",
    "In a mixing bowl add 1/2 cup thick curd, 2 tbsp besan, 1 tbsp ginger-garlic paste, "
    "1 tsp red chilli powder, 1/2 tsp turmeric, 1/2 tsp garam masala, 1 tsp kasuri methi and 1 tsp salt; mix until smooth.",
    "Coat paneer cubes evenly with the marinade.",
    "Cover bowl and rest 30 minutes.",
    "Heat 2 tbsp oil in pan on medium flame for 40 seconds.",
    "Place paneer cubes and sear each side 40–50 seconds.",
    "Remove paneer and keep aside.",
    "Heat 1 tbsp butter + 1 tbsp oil; add chopped onion.",
    "Sauté 4–5 minutes until golden.",
    "Add tomatoes, cook 5 minutes.",
    "Add cashews, cook 1.5 minutes, blend to smooth paste.",
    "Return paste, add spices and salt.",
    "Cook 6–7 minutes until oil separates.",
    "Add 1/2 cup water, boil then simmer 3 minutes.",
    "Add cream, mix, add paneer, simmer 5 minutes.",
    "Turn gas OFF and rest 2 minutes."
]

paneer_recipe = {
    "id": "r1",
    "name": "Paneer Tikka Masala",
    "category": "Indian",
    "difficulty": "Medium",
    "cook_time": 45,
    "ingredients": [
        "200 grams paneer", "1/2 cup thick curd", "2 tbsp gram flour",
        "ginger-garlic paste", "red chilli powder", "turmeric powder",
        "garam masala", "kasuri methi", "salt", "oil", "butter",
        "1 onion", "2 tomatoes", "12 cashews", "fresh cream", "water"
    ],
    "steps": [{"stepNumber": i+1, "instruction": s} for i, s in enumerate(paneer_steps)],
    "createdAt": datetime.datetime.utcnow()
}

db.collection("recipes").document("r1").set(paneer_recipe)
print("✔ Uploaded: Paneer Tikka Masala")


# ---------------------------------------------------------
# 3. SYNTHETIC 19 RECIPES
# ---------------------------------------------------------
synthetic_names = [
    "Veg Biryani", "Chicken Curry", "Masala Dosa", "Aloo Paratha", "Palak Paneer",
    "Chole Bhature", "Dal Makhani", "Fish Fry", "Egg Curry", "Idli Sambhar",
    "Paneer Butter Masala", "Mutton Rogan Josh", "Pav Bhaji", "Kadhai Paneer",
    "Rajma Chawal", "Gobi Manchurian", "Hyderabadi Biryani", "Veg Pulao", "Chicken Tikka"
]

generic_steps = [
    "Prepare all ingredients.",
    "Heat oil in pan.",
    "Add onions and sauté.",
    "Add spices and mix well.",
    "Add main ingredient and cook.",
    "Simmer for few minutes.",
    "Turn gas off and serve hot."
]

for i, name in enumerate(synthetic_names, start=2):
    step_count = random.randint(5, 7)
    steps = random.sample(generic_steps, step_count)

    recipe_doc = {
        "id": f"r{i}",
        "name": name,
        "category": name.split()[0],
        "difficulty": random.choice(["Easy", "Medium", "Hard"]),
        "cook_time": random.randint(20, 60),
        "ingredients": [f"Ingredient {j}" for j in range(1, random.randint(5, 10))],
        "steps": [{"stepNumber": k+1, "instruction": s} for k, s in enumerate(steps)],
        "createdAt": datetime.datetime.utcnow()
    }

    db.collection("recipes").document(f"r{i}").set(recipe_doc)
    print(f"✔ Uploaded synthetic recipe: {name}")


# ---------------------------------------------------------
# 4. USERS COLLECTION
# ---------------------------------------------------------
users = [
    {"id": "u1", "name": "Ayuresh Fendar", "email": "ayuresh@example.com"},
    {"id": "u2", "name": "Meera", "email": "meera@example.com"},
    {"id": "u3", "name": "Rohit", "email": "rohit@example.com"},
    {"id": "u4", "name": "Sana", "email": "sana@example.com"},
    {"id": "u5", "name": "Karan", "email": "karan@example.com"}
]

for u in users:
    db.collection("users").document(u["id"]).set(u)

print("✔ Users uploaded")


# ---------------------------------------------------------
# 5. USER_INTERACTION (ONLY 30 documents)
# ---------------------------------------------------------
for _ in range(30):

    recipe_id = f"r{random.randint(1, 20)}"
    user_id = f"u{random.randint(1, 5)}"

    number_of_views = random.randint(1, 20)
    number_of_likes = random.randint(0, 10)
    cook_attempts = random.randint(0, 5)

    rating_count = cook_attempts
    rating_total = sum(random.randint(1, 5) for __ in range(rating_count))
    avg_rating = round(rating_total / rating_count, 2) if rating_count else 0

    interaction_doc = {
        "userId": user_id,
        "recipeId": recipe_id,
        "timestamp": datetime.datetime.utcnow(),
        "number_of_views": number_of_views,
        "number_of_likes": number_of_likes,
        "cook_attempts": cook_attempts,
        "avg_rating": avg_rating
    }

    db.collection("user_interaction").add(interaction_doc)
print("🔥 Firestore Seeding Complete!")
