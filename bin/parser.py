from collections import Counter
import requests
from lxml import html
from Logger.Logger import Logger
class Parser:

    def __init__(self,URL):
        if type(URL) != str:
            print('Unexpected URL')
            raise TypeError
        else:
            self.URL=URL
            self.site_name = URL.split('//')[1].split('/')[0]
            self.log = Logger(self.URL)

    def tags(self):
        page = requests.get(self.URL)
        tree = html.fromstring(page.content)

        all_elms = tree.cssselect('*')
        all_tags = [x.tag for x in all_elms]

        c = Counter(all_tags)
        tags={}
        self.log.log_site()
        for e in c:
            tags[e]=c[e]
        return tags
