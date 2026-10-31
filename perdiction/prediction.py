import joblib
import pandas as pd

# Load the trained model
model = joblib.load("salary_model.pkl")

# Load new test data (years of experience)
given_year = float(input("enter your experience in years:"))
test_data = pd.DataFrame({"Years": [given_year]})

# Predict salaries
predictions = model.predict(test_data)
print(predictions)

# Save predictions
test_data["PredictedSalary"] = predictions
test_data.to_csv("predicted_salaries.csv", index=False)

print("Predictions saved to predicted_salaries.csv")