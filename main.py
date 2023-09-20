import pandas as pd

file_path = '/Users/methsara/Downloads/MDT 20230817/Huawei MDT.csv'

try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, encoding='utf-8')

    # Display the DataFrame
    print(df)

except Exception as e:
    print(f"An error occurred: {str(e)}")

print(f"File path: {file_path}")
