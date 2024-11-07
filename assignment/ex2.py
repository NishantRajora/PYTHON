import pandas as pd
import numpy as np

# Specify the file path
file_path = "D:\\python\\assignment\\Automobile_data.csv"

try:
    # Load the data
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Replace '?', 'n.a' and 'NaN' with NaN
    df.replace(['?', 'n.a'], np.nan, inplace=True)

    # Optionally, you can fill NaN with a placeholder value or forward fill/backward fill
    # Example: Filling NaN with the mean of the respective columns (for numerical columns)
    df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill NaN in numerical columns with mean
    df.fillna("Unknown", inplace=True)  # Fill NaN in non-numeric columns with "Unknown"

    # Save the cleaned data to the same CSV file or a new one
    df.to_csv(file_path, index=False, encoding='ISO-8859-1')

    # Print the first and last few rows to check the cleaning process
    print("First five rows after cleaning:")
    print(df.head())
    
    print("\nLast five rows after cleaning:")
    print(df.tail())

except Exception as e:
    print(f"An error occurred: {e}")
