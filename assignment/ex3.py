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

    # Find the row with the maximum price
    most_expensive_row = df.loc[df['price'].idxmax()]

    # Extract the car company name and price of the most expensive car
    most_expensive_car_company = most_expensive_row['company']
    most_expensive_car_price = most_expensive_row['price']

    # Print the result
    print(f"The most expensive car company is: {most_expensive_car_company}")
    print(f"The price of the most expensive car is: {most_expensive_car_price}")

except Exception as e:
    print(f"An error occurred: {e}")
