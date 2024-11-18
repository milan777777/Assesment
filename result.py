import pandas as pd

file_path = '/Users/milangodar/Downloads/Expense.xlsx'
sheet_name = "sheet2"
df = pd.read_excel(file_path)
print("Original Data:")
print(df)
sorted_df = df.sort_values(by='Name', ascending=True)

print("\nSorted Data:")
print(sorted_df)

sorted_df.to_excel('sorted_excel_file.xlsx', index=False)

print("\nSorted data saved to 'sorted_excel_file.xlsx'")
