import pandas as pd

file_path = "portfolio.dat"
column_names = ['Stock Name', 'Amount', 'Single Share Price']
df = pd.read_csv(file_path, sep=" ", header=None, names=column_names)
df['Total'] = df['Amount'] * df['Single Share Price']
amount = df['Total'].sum()
print(f"Total Amount needed to buy all stocks: ${amount:,.2f}")