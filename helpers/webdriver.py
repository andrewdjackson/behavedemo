from selenium import webdriver

class WebDriver(object):
    def __init__(self):
        self.url = 'http://localhost:10000'
        self.driver = webdriver.Chrome()  # Optional argument, if not specified will search path.


    def browse_to_url(self, url):
        self.driver.get(url)


    def send_keys(self, element, value):
        self.webUI = self.driver.find_element_by_name(element)
        self.webUI.send_keys(value)


    def submit(self):
        self.webUI.submit()


    def get_value(self, element):
        webUI = self.driver.find_element_by_name(element)
        return webUI.text


    def close(self):
        self.driver.quit()
