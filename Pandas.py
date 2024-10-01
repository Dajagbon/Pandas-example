import pandas as pd

# Import Petal_Data from CSV
Petal_Data = pd.read_csv('C:/Users/danie/Downloads/Pythonclasstwo/Petal_Data.csv')

# Import Sepal_Data from CSV
Sepal_Data = pd.read_csv('C:/Users/danie/Downloads/Pythonclasstwo/Sepal_Data.csv')

# Merge the datasets
combined_data = pd.merge(Petal_Data, Sepal_Data, on=['sample_id', 'species'])

# Convert all string columns to float
for col in combined_data.columns:
    if combined_data[col].dtype == 'object':
        combined_data[col] = pd.to_numeric(combined_data[col], errors='coerce')

# Calculate the correlation matrix
correlation_matrix = combined_data.corr()

# Calculate the average of each variable
average_values = combined_data.mean()

# Calculate the median of each variable
median_values = combined_data.median()

# Calculate the standard deviation of each variable
std_deviation = combined_data.std()

# Display the results
print("Combined DataFrame:\n", combined_data)
print("\nCorrelation Matrix:\n", correlation_matrix)
print("\nAverage Values:\n", average_values)
print("\nMedian Values:\n", median_values)
print("\nStandard Deviation:\n", std_deviation)
