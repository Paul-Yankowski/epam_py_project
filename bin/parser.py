from lxml import html
import requests
from collections import Counter
URL = 'https://www.onliner.by/'
def parse():
    page = requests.get(URL)
    tree = html.fromstring(page.content)

    all_elms = tree.cssselect('*')
    all_tags = [x.tag for x in all_elms]

    c = Counter(all_tags)

    # print('all:', len(all_elms), 'span:', c['span'])

    for e in c:
        print(f'{e}: {c[e]}')
parse()



