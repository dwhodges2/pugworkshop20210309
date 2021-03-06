# Curating a Virtual Gallery the Met Museum Database

We will be working with data about art objects in the Met's collections, as obtained through the [Met API](https://metmuseum.github.io/), a freely available resource with a fairly straightforward interface.

To make things easier, a set of functions for forming requests to the Met API is included as `meapitools.py`, and are incorporated like this:

```python
import metapitools as met
```

## 1. Retrieve a list of object IDs from a sheet

"Sheet1" of [this spreadsheet](https://docs.google.com/spreadsheets/d/1K9UTydjBhHzwMjNh5xkk5qK1isKB8kdm5lflWVKJ3dE/edit?usp=sharing) contains a list of artworks that purportedly relate to *animals*. We will use this to build a data set and do some refinement in Google Sheets and Python.

After defining a `dataSheet` for Sheet1, the script `lesson_4a.py` retrieves the the data to get a list of IDs:

```python
the_ids = pug_sheet1.getDataColumns()[0]

# Sort them numerically
the_ids = list(map(int, the_ids))
the_ids.sort()

print(the_ids)
```

The data has two columns, so our code uses the `getDataColumns()` method and makes column 0 into our list. (Remember that in most Python contexts indexing starts with 0, not 1.) Now we have a sorted list of IDs to work with!

## 2. Build a data set from the IDs

Script `lesson_4b.py` uses the API request functions from `metapitools` to take each ID and pull down a `dict` of data. You can see an example JSON output for object 10771 in a browser here:

https://collectionapi.metmuseum.org/public/collection/v1/objects/10771

The script extracts only some elements as shown in the heads:

```python
heads = ['objectID', 'title', 'objectWikidata_URL', 'objectBeginDate', 'objectEndDate', 'primaryImageSmall', 'artistDisplayName', 'artistWikidata_URL',
         'objectName', 'medium', 'accessionYear', 'terms', 'EXCLUDE?']
```

(We are adding the "EXCLUDE?" column at the end for the next step.) The script iterates through each object and composes a row of the data. When done it posts the list of rows to Sheet2 of the spreadsheet.

To try it for yourself do this:

1. Create a new Google Sheet document. Note the UID of the document.
2. Copy the contents of Sheet1 to your Sheet1.
3. Create another tab called Sheet2.
4. Modify `lesson_4b.py` to have your document's UID in the `sheet_id` variable.
5. Run `lesson_4b.py`. After a minute or so you should see a full table appear in Sheet2.

## 3. Curate the Collection

All of these objects purport to be related to *animals*. Let's curate the list so we are only showing ones that have animal themes. This would exclude things made out of animal parts (e.g., ivory), or have no apparent relation to animals (perhaps there were mis-cataloged in the Met's database). To do this we will put a "Y" in the EXCLUDE? column.

This could form the data for data visualizations or online exhibits. I created this page in Google Data Studio that uses this data to show the contents of our collection:

https://datastudio.google.com/reporting/5c594c39-f214-4b11-b2fc-02334151087e/page/sYD4B

Note that ones marked to be Excluded should not appear!

We could use `sheetFeeder` to obtain a filtered list that based on our exclusions. `The getData()` method provides a filtering option. To get only the excluded rows (say, to make a report of corrections to remove animal tagging), you could use:

```python
the_sheet.getData()
query1 = [['EXCLUDE?', '[Yy]']]
x = pug_sheet2.getData(filter_queries=query1)
print(x)
```

The query syntax is of the form 

```python
[[<col_name1>, <pattern1>], [<col_name2>, <pattern2>] ... ]
```

By default the pattern is a regular expression (regex), but this can be disabled. The pattern above matches either upper or lowercase Y wherever it is in the EXCLUDE? column.

[<<< Previous](Lesson_3.md) 