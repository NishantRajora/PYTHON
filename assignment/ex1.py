import pandas as pd

# Specify the file path
file_path = "D:\\python\\assignment\\Automobile_data.csv"

try:
    # Load the data and display the first and last five rows
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Display the first and last five rows separately if needed
    first_five = df.head()
    last_five = df.tail()
    
    print("First five rows:")
    print(first_five)
    
    print("\nLast five rows:")
    print(last_five)

except Exception as e:
    print(f"An error occurred: {e}")
