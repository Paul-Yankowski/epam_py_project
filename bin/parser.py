import requests
from collections import Counter

from lxml import html

URL = 'https://www.onliner.by/'
def parse():
    page = requests.get(URL)
    tree = html.fromstring(page.content)

    all_elms = tree.cssselect('*')
    all_tags = [x.tag for x in all_elms]

    c = Counter(all_tags)

    for e in c:
        print(f'{e}: {c[e]}')
parse()



