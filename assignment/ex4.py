import pandas as pd

# Specify the file path
file_path = "D:\\python\\assignment\\Automobile_data.csv"

try:
    # Load the data
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Clean the dataset by replacing '?' and 'n.a' with NaN
    df.replace(['?', 'n.a'], pd.NA, inplace=True)

    # Filter the rows where 'company' is 'toyota'
    toyota_cars = df[df['company'] == 'toyota']

    # Print the details of all Toyota cars
    print("Details of all Toyota cars:")
    print(toyota_cars)

except Exception as e:
    print(f"An error occurred: {e}")
