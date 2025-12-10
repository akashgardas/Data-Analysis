import os
import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv


# Initialize Supabase client
def get_supabase_client():
    """Initialize and return Supabase client."""
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
   
    if not url or not key:
        raise ValueError("❌ Missing SUPABASE_URL or SUPABASE_KEY in .env")
       
    return create_client(url, key)

def validate(staged_path):
    # Convert to absolute path
    if not os.path.isabs(staged_path):
        staged_path = os.path.abspath(os.path.join(os.path.dirname(__file__), staged_path))
   
    print(f"🔍 Looking for data file at: {staged_path}")
   
    if not os.path.exists(staged_path):
        print(f"❌ Error: File not found at {staged_path}")
        print("ℹ️  Please run transform.py first to generate the transformed data")
        return
 
    try:
        # Initialize Supabase client
        supabase = get_supabase_client()
       
        # Read the CSV in chunks
        batch_size = 50  # Reduced batch size for better reliability
        df_original = pd.read_csv(staged_path)
        df_original = df_original[['tenure', 'monthlycharges', 'totalcharges', 'churn', 'internetservice', 'contract', 'paymentmethod', 'tenure_group', 'monthly_charge_segment', 'has_internet_service', 'is_multi_line_user', 'contract_type_code']]
        total_rows = len(df_original)
    
        # load supabase data
        data = supabase.table("telco_customer_churn_data").select("*").execute()
        df = pd.DataFrame(data.data)
        
        # Missing values
        print(df.isnull().sum())
        
        print(df.tenure_group.unique())
        
        # Unique count of rows
        if (len(df) == total_rows):
            print('Yes')
        else:
            print('No')
        
        # All segments exists
        print(df.columns)
        
        # Contract codes
        print(df.contract.unique())

    except Exception as e:
        print(f"❌ Error loading data: {e}")

if __name__ == "__main__":
    # Path relative to the script location
    staged_csv_path = os.path.join("..", "data", "staged", "churn_transformed.csv")
    validate(staged_csv_path)
    