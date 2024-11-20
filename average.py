import pandas as pd

file_path = '/Users/milangodar/Downloads/Expense.xlsx'
df = pd.read_excel(file_path)

print("Available columns:", df.columns)

column_name = "Goals"

if column_name in df.columns:
    average = df[column_name].mean()
    print(f"The average of {column_name} is: {average}")
else:
    print(f"Error: Column '{column_name}' does not exist in the Excel file.")
