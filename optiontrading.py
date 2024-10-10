#!/bin/python3

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import sys
from io import StringIO

# Placeholder for training data - replace this with actual training data as needed
dummy_train_data = {
    'Id': ['Dummy1', 'Dummy2'],
    'OptionType': ['Call', 'Put'],
    'Strike': [60, 120],
    'Spot': [148.1797401, 148.5581572],
    'TimeToExpiry': [1.243255425, 0.944953829],
    'RiskfreeRate': [3.1980597, 0.027206587],
    'MarketFearIndex': [6.436489684, 71.28559419],
    'BuySellRatio': [1.068700429, 0.487120444],
    'OptionPrice': [1, 2.877918997]  # Example option prices
}

# Create a DataFrame for training
train_data = pd.DataFrame(dummy_train_data)

# Separate features and target variable from the training data
X_train = train_data.drop(columns=['Id', 'OptionPrice'])
y_train = train_data['OptionPrice']

# Define categorical and numerical features
categorical_features = ['OptionType']
numerical_features = ['Strike', 'Spot', 'TimeToExpiry', 'RiskfreeRate', 'MarketFearIndex', 'BuySellRatio']

# Preprocessing: OneHotEncode categorical features, Standardize numerical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Build the pipeline with preprocessing and RandomForestRegressor
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train the model with the dummy training data
model.fit(X_train, y_train)

# Read the input CSV data directly from stdin
input_data = sys.stdin.read().strip()

# Replace escaped newline with an actual newline character
input_data = input_data.replace('\\n', '\n')

# Use StringIO to treat the string as a file object
test_data = pd.read_csv(StringIO(input_data))

# Clean column names to ensure no extra whitespace or special characters
test_data.columns = test_data.columns.str.strip()

# Check for missing columns
missing_columns = set(numerical_features + categorical_features) - set(test_data.columns)
if missing_columns:
    print(f"Warning: Missing columns in test data: {missing_columns}")
    sys.exit()

# Prepare the test data
X_test = test_data.drop(columns=['Id'])  # Drop the 'Id' column for predictions

# Ensure columns are in the correct order (match training data)
X_test = X_test[numerical_features + categorical_features]

# Check if the test set is empty before prediction
if X_test.empty:
    print("Error: X_test is empty. Please check the test data.")
    sys.exit()

# Predict the option prices for the test set
y_pred = model.predict(X_test)

# Create the output DataFrame with Id and predicted OptionPrice
output = pd.DataFrame({'Id': test_data['Id'], 'OptionPrice': y_pred})

# Ensure that the output is formatted exactly as requested
formatted_output = output.to_csv(index=False, header=True).strip()

# Print the exact formatted output
print(formatted_output)