from sheetFeeder import dataSheet
import metapitools as met


sheet_id = '1K9UTydjBhHzwMjNh5xkk5qK1isKB8kdm5lflWVKJ3dE'
pug_sheet1 = dataSheet(sheet_id, 'Sheet1!A:Z')
pug_sheet2 = dataSheet(sheet_id, 'Sheet2!A:Z')


query1 = [['EXCLUDE?', '[Yy]']]

# x = pug_sheet2.matchingRows(query1)
x = pug_sheet2.getData(filter_queries=query1)
print(x)
