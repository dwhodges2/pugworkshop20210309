from sheetFeeder import dataSheet
import pandas as pd
import pandas_functions as pf


# Test sheet with sample data
sheet_id = '19zHqOJt9XUGfrfzAXzOcr4uARgCGbyYiOtoaOCAMP7s'
sheet_range = 'Sheet1!A:Z'
the_sheet = dataSheet(sheet_id, sheet_range)

# 1. Data from sheetFeeder dataSheet
print("1. dataSheet data array:")
ds = the_sheet.getData()
print(ds)

print("")

# 2. Convert ds to df
df = pf.datasheet_to_dataframe(sheet_id, sheet_range)
print("2. Converted to DataFrame:")
print(df)
print("")
print("Some Pandas analysis...")
print("DataFrame shape:")
print(df.shape)
print("")
print("Data types:")
print(df.dtypes)
print("")
print("Column averages:")
print(df.mean())

print("")

# df back to ds
ds = pf.dataframe_to_datasheet(df)
print("3. Converted back to dataSheet array:")
print(ds)
