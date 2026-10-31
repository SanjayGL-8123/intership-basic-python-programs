# Food Nutrition & Benefits Lookup (`foodRecommandation.py`)

A Pandas-powered data lookup tool that reads a CSV dataset of foods, queries dietary benefits and demerits, and outputs recommendations.

---

## 📋 Overview

Loads nutritional data from `food_data.csv`, prompts the user to enter a food item (e.g., Apple, Banana, Spinach), matches the query against the dataset, and displays the corresponding health benefits and drawbacks.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x (Tested on Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install pandas
  ```
  *(Status: **Installed** ✅ `pandas==2.3.3`)*
- **Required Data File:** `food_data.csv` must be in the same folder.

---

## 🚀 How to Run

```powershell
python foodRecommandation.py
```

---

## 🔍 Code Breakdown

```python
import pandas as pd

# Load data from CSV
df = pd.read_csv("food_data.csv")

def display_food_info(food_item):
    # Check if the food item exists in the DataFrame
    if food_item in df["Food Item"].values:
        row = df[df["Food Item"] == food_item].iloc[0]
        print(f"Food Item: {row['Food Item']}")
        print(f"Benefits: {row['Benefits']}")
        print(f"Demerits: {row['Demerits']}")
    else:
        print("Food item not found!")

food_item = input("Enter a food item: ")
display_food_info(food_item)
```

### Key Concepts:
- `pd.read_csv("food_data.csv")`: Parses the tabular comma-separated values file into a structured Pandas DataFrame.
- `df["Food Item"].values`: Returns an array of available food entries for existence checking.
- `df[df["Food Item"] == food_item].iloc[0]`: Filters rows matching the query string and extracts the first matching record.

---

## 💡 Example Run

```text
Enter a food item: Apple
Food Item: Apple
Benefits: Rich in fiber and vitamin C, supports gut health
Demerits: High sugar content if consumed in excess
```
