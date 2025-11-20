# 🍽️ Recipe Analysis Data Pipeline (Firebase-Based)

## 🎯 Goal
Design and implement a **data pipeline** using Firebase as the source system to:

- Track **recipe data** 🍲  
- Monitor **user interactions** 👤  
- Generate **analytics insights** 📊  

This pipeline supports **data validation, ETL, and visualization** of recipe performance metrics.

---

## 1️⃣ Data Modeling 🔹

The data model includes **recipes**, **users**, and **user_interactions** collections.  

<details>
<summary>Click to expand: Schema Overview</summary>

### 🥘 Recipes

| Field        | Type       | Description | Example |
|-------------|-----------|-------------|---------|
| `id`        | string     | Unique recipe ID | `"r1"` |
| `name`      | string     | Recipe name | `"Paneer Tikka Masala"` |
| `category`  | string     | Cuisine/category | `"Indian"` |
| `difficulty`| string     | Difficulty (`Easy`, `Medium`, `Hard`) | `"Medium"` |
| `cook_time` | integer    | Cooking time in minutes | `45` |
| `ingredients` | array    | List of ingredients | `[{"name": "Paneer", "qty": 200, "unit": "grams"}, ...]` |
| `steps`     | array      | Step-by-step instructions | `["Marinate paneer", "Fry cubes", ...]` |
| `createdAt` | timestamp  | Recipe creation datetime | `"2025-11-20T12:42:34+05:30"` |

### 👤 Users

| Field      | Type   | Description | Example |
|-----------|--------|-------------|---------|
| `userId`  | string | Unique user ID | `"u2"` |
| `name`    | string | User name | `"Ayuresh"` |
| `email`   | string | Optional email | `"ayuresh@example.com"` |

### 📊 User Interactions

Tracks **views, likes, cook attempts, and ratings**.

| Field             | Type      | Description | Example |
|------------------|-----------|-------------|---------|
| `userId`          | string    | User reference | `"u2"` |
| `recipeId`        | string    | Recipe reference | `"r16"` |
| `number_of_views` | integer   | Total views | `12` |
| `number_of_likes` | integer   | Total likes | `4` |
| `cook_attempts`   | integer   | Number of cook attempts | `5` |
| `avg_rating`      | float     | Average rating (1–5) | `3.8` |
| `timestamp`       | timestamp | Interaction datetime | `"2025-11-20T12:42:48+05:30"` |

</details>

---

## 2️⃣ Firebase Source Data Setup 🔹

- **Collections**: `recipes`, `users`, `interactions`  
- **Primary dataset**: Candidate’s own recipe  
- **Synthetic data**: 15–20 recipes, 10–20 users, sample interactions  
- **Firestore hierarchy example**:


---

## 3️⃣ ETL / ELT Pipeline 🔄

- Export Firestore collections → JSON/CSV  
- Transform into **normalized tables**:


- Implement in **Python** or **Node.js**  
- Ensure **data consistency** & **schema validation**
- **Output**:
```
ingredients.csv
interaction.csv
recipe.csv
steps.csv
```

---

## 4️⃣ Data Quality Validation ✅

- Rules:
  - Required fields present
  - Positive numeric values
  - Non-empty arrays
  - Valid difficulty values (`Easy`, `Medium`, `Hard`)
- **Validation Output**:
```
validation_summary.csv
```


> Dataset validated successfully ✔️

---

## 5️⃣ Analytics Insights 📊

Dynamic insights with visual separation and icons for clarity.

---

### 5.1 Most Common Ingredients 🥬
![Ingredients Chart](images/1.png)

| Ingredient             | Count |
|------------------------|-------|
| 200 grams paneer       | 1     |
| 1/2 cup thick curd     | 1     |
| 2 tbsp gram flour      | 1     |
| ginger-garlic paste    | 1     |
| red chilli powder      | 1     |
| turmeric powder        | 1     |
| garam masala           | 1     |
| kasuri methi           | 1     |
| salt                   | 1     |
| oil                    | 1     |

---

### 5.2 Average Preparation Time ⏱️
![Prep Time Chart](output/2.png)  
**42.45 minutes**

---

### 5.3 Difficulty Distribution 🎚️
![Difficulty Chart](output/3.png)

| Difficulty | Count |
|------------|-------|
| Medium     | 9     |
| Hard       | 6     |
| Easy       | 5     |

---

### 5.4 Most Frequently Viewed Recipes 👀
![Views Chart](output/4.png)

| Recipe Name             | Views |
|-------------------------|-------|
| Mutton Rogan Josh       | 68    |
| Veg Pulao               | 56    |
| Fish Fry                | 33    |
| Chicken Curry           | 31    |
| Chole Bhature           | 28    |
| Palak Paneer            | 23    |
| Egg Curry               | 18    |
| Paneer Butter Masala    | 17    |
| Hyderabadi Biryani      | 16    |
| Rajma Chawal            | 12    |

---

### 5.5 Recipes with Highest Average Likes ❤️
![Likes Chart](output/5.png)

| Recipe Name             | Avg Likes |
|-------------------------|-----------|
| Idli Sambhar            | 9.0       |
| Chole Bhature           | 7.5       |
| Masala Dosa             | 6.0       |
| Fish Fry                | 5.67      |
| Hyderabadi Biryani      | 5.0       |
| Dal Makhani             | 5.0       |
| Veg Pulao               | 5.0       |
| Veg Biryani             | 5.0       |
| Pav Bhaji               | 4.0       |
| Aloo Paratha            | 4.0       |

---

### 5.6 Recipes with Highest Cook Attempts 👩‍🍳
![Cook Attempts Chart](output/6.png)

| Recipe Name             | Cook Attempts |
|-------------------------|---------------|
| Veg Biryani             | 5.0           |
| Rajma Chawal            | 5.0           |
| Paneer Tikka Masala     | 4.0           |
| Pav Bhaji               | 4.0           |
| Chole Bhature           | 4.0           |
| Palak Paneer            | 4.0           |
| Masala Dosa             | 3.0           |
| Dal Makhani             | 3.0           |
| Mutton Rogan Josh       | 2.75          |
| Idli Sambhar            | 2.0           |

---

### 5.7 Correlation between Prep Time & Likes 📈
![Correlation Chart](output/7.png)  
**0.242** → small positive correlation

---

### 5.8 Top Rated Recipes ⭐
![Ratings Chart](output/8.png)

| Recipe Name             | Avg Rating |
|-------------------------|------------|
| Kadhai Paneer           | 5.0        |
| Dal Makhani             | 4.0        |
| Egg Curry               | 4.0        |
| Rajma Chawal            | 3.8        |
| Fish Fry                | 3.67       |
| Paneer Tikka Masala     | 2.75       |
| Chole Bhature           | 2.665      |
| Paneer Butter Masala    | 2.5        |
| Masala Dosa             | 2.33       |
| Palak Paneer            | 2.265      |

---

### 5.9 Ingredients with Highest Engagement 💬
![Ingredient Engagement](output/9.png)

| Ingredient             | Avg Likes |
|------------------------|-----------|
| 1 onion                | 0.0       |
| 1/2 cup thick curd     | 0.0       |
| 12 cashews             | 0.0       |
| 2 tbsp gram flour      | 0.0       |
| 2 tomatoes             | 0.0       |
| 200 grams paneer       | 0.0       |
| butter                 | 0.0       |
| fresh cream            | 0.0       |
| garam masala           | 0.0       |
| ginger-garlic paste    | 0.0       |

---

### 5.10 Average Likes by Difficulty 🎚️
![Difficulty Likes](output/10.png)

| Difficulty | Avg Likes |
|------------|-----------|
| Easy       | 4.2       |
| Hard       | 4.91      |
| Medium     | 3.78      |
