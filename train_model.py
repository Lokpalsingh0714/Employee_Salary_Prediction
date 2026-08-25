import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# 1. Read dataset
data = pd.read_csv("Salary_Data.csv")

# 2. Display first 5 rows
print(data.head())

# 3. Separate input and output
X = data[["YearsExperience"]]
y = data["Salary"]

# 4. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:", len(X_train))
print("Testing data:", len(X_test))

# 5. Create Linear Regression model
model = LinearRegression()

# 6. Train the model
model.fit(X_train, y_train)

# 7. Make predictions
predictions = model.predict(X_test)

print("Predictions:")
print(predictions)

# 8. Evaluate the model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# 9. Save trained model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")