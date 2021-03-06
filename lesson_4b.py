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
