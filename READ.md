# 🍽️ Recipe Analytics Data Pipeline (Firebase-Based)

---

## 🎯 Goal
Design and implement a **data pipeline** using Firebase as the source system, processing:

- **Recipe data** 🍲  
- **User interactions** 👤  
- Generating **analytics insights** 📊  

This pipeline enables tracking, validation, and visualization of recipe performance metrics.

---

## 1️⃣ Data Modeling 🔹

The data model consists of **Recipes**, **Users**, and **User Interactions**. Each collection is structured with key attributes, types, and descriptions.

---

### 🥘 1.1 Recipes

| Field        | Type       | Description                                   | Example |
|-------------|-----------|-----------------------------------------------|---------|
| `id`        | string     | Unique recipe ID                               | `"r1"` |
| `name`      | string     | Recipe name                                    | `"Paneer Tikka Masala"` |
| `category`  | string     | Cuisine or category                            | `"Indian"` |
| `difficulty`| string     | Difficulty level (`Easy`, `Medium`, `Hard`)  | `"Medium"` |
| `cook_time` | integer    | Cooking time in minutes                        | `45` |
| `ingredients` | array    | List of ingredients                            | List of ingredients |
| `steps`     | array      | Step-by-step instructions                      | Step-by-step instructions  |
| `createdAt` | timestamp  | Recipe creation date/time                       | `"2025-11-20T12:42:34+05:30"` |

</details>

---

### 👤 1.2 Users

| Field      | Type   | Description            | Example |
|-----------|--------|------------------------|---------|
| `userId`  | string | Unique user ID         | `"u2"` |
| `name`    | string | User name              | `"Ayuresh"` |
| `email`   | string | Optional email         | `"ayuresh@example.com"` |

---

### 📊 1.3 User Interactions

Tracks **views, likes, cook attempts, and ratings** per recipe per user.

| Field             | Type      | Description                                                      | Example |
|------------------|-----------|------------------------------------------------------------------|---------|
| `userId`          | string    | Unique user ID                                                   | `"u2"` |
| `recipeId`        | string    | Reference to the recipe                                           | `"r16"` |
| `number_of_views` | integer   | Total recipe views                                               | `12` |
| `number_of_likes` | integer   | Total likes given                                                | `4` |
| `cook_attempts`   | integer   | Number of times the recipe was attempted                         | `5` |
| `avg_rating`      | float     | Average rating given (1–5)                                       | `3.8` |
| `timestamp`       | timestamp | Time when the interaction was recorded                            | `"2025-11-20T12:42:48+05:30"` |

<summary>Example Document</summary>

```json
{
  "userId": "u2",
  "recipeId": "r16",
  "number_of_views": 12,
  "number_of_likes": 4,
  "cook_attempts": 5,
  "avg_rating": 3.8,
  "timestamp": "2025-11-20T12:42:48+05:30"
}
```
---

## 2. Firebase Source Data Setup 🔹

1. Create collections in Firebase Firestore:
   - `recipes`
   - `users`
   - `interactions`
2. Insert your own recipe as the primary dataset.
3. Create **synthetic data**:
   - 15–20 recipes
   - 10–20 users
   - Sample interactions: views, likes, cook attempts, ratings
4. Example Firestore structure:









---

## 3. ETL / ELT Pipeline 🔹

### 3.1 Export Data
- Export Firestore collections to **JSON** or **CSV**:
  - `recipes.json`
  - `users.json`
  - `interactions.json`
- Example using Firebase CLI:
```bash
firebase firestore:export ./firestore-backup
