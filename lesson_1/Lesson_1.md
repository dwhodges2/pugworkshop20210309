# Lesson 1: Connecting to the Google Sheets API

Before using the API there are a few things to install and configure in your local environment. You will need to be able to authenticate to a Google Apps-enabled account, i.e., an an account that you can use to create, read, and edit Google Sheets documents. Your CU LionMail account should suffice, but you may wish to use a different account instead.

## Installing and configuring sheetFeeder

The Google Sheets API is well documented with plenty of samples and guidelines. It can be a little overwhelming however, and we want to get up and running quickly. To make things easier we will be using a Python library called `sheetFeeder` that abstracts some of the more useful API features into a set of short commands. 

### 1. Install sheetFeeder package and dependencies

Once you have your Anaconda or other Python 3 environment ready, install sheetFeeder and its dependencies using

```
pip install sheetFeeder
```

Note: If you have both Python 2 and Python 3 installed, you may need to use pip3:

```
pip3 install sheetFeeder
```

This will install `sheetFeeder` along with the Google API client library and some other dependencies (some of which you may already have, like `requests`).

### 2. Obtain Google API credentials

(TK)

### 3. Generate an API token

(TK)

