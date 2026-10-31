import pandas as pd

# pip install pandas
# Load data from CSV
df = pd.read_csv("food_data.csv")


# Function to display benefits and demerits based on food item
def display_food_info(food_item):
    # Check if the food item exists in the DataFrame
    if food_item in df["Food Item"].values:
        row = df[df["Food Item"] == food_item].iloc[0]
        print(f"Food Item: {row['Food Item']}")
        print(f"Benefits: {row['Benefits']}")
        print(f"Demerits: {row['Demerits']}")
    else:
        print("Food item not found!")


# Example usage
food_item = input("Enter a food item: ")
display_food_info(food_item)