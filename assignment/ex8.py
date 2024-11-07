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

    # Sort by 'price' column in ascending order
    sorted_df_ascending = df.sort_values(by='price', ascending=True)

    # Print the result
    print("Cars sorted by price in ascending order:")
    print(sorted_df_ascending[['company', 'model', 'price']])

except Exception as e:
    print(f"An error occurred: {e}")
