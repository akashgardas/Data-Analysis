# ===========================
# transform.py
# ===========================
 
import os
import pandas as pd
import numpy as np
 
# Purpose: Clean and transform Titanic dataset
def transform_data(raw_path):
    # Ensure the path is relative to project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # go up one level
    staged_dir = os.path.join(base_dir, "data", "staged")
    os.makedirs(staged_dir, exist_ok=True)
 
    df = pd.read_csv(raw_path)
 
    # --- 1️⃣ Data Cleaning ---
    # map spaces to NaN
    df['TotalCharges'] = df['TotalCharges'].replace(r'\s+', np.nan, regex=True)
    # data type conversion
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])
    
    # tenure - median value
    df['tenure'] = df['tenure'].fillna(df['tenure'].median())
    # MonthlyCharges - median value
    df['MonthlyCharges'] = df['MonthlyCharges'].fillna(df['MonthlyCharges'].median())
    # TotalCharges - median value
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
    
    # Categorical values - fill with UNKNOWN
    df['SeniorCitizen'] = df['SeniorCitizen'].fillna('UNKNOWN')
    
    # --- 2️⃣ Feature Engineering ---
    # tenure_group
    df['tenure_group'] = pd.cut(df['tenure'], bins=[-1, 12, 36, 60, 100], labels=['New', 'Regular', 'Loyal', 'Champion'])

    # monthly_charge_segment
    df['monthly_charge_segment'] = pd.cut(df['MonthlyCharges'], bins=[0, 30, 70, np.inf], labels=['Low', 'Med', 'High'])
    
    # has_internet_service
    df['has_internet_service'] = np.where((df['InternetService'] == 'DSL') | (df['InternetService'] == 'Fiber optic'), 1, 0)
    
    # is_multi_line_user
    df['is_multi_line_user'] = np.where(df['MultipleLines'] == 'Yes', 1, 0)
    
    # contact_type_code
    df['contract_type_code'] = df['Contract'].map({
        'Month-to-month': 0,
        'One year': 1,
        'Two year': 2
    })
    
    # --- 3️⃣ Dropping Unneccessary fields
    # customerID, gender
    df.drop(['customerID', 'gender'], axis=1, inplace=True)
    
    # --- 4️⃣ Save transformed data ---
    staged_path = os.path.join(staged_dir, "churn_transformed.csv")
    df.to_csv(staged_path, index=False)
    print(f"✅ Data transformed and saved at: {staged_path}")
    return staged_path
 
 
if __name__ == "__main__":
    from extract import extract_data
    raw_path = extract_data()
    transform_data(raw_path)
 