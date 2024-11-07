import pandas as pd

# Specify the file path
file_path = "D:\\python\\assignment\\Automobile_data.csv"

try:
    # Load the data
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Clean the dataset by replacing '?' and 'n.a' with NaN
    df.replace(['?', 'n.a'], pd.NA, inplace=True)

    # Convert the 'price' column to numeric, in case there are any non-numeric values
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # Drop rows where 'price' is NaN
    df.dropna(subset=['price'], inplace=True)

    # Find the row with the highest price for each company
    highest_price_per_company = df.loc[df.groupby('company')['price'].idxmax()]

    # Print the result (Company name, Highest priced car, and price)
    print("Highest price car for each company:")
    print(highest_price_per_company[['company', 'price']])

except Exception as e:
    print(f"An error occurred: {e}")

