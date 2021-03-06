from sheetFeeder import dataSheet
import pandas as pd
import pandas_functions as pf


sheet_id = '19zHqOJt9XUGfrfzAXzOcr4uARgCGbyYiOtoaOCAMP7s'
sheet_range = 'Pandas!A:Z'
the_sheet = dataSheet(sheet_id, sheet_range)

# Put some sample data in the sheet
data1 = [['Col A', 'Col B', 'Col C', 'Col D'], [1.0, 2.0, 3.0, 4.0],
         [5.0, 6.0, 7.0, 8.0], [0.0, 11.5, -5.0, 9.25]]

the_sheet.clear()
the_sheet.appendData(data1)

# 1. Get the data from the sheet (this is redundant, but just for demo purposes!)
ds = the_sheet.getData()

# 2. Convert to Pandas DataFrame
df = pf.datasheet_to_dataframe(sheet_id, sheet_range)

print(df)

print("")

# Add a column calculating the averages of each row
df['Average'] = df.mean(numeric_only=True, axis=1)
print(df)

# Convert back into array
data2 = pf.dataframe_to_datasheet(df)

# Post back to sheet, replacing data
the_sheet.clear()
the_sheet.appendData(data2)
# quit()

print("")
