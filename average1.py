import pandas as pd

file_path = '/Users/milangodar/Downloads/Expense.xlsx'
df = pd.read_excel(file_path)
column_name = "Goals"
average = df[column_name].mean()
print(f"The average of {column_name} is: {average}")