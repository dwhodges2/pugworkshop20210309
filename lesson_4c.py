from sheetFeeder import dataSheet
import metapitools as met


sheet_id = '1K9UTydjBhHzwMjNh5xkk5qK1isKB8kdm5lflWVKJ3dE'
pug_sheet1 = dataSheet(sheet_id, 'Sheet1!A:Z')
pug_sheet2 = dataSheet(sheet_id, 'Sheet2!A:Z')


query1 = [['EXCLUDE?', '[Yy]']]

# x = pug_sheet2.matchingRows(query1)
x = pug_sheet2.getData(filter_queries=query1)
print(x)

quit()

# Retrieve the list of art objects from Sheet1.
# When getting by columns, the result is of form
# [[<col0 data>], [<col1 data>], ... ]
# The below gets just col 0 of Sheet1 as a list:
the_ids = pug_sheet1.getDataColumns()[0]

# Sort them numerically
the_ids = list(map(int, the_ids))
the_ids.sort()


# Create a new array the_data and populate it with the table heads.
heads = ['objectID', 'title', 'objectWikidata_URL', 'objectBeginDate', 'objectEndDate', 'primaryImageSmall', 'artistDisplayName', 'artistWikidata_URL',
         'objectName', 'medium', 'accessionYear', 'terms', 'EXCLUDE?']
the_data = [heads]

# Loop through ids and put specific elements into rows of data.
for id in the_ids:
    print(str(id))
    endpoint = 'objects/' + str(id)
    # Get the data from the API
    obj = met.get_item(id)
    # obj = met.api_requester(met.MET_BASE_URL, endpoint)
    # Compose into a list
    obj_info = [obj['objectID'], obj['title'], obj['objectWikidata_URL'],
                obj['objectBeginDate'], obj['objectEndDate'], obj['primaryImageSmall'],
                obj['artistDisplayName'], obj['artistWikidata_URL'],
                obj['objectName'], obj['medium'], obj['accessionYear'],
                met.parse_tags(obj['tags'])
                ]
    # Add the list as a row in array
    the_data.append(obj_info)

# Post the data to Sheet2
pug_sheet2.clear()
pug_sheet2.appendData(the_data)


quit()


pug_sheet3 = dataSheet(sheet_id, 'Sheet3!A:Z')
pug_sheet5 = dataSheet(sheet_id, 'Sheet5!A:Z')  # TEST


# met_query = 'search?dateBegin=1750&dateEnd=1800&q=animals'

# x = api_requester(met_base, met_query)

# the_ids = x['objectIDs']  # a list

# heads = ['objectID', 'title', 'objectWikidata_URL', 'objectBeginDate', 'objectEndDate', 'primaryImageSmall', 'artistDisplayName', 'artistWikidata_URL',
#          'objectName', 'medium', 'accessionYear', 'terms', 'EXCLUDE?']
# the_data = [heads]

# for id in the_ids:
#     print(str(id))
#     endpoint = 'objects/' + str(id)
#     # Get the data from the API
#     obj = api_requester(met_base, endpoint)
#     # Compose into a list
#     obj_info = [obj['objectID'], obj['title'], obj['objectWikidata_URL'],
#                 obj['objectBeginDate'], obj['objectEndDate'], obj['primaryImageSmall'],
#                 obj['artistDisplayName'], obj['artistWikidata_URL'],
#                 obj['objectName'], obj['medium'], obj['accessionYear'],
#                 get_tags(obj['tags'])
#                 ]
#     # Add the list as a row in array
#     the_data.append(obj_info)

# pug_sheet5.clear()
# pug_sheet5.appendData(the_data)

# quit()


quit()

query1 = [['EXCLUDE?', '[Yy]']]

# x = pug_sheet2.matchingRows(query1)
x = pug_sheet3.getData(filter_queries=query1)
print(x)
print('')

x = pug_sheet3.getData()
print(x)
print('')

x = pug_sheet3.getDataColumns()
print(x)
print('')

x = pug_sheet3.matchingRows(query1)
print(x)

quit()

# x = pug_sheet2.matchingRows([['title', 'sampler']])
# x = pug_sheet2.matchingRows([['EXCLUDE', 'Y']])
# x = pug_sheet2.getData()

# print(x)


# the_ids = x['objectIDs']  # a list

# pug_sheet1.clear()
# pug_sheet1.appendData(list_to_array(the_ids))


quit()


# print(pug_sheet.getData())

url = 'http://winterolympicsmedals.com/medals.csv'

pug_sheet1.importCSV(url)
# pug_sheet.importCSV('moma/artists.csv')
