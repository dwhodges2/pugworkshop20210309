from sheetFeeder import dataSheet

# Replace with the UID of your sheet.
sheet_id = 'xxxxxxxxxxxxxxxxx'
sheet_id = '1uJZ5eqjrqdzs0P_8tvePIK4MGn0a9_RGmJtBda_KrOs'

test_sheet = dataSheet(sheet_id, 'Sheet1!A:Z')

print("Getting data from the sheet...")
x = test_sheet.getData()
print(x)

print("")
print("Getting data as columns...")
x = test_sheet.getDataColumns()
print(x)

print("")
print("Append some data ...")
new_data = [['x', 'y', 'z'], [12, '', 'Hello'], ['055', 34, 'c']]
x = test_sheet.appendData(new_data)
print(x)

print("")
print("The new data looks like...")
x = test_sheet.getData()
print(x)
