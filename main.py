import csv
from tabulate import tabulate

file_path = '/Users/methsara/Downloads/MDT 20230817/Huawei MDT.csv'

try:
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Read and display the first 10 rows as a sample
        data = [row for i, row in enumerate(csv_reader) if i < 10]

        if data:
            print(tabulate(data, headers="firstrow", tablefmt="grid"))
        else:
            print("No data found in the CSV file.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

print(f"File path: {file_path}")
