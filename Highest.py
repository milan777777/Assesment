import pandas as pd

file_path = '/Users/milangodar/Downloads/Expense.xlsx'
df = pd.read_excel(file_path)

print("Available columns:", df.columns)

column_name = "Goals"

if column_name in df.columns:
    highest = df[column_name].max()
    print(f"The highest value in {column_name} is: {highest}")
else:
    print(f"Error: Column '{column_name}' does not exist in the Excel file.")
