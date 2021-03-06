from sheetFeeder import dataSheet
import metapitools as met


sheet_id = '1K9UTydjBhHzwMjNh5xkk5qK1isKB8kdm5lflWVKJ3dE'
pug_sheet1 = dataSheet(sheet_id, 'Sheet1!A:Z')
pug_sheet2 = dataSheet(sheet_id, 'Sheet2!A:Z')


# Retrieve the list of art objects from Sheet1.
# When getting by columns, the result is of form
# [[<col0 data>], [<col1 data>], ... ]
# The below gets just col 0 of Sheet1 as a list:
the_ids = pug_sheet1.getDataColumns()[0]

# Sort them numerically
the_ids = list(map(int, the_ids))
the_ids.sort()

print(the_ids)
