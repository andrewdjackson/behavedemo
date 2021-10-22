from behave import *
from hamcrest import assert_that, equal_to
from helpers.webdriver import WebDriver
from helpers.client import Client


@given(u'the user is on the login page')
def step_impl(context):
    # instantiate the web driver and open the url in the browser
    context.webdriver = WebDriver()
    context.webdriver.browse_to_url('http://localhost:10000')


@given(u'the username "{username}"')
def step_impl(context, username):
    # store the username
    context.username = username


@given(u'the password "{password}"')
def step_impl(context, password):
    # store the password
    context.password = password


@when(u'the user logs in')
def step_impl(context):
    # send the username and password to the
    # browser and submit the form
    context.webdriver.send_keys('username', context.username)
    context.webdriver.send_keys('password', context.password)
    context.webdriver.submit()


@then(u'the user has logged in with "{result}"')
def step_impl(context, result):
    # validate the response displayed in the browser
    status = context.webdriver.get_value("login")
    assert_that(status, equal_to(result))
    context.webdriver.close()


#
# Alternative flow using 'headless' Python Requests 
#

@when(u'the login form is submitted')
def step_impl(context):
    context.client = Client()
    context.client.post_login_form(context.username, context.password)
    


@then(u'the user has logged in with the status code "{status_code}"')
def step_impl(context, status_code):
    # validate the response displayed in the browser
    assert_that(context.client.status, equal_to(int(status_code)))

