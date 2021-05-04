import requests
from collections import Counter

from lxml import html

def parse(URL):
    page = requests.get(URL)
    tree = html.fromstring(page.content)

    all_elms = tree.cssselect('*')
    all_tags = [x.tag for x in all_elms]

    c = Counter(all_tags)
    tags={}
    for e in c:
        tags[e]=c[e]
    return tags
        #print(f'{e}: {c[e]}')

print(str(parse('https://www.onliner.by/')).replace('\'','\"',100000))



