from collections import Counter
import requests
from lxml import html
#import datetime

#logger
# def log_site(param):
#     n=datetime.datetime.now()
#     log_str=str(datetime.date.today())+' | '+str(n.hour)+':'+str(n.minute)+' | '+str(param)
#     with open('log_file.txt','a') as f:
#         f.write(log_str+'\n')

class Parser:

    def __init__(self,URL):
        self.URL=URL
        self.site_name = 'parsed URL'
    def tags(self):
        page = requests.get(self.URL)
        tree = html.fromstring(page.content)

        all_elms = tree.cssselect('*')
        all_tags = [x.tag for x in all_elms]

        c = Counter(all_tags)
        tags={}
       # log_site(self.URL)
        for e in c:
            tags[e]=c[e]
        return tags
