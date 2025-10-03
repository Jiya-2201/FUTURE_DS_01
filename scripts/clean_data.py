# clean_data.py

import pandas as pd
import os

def clean_retail_data(input_path="data/raw/online_retail_ii.xlsx", 
                      output_path="data/processed/cleaned_retail.csv"):
    """
    Load, clean, and save the Online Retail dataset.
    """

    # Load dataset
    print("📥 Loading dataset...")
    df = pd.read_excel(input_path)

    # Show initial shape
    print(f"Initial dataset shape: {df.shape}")

    # Drop rows with missing Customer ID
    df = df.dropna(subset=["Customer ID"])

    # Remove negative or zero quantities and prices
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    print(f"✅ Cleaned dataset saved at: {output_path}")
    print(f"Final dataset shape: {df.shape}")


if __name__ == "__main__":
    clean_retail_data()
