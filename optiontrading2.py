import sys
import pandas as pd
import requests
import pickle
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor

# Function to download and load the model, scaler, and imputer
def load_model():
    model_url = "https://raw.githubusercontent.com/ZaGrayWolf/QUANT-Predict-Closing-Auction-Volume/main/trained_nn_model.pkl"
    scaler_url = "https://raw.githubusercontent.com/ZaGrayWolf/QUANT-Predict-Closing-Auction-Volume/main/scaler.pkl"
    imputer_url = "https://raw.githubusercontent.com/ZaGrayWolf/QUANT-Predict-Closing-Auction-Volume/main/imputer.pkl"

    model = pickle.loads(requests.get(model_url).content)
    scaler = pickle.loads(requests.get(scaler_url).content)
    imputer = pickle.loads(requests.get(imputer_url).content)

    return model, scaler, imputer

# Function to preprocess input data
def preprocess_input_data(input_data, scaler, imputer):
    # Drop columns that are not needed for prediction
    input_data_cleaned = input_data.drop(columns=['close_volume', 'date_id', 'symbol_id'], errors='ignore')
    input_data_imputed = imputer.transform(input_data_cleaned)
    input_data_scaled = scaler.transform(input_data_imputed)
    return input_data_scaled

# Function to predict close volume
def predict_close_volume(input_file, model, scaler, imputer):
    input_data = pd.read_csv(input_file)
    input_data_scaled = preprocess_input_data(input_data, scaler, imputer)
    predictions = model.predict(input_data_scaled)
    return predictions

def main():
    # Load the models, scaler, and imputer
    mlp_model, scaler, imputer = load_model()

    # Read input file path from stdin
    input_file = sys.stdin.read().strip()

    # Output predictions
    predictions = predict_close_volume(input_file, mlp_model, scaler, imputer)
    print(predictions)

if __name__ == "__main__":
    main()
