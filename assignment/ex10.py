import pandas as pd

# Create the Car_Price and car_Horsepower dictionaries
Car_Price = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'horsepower': [141, 80, 182, 160]}

# Create dataframes from the dictionaries
df_price = pd.DataFrame(Car_Price)
df_horsepower = pd.DataFrame(car_Horsepower)

# Merge the two dataframes on the 'Company' column
df_merged = pd.merge(df_price, df_horsepower, on='Company')

# Print the merged dataframe
print(df_merged)
