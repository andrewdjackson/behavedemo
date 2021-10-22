from behave import *
from hamcrest import assert_that, equal_to, greater_than
from helpers.client import Client


@given(u'the article service')
def step_impl(context):
    # instantiate the api client
    context.client = Client()
    context.client.serviceurl = 'http://localhost:10000'


@given(u'a list of "{n}" articles')
def step_impl(context, n):
    # convert string parameter to integer
    context.n = int(n)


@when(u'a list of all articles is requested')
def step_impl(context):
    # call rest api here
    context.client.get_all_articles()


@then(u'the list of articles is returned')
def step_impl(context):
    # expect the number of articles returned to be the same
    assert_that(context.client.count, greater_than(0))


@given(u'the article id is "{id}"')
def step_impl(context, id):
    # instantiate the api client
    context.client = Client()
    context.id = id


@when(u'a single article is requested')
def step_impl(context):
    # call rest api here
    context.client.get_article(context.id)


@then(u'the requested article is returned')
def step_impl(context):
    # expect the number of articles returned to be 1
    assert_that(context.client.count, equal_to(1))
    # validate the id is the same as the requested id
    assert_that(context.client.articles[0]["Id"], equal_to(context.id))


@then(u'the status code "{status_code}" returned')
def step_impl(context, status_code):
    # convert string parameter to integer
    status_code = int(status_code)
    # validate the status code
    assert_that(context.client.status, equal_to(status_code))



@when(u'the user creates a new article with the id "{id}"')
def step_impl(context, id):
    context.id = id
    context.client.create_article(id)


@given(u'the user creates a new article with the id "{id}"')
def step_impl(context, id):
    context.id = id
    context.client.create_article(id)


@when(u'the user deletes the article with the id "{id}"')
def step_impl(context, id):
    context.client.delete_article(id)


@then(u'the requested article is not found')
def step_impl(context):
    assert_that(context.client.status, equal_to(200))