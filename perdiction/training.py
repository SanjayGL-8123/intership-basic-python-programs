import pandas as pd  # pip install pandas
import joblib  # pip install joblib
# pip install scikit-learn
from sklearn.linear_model import LinearRegression
# pip install scikit-learn

# Load dataset
data = pd.read_csv("data.csv")

# Split features and target
X = data[["Years"]]  # Independent variable
y = data["Salary"]   # Dependent variable

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
joblib.dump(model, "salary_model.pkl")

print("Model trained and saved as salary_model.pkl")