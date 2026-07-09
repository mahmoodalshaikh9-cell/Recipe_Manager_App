# 🍽️ The Recipe Address Book

A simple and interactive **Recipe Manager** built with **Python**, **Pandas**, and **Streamlit**. The application allows users to create, search, organize, rate, and randomly discover recipes while also generating shopping lists from recipe ingredients.

---

## 📖 Project Overview

The Recipe Address Book is designed to help users manage their personal recipe collection in one place. Users can add recipes, search recipes by ingredient, browse recipes by meal type, receive random recipe suggestions, rate recipes, and generate shopping lists.

The application stores recipe information in a CSV file, making it lightweight and easy to use without requiring a database.

---

## ✨ Features

### ➕ Add Recipes
Users can add recipes by entering:

- Recipe title
- Ingredients
- Preparation time
- Cooking instructions
- Difficulty level
- Meal type
- Default rating ("Not Rated")

The recipe is automatically saved into the application's dataset.

---

### 🔍 Search Recipes

Search recipes using any ingredient.

Example:

- chicken
- tomato
- rice
- garlic

Matching recipes are displayed instantly.

---

### 🍳 Browse Recipes

View recipes by meal category:

- Breakfast
- Lunch
- Dinner
- Dessert

Users can also view a quick summary showing recipe titles and preparation times.

---

### 🎲 Random Recipe Generator

Can't decide what to cook?

Click the **Generate Random** button to receive a random recipe suggestion from the collection.

---

### ⭐ Rate Recipes

Users can assign ratings to recipes.

Available ratings:

- ⭐ 1 Star
- ⭐⭐ 2 Stars
- ⭐⭐⭐ 3 Stars

Recipes are automatically updated and sorted according to their ratings.

---

### 🛒 Shopping List Generator

Select a recipe and automatically generate a shopping list containing all required ingredients using the helper function.

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Random Module
- CSV File Storage

---

## 📂 Project Structure

```
Recipe-Address-Book/
│
├── app.py                # Main Streamlit application
├── helper.py             # Shopping list helper functions
├── added.csv             # Recipe data storage
├── images.jpg            # Application image
├── README.md
└── requirements.txt
```

---

## 📊 Data Storage

Recipes are stored inside:

```
added.csv
```

Each recipe contains:

| Field | Description |
|---------|------------|
| Recipe title | Name of recipe |
| Ingredients | Ingredient list |
| Preparation time | Time in minutes |
| Instructions | Cooking instructions |
| Difficulty level | Easy / Medium / Hard |
| Meal time | Breakfast / Lunch / Dinner / Dessert |
| Rating | Recipe rating |

---

## 🚀 Live Application

Try the application here:

**https://recipemanagerapp-daydpt2bppzyceoepz7sra.streamlit.app/**

---

## 🎥 Video Demonstration

Watch the project demonstration here:

**https://youtu.be/x1QIcRY6FfQ**

---

## ▶️ Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/recipe-address-book.git
```

### 2. Navigate into the project

```bash
cd recipe-address-book
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 📦 Required Libraries

```text
streamlit
pandas
```

---

## 💡 How the Application Works

### Add Recipe

Users fill in the recipe form and submit it. The recipe is appended to the CSV file.

### Search

Users enter an ingredient and the application searches the stored recipes using Pandas string matching.

### View Recipes

Recipes can be filtered according to meal type using Streamlit buttons.

### Random Suggestion

A random recipe is selected using Pandas' sample() function.

### Rating

Users choose a recipe and assign a star rating.

### Shopping List

The helper function extracts ingredients for the selected recipe and displays them as a shopping list.

---

## 🎯 Learning Outcomes

This project demonstrates the use of:

- Interactive Streamlit interfaces
- Forms and user input
- DataFrames with Pandas
- Reading and writing CSV files
- Data filtering
- Random data selection
- Data persistence
- Modular programming using helper functions

---

## 🔮 Future Improvements

Potential enhancements include:

- User accounts and authentication
- Image uploads for recipes
- Recipe editing and deletion
- Recipe favorites
- Advanced search filters
- Nutritional information
- Cloud database integration
- Recipe sharing
- Ingredient quantity management
- Mobile-friendly interface

---

## 👨‍💻 Author

Developed as a Recipe Manager project using **Python**, **Pandas**, and **Streamlit**.

---