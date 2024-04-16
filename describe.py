import pandas as pd

# Load the dataset
df = pd.read_csv('dataset_file.csv')
# Basic statistics
print(df.describe())