from collections import Counter
import requests
from lxml import html
import datetime

def log_site(param):
    n=datetime.datetime.now()
    log_str=str(datetime.date.today())+' | '+str(n.hour)+':'+str(n.minute)+' | '+str(param)
    with open('log_file.txt','a') as f:
        f.write(log_str+'\n')

def parse(URL):
    page = requests.get(URL)
    tree = html.fromstring(page.content)

    all_elms = tree.cssselect('*')
    all_tags = [x.tag for x in all_elms]

    c = Counter(all_tags)
    tags={}
    log_site(URL)
    for e in c:
        tags[e]=c[e]
    return tags
        #print(f'{e}: {c[e]}')




