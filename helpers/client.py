import requests
import json

class Client(object):
    def __init__(self):
        self.serviceurl = 'http://localhost:10000'
        self.articles = []
        self.status = 500
        self.response = None
        self.count = 0


    def get_all_articles(self):
        # use the helper function to make the rest GET api call
        self._get_rest_api_call(f"{self.serviceurl}/articles")

        # use the helper function to extract the articles
        self._get_list_of_articles(self.response)


    def get_article(self, id):
        # use the helper function to make the rest GET api call
        self._get_rest_api_call(f"{self.serviceurl}/article/{id}")

        if self.status != 404:
            # use the helper function to extract the articles
            self._get_list_of_articles(self.response)


    def post_login_form(self, username, password):
        response = requests.post(self.serviceurl, data = {'username':username, 'password':password})
        self.status = response.status_code

    
    def create_article(self, id):
        article = {'Id':id, 'Title':id, 'desc':'the description for my new post', 'content':'my article content'}
        response = requests.post(f"{self.serviceurl}/article", data = json.dumps(article))
        self.status = response.status_code


    def delete_article(self, id):
        response = requests.delete(f"{self.serviceurl}/article/{id}")
        self.status = response.status_code       

    #
    # Helper functions
    # Python convention is to put an underscore at the start of the function name
    # to indicate it's an internal or private method
    #

    def _get_rest_api_call(self, endpoint):
        resp = requests.get(endpoint)
        self.status = resp.status_code

        if self.status != 404:
            self.response = resp.json()


    def _get_list_of_articles(self, response):
        # if the response is a list, then use the length of the
        # list as the count.
        # for a single response we need to append that as the
        # only item in the list. This eliminates the need for
        # conditional logic when handle single vs multiple results

        if isinstance(self.response, list):
            self.count = len(response)
            self.articles = self.response
        else:
            self.count = 1
            self.articles.append(response)