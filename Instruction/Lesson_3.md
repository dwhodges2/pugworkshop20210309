# Using Data from the Met Museum Database

We will be working with data about art objects in the Met's collections, as obtained through the  [Met API](https://metmuseum.github.io/), a freely available resource with a fairly straightforward interface.

## 1. Retrieve a list of object IDs from a sheet

A sheet contains a list of 18th century artworks that purportedly relate to animals. We will use this to build a data set and do some refinement in Google Sheets and Python.

You can see the list here, in Sheet1 of this document:

https://docs.google.com/spreadsheets/d/1K9UTydjBhHzwMjNh5xkk5qK1isKB8kdm5lflWVKJ3dE/edit?usp=sharing

Script `lesson_3a.py` shows how to retrieve the data and turn it into a list of IDs:

```python
(code snippet)
```

The data has two columns, so our code will extract it using the `getDataColumns()` method and making column 0 into our list. (Remember that in most Python contexts indexing starts with 0, not 1.)

## 2. Build a data set from the IDs

Script `lesson_3b.py` introduces a generalized function to make a request to a Web API:

```python
def api_requester(base_url, query_path):
    req = base_url + '/' + query_path
    response = requests.get(req)
    # time.sleep(.05)
    return response.json()
```

(Note, since the Met API limits requests to 80 per second, there is some chance that the script will run too rapidly and get a rejection response. If this happens, the `time.sleep` instruction can be uncommented to add a little delay.)

The `base_url` for the Met API will always be the same, so we can declare a variable to make things easier:

```python
met_base = 'https://collectionapi.metmuseum.org/public/collection/v1'
```

To see an API response for an artwork in a browser you can look at

https://collectionapi.metmuseum.org/public/collection/v1/objects/774336

We will be taking each ID and forming a GET request like this, processing the JSON to get some key information, and then sending that to Sheet2 of our Google Sheet.

(MORE TK)

[<<< Previous](Lesson_2.md) | [Next >>>](Lesson_4.md)