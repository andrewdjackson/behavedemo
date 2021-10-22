## Behave API and Selenium Example

[Python Behave Documentation]('https://behave.readthedocs.io/en/latest/index.html')
[PyHamcrest]('https://pyhamcrest.readthedocs.io/en/v2.0.2/library/')
[pyHamcrest Matchers]('https://pyhamcrest.readthedocs.io/en/v2.0.2/library/')
[Python Requests]('https://requests.readthedocs.io/en/master/user/quickstart/')
[Using the behave Framework for Selenium BDD]('https://www.blazemeter.com/blog/using-the-behave-framework-for-selenium-bdd-testing-a-tutorial')

## Setup

To get up and running make sure you have Python 3.8 installed.
Install the following Python modules:

pip install pyhamcrest

pip install behave

pip install selenium

pip install requests

## Running the Tests

To run the tests in the behavedemo folder run the command 'behave'

A couple of simple tags have been implemented, @api to run the API tests, @web to run the Selenium tests.

These can be run with 'behave --tags="@api"' or 'behave --tags="@selenium'

## The Server

The server is based on the project [Creating Restful API with GoLang](https://tutorialedge.net/golang/creating-restful-api-with-golang/)
This server provides a REST API to add, remove and list articles.
On startup the service creates 2 articles

### Building and Running the Server

Install GoLang, assuming the paths are set correct run the following commands:

'go get'

'go build'

then run the output executable 'server(.exe)'

The server will listen on http://localhost:10000

### REST API:

| Path            | Function            | Method            |
| --------------- | ------------------- | ----------------- |
| "/articles"     | returnAllArticles   | Methods("GET")    |
| "/article"      | createNewArticle    | Methods("POST")   |
| "/article/{id}" | deleteArticle       | Methods("DELETE") |
| "/article/{id}" | returnSingleArticle | Methods("GET")    |

### Web Interface

The root URL will present a login page.
On submit this will redirect to /login with a status message

### Article Data Structure:

```
{
    "Id": "3",
    "Title": "Newly Created Post",
    "desc": "The description for my new post",
    "content": "my articles content"
}
```

## Behave Tests

### Folder Structure

The Python Behave folder structure is as follows:

features/

features/everything.feature

features/steps/

features/steps/steps.py

For this example, there is a server written in Go which provides a simple login web page and a simple REST API.
This can be found in the /server folder.

## General Coding Style Notes

-  The selenium web driver and the rest api client have been abstracted into Python classes.
-  This creates a well structured low coupling and high cohesion approach (see SOLID principles).
-  Internal helper functions follow the Python convention of functions prefixed with an underscore.
-  The feature files and associated step files share the same name, e.g. login.feature, steps/login.py
-  The use of Hamcrest simplifies the assertion logic considerably and is well supported.

## Next Steps

-  The example doesn't take advantage of Behave background steps which will simplify and create greater reuse opportunities.
-  The example doesn't take advantage of Behave fixtures that will allow for tests to be written once for multiple environments.
-  The selenium driver is setup in the simplest form possible but can be coded to be optimised to run at the start of the test run and close at the end.
