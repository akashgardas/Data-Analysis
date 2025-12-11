# run_pipeline.py
"""
Orchestrates the full Air Quality ETL pipeline in order:
1) extract   -> pulls raw air quality data into data/raw/
2) transform -> flattens JSON + feature engineering into data/staged/
3) load      -> loads staged data into Supabase table air_quality_data
4) analysis  -> reads from Supabase, computes KPIs, exports CSVs & plots

Usage:
    python run_pipeline.py
"""

import time

from extract import fetch_all_cities
from transform import process_all_raw_files, save_transformed
from load import load_to_supabase
from etl_analysis import run_analysis


def run_full_pipeline():
    print("🟢 Step 1: Extract")
    fetch_all_cities()
    time.sleep(1)

    print("\n🟢 Step 2: Transform")
    df_transformed = process_all_raw_files()
    csv_path = save_transformed(df_transformed)
    print(f"Transformed data saved: {csv_path}")

    print("\n🟢 Step 3: Load")
    load_to_supabase()

    print("\n🟢 Step 4: Analysis")
    run_analysis()

    print("\n✅ Full ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_full_pipeline()