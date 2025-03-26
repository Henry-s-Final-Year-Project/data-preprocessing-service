import joblib
import numpy as np
import json
import pandas as pd

# Load preprocessing artifacts
imputer = joblib.load("model_artifacts/geoloc_imputer.pkl")
encoder = joblib.load("model_artifacts/geoloc_encoder.pkl")

with open("model_artifacts/geolocation_fraud_feature_order.json") as f:
    feature_order = json.load(f)

binary_cols = ["vpn_usage", "proxy_usage", "is_new_device"]
categorical_cols = [
    "currency",
    "transaction_type",
    "country",
    "device_type",
    "operating_system",
    "app_version",
    "timezone",
    "ISP",
]
numeric_cols = [
    "amount",
    "avg_spend_30d",
    "transactions_last_7d",
    "time_since_last_login",
    "login_attempts_last_24h",
    "ip_risk_score",
    "latitude",
    "longitude",
]


def preprocess_transaction(tx_dict):
    # Step 1: Prepare numeric features
    numeric_df = pd.DataFrame([tx_dict], columns=numeric_cols)
    numeric_imputed = imputer.transform(numeric_df)

    # Step 2: Prepare categorical features (with missing filled)
    categorical_df = pd.DataFrame([tx_dict], columns=categorical_cols)
    categorical_df = categorical_df.fillna("missing")
    categorical_encoded = encoder.transform(categorical_df)

    # Step 3: Prepare binary features
    binary_data = np.array(
        [[tx_dict.get(col, 0) for col in binary_cols]], dtype=np.float32
    )

    # Step 4: Combine into single feature vector
    full_vector = np.concatenate(
        [numeric_imputed, categorical_encoded, binary_data], axis=1
    ).flatten()

    return full_vector.tolist()
