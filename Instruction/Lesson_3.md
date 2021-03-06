# Using Pandas

The `pandas` Python library is very popular among data scientists and has many great features. It is fairly simple to take data from a Google Sheet and cast it as a Pandas DataFrame, on which you can perform operations and analysis. Conversely, you can take a Pandas DataFrame and save it to a Google Sheet via the API. It is all a matter of getting it into the right format.

First, make sure you have the `pandas` package installed. Since you are (probably) using a virtual environment, you may need to install it there:

```
pip install pandas
```

Recall that the basic data format understood by the Google Sheets API is a 2-dimensional array, a list of lists, one for each row including the heads:

```python
[ ['column head 1', 'column head 2'], ['row1-col1', 'row1-col2'] ]
```

A Pandas DataFrame could be expressed as:
```python
pd.DataFrame([['row1-col1', 'row1-col2']], ['column head 1', 'column head 2'])
```

This is just to say that the formats are interchangeable. Included here is a set of functions to convert between a sheetFeeder `dataSheet` and a Pandas `DataFrame` gathered in `pandas_functions.py`. You can import them from the base directory using:

```python
import pandas_functions as pf
```

`lesson_3a.py` shows a few examples of getting data from Google Sheets, transforming it into `Pandas` format, getting some information, and transforming it back into a simple array that could be sent back to Google Sheets. The output should look like:

```
1. dataSheet data array:
[['Col A', 'Col B', 'Col C', 'Col D'], ['1', '2', '3', '4'], ['5', '6', '7', '8'], ['0', '11.5', '-5', '9.25']]

2. Converted to DataFrame:
   Col A  Col B  Col C  Col D
0      1    2.0      3   4.00
1      5    6.0      7   8.00
2      0   11.5     -5   9.25

Some Pandas analysis...
DataFrame shape:
(3, 4)

Data types:
Col A      int64
Col B    float64
Col C      int64
Col D    float64
dtype: object

Column averages:
Col A    2.000000
Col B    6.500000
Col C    1.666667
Col D    7.083333
dtype: float64

3. Converted back to dataSheet array:
[['Col A', 'Col B', 'Col C', 'Col D'], [1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [0.0, 11.5, -5.0, 9.25]]
```

Next let's try modifying the data in Pandas. Say we are given a Google Sheet with some data and we want to enrich it where it is.

In your Google Sheet document create a new tab called "Pandas". Again note the UID of your document. Modify the script `lesson_3b.py` with your UID and tab name:

```python
sheet_id = '<YOUR_UID_HERE>'
sheet_range = 'Pandas!A:Z'
the_sheet = dataSheet(sheet_id, sheet_range)
```

After populating your new tab with some seed data, it retrieves it and transforms it into Pandas format using the `datasheet_to_dataframe()` function. Next we want to calculate the mean of each row and put it in a new column. This can be done like so:

```python
df['Average'] = df.mean(numeric_only=True, axis=1)
```

The resulting table output looks like

```
   Col A  Col B  Col C  Col D  Average
0      1    2.0      3   4.00   2.5000
1      5    6.0      7   8.00   6.5000
2      0   11.5     -5   9.25   3.9375
```

Using the `dataframe_to_datasheet` function we can then convert back to an array and put the updated table in the Google Sheet:

```python
# Convert back into array
data2 = pf.dataframe_to_datasheet(df)

# Post back to sheet, replacing data
the_sheet.clear()
the_sheet.appendData(data2)
```


[<<< Previous](Lesson_2.md) | [Next >>>](Lesson_4.md)