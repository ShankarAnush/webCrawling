from html.parser import HTMLParser
from urllib import parse
from bs4 import BeautifulSoup


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.first_tag = None
        self.product_name = None
        self.link = None
        self.dictionary_of_links = dict()

    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            self.first_tag = tag
            for (attribute, value) in attrs:
                if attribute == 'href':
                    link = parse.urljoin(self.base_url, value)
                    # This take care of the relative path ( only '/banking_sector' of
                    # 'https://www.com/banking_sector' present as value field) present in the value field
                    # of attribute href self.temporary_links.add(link)
                    self.link = link
            print("Encountered a start tag:", tag)

    def handle_data(self, data):  # to fetch data only from anchor tags
        if self.first_tag == 'a':
            print("Encountered some data  :", data)
            self.first_tag = None
            string = str(data)  # convert to data type string
            self.product_name = string.replace("\r\n", "")
            # self.anchor_text.add(data)
            if self.link not in self.dictionary_of_links.keys():
                self.dictionary_of_links[self.link] = self.product_name
            # temp_dict = {self.link: self.product_name}  # temporary local dictionary before updating the global
            # dictionary
            # self.dictionary_of_links.update(temp_dict)

    def send_links_and_data(self):
        # dictionary_of_links = dict(zip(self.temporary_links, self.anchor_text))
        # print(self.dictionary_of_links)
        return self.dictionary_of_links
