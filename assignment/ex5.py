import pandas as pd

# Specify the file path
file_path = "D:\\python\\assignment\\Automobile_data.csv"

try:
    # Load the data
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Clean the dataset by replacing '?' and 'n.a' with NaN
    df.replace(['?', 'n.a'], pd.NA, inplace=True)

    # Count the total cars per company
    cars_per_company = df.groupby('company').size()

    # Print the total cars per company
    print("Total cars per company:")
    print(cars_per_company)

except Exception as e:
    print(f"An error occurred: {e}")
