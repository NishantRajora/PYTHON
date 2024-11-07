import pandas as pd

# Create the GermanCars and JapaneseCars dictionaries
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
JapaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}

# Create dataframes from the dictionaries
df_german = pd.DataFrame(GermanCars)
df_japanese = pd.DataFrame(JapaneseCars)

# Concatenate the two dataframes vertically (by rows)
df_concatenated = pd.concat([df_german, df_japanese], ignore_index=True)

# Print the concatenated dataframe
print(df_concatenated)
