# Asg-4-Pandas

**Purpose**
This project analyzes two datasets: Petal_Data and Sepal_Data. The code merges these datasets, converts string columns to numeric values, and calculates various statistical measures such as correlation, average, median, and standard deviation.

**Input**
Petal_Data.csv: A CSV file containing data related to petal measurements.
Sepal_Data.csv: A CSV file containing data related to sepal measurements.

**Output**
Combined DataFrame: The merged dataset contains both petal and sepal data.
Correlation Matrix: A matrix showing the correlation between different variables.
Average Values: The mean of each variable in the combined dataset.
Median Values: The median of each variable in the combined dataset.
Standard Deviation: The standard deviation of each variable in the combined dataset.

**Imported Libraries**
pandas: Used for data manipulation and analysis.

**Code process**
pd.read_csv: Reads CSV files into DataFrames.
pd.merge: Merges two DataFrames on specified columns.
pd.to_numeric: Converts string columns to numeric values, coercing errors to NaN.

.corr(): Calculates the correlation matrix.
.mean(): Calculates the mean of each variable.
.median(): Calculates the median of each variable.
.std(): Calculates the standard deviation of each variable.
print(): Displays the results.

**Limitations**
The code assumes that the CSV files are correctly formatted and contain the necessary columns (sample_id and species).
String columns that cannot be converted to numeric values will be set to NaN.
The code does not handle missing values or outliers.
