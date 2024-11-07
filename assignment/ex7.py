import pandas as pd

# Specify the file path
file_path = "D:\\python\\assignment\\Automobile_data.csv"

try:
    # Load the data
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Clean the dataset by replacing '?' and 'n.a' with NaN
    df.replace(['?', 'n.a'], pd.NA, inplace=True)

    # Convert the 'average-mileage' column to numeric, in case there are any non-numeric values
    df['average-mileage'] = pd.to_numeric(df['average-mileage'], errors='coerce')
    
    # Drop rows where 'average-mileage' is NaN
    df.dropna(subset=['average-mileage'], inplace=True)

    # Group by company and calculate the average mileage
    average_mileage_per_company = df.groupby('company')['average-mileage'].mean()

    # Print the result
    print("Average mileage per company:")
    print(average_mileage_per_company)

except Exception as e:
    print(f"An error occurred: {e}")
