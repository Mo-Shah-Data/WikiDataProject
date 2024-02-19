import sys
from urllib.request import urlretrieve

for i in sys.argv:
    if sys.argv is not sys.argv[0]:
        print(i)

# id_q = str(sys.argv[1])
# url = 'https://www.wikidata.org/wiki/Special:EntityData/{}.json'.format(id_q)
# filename = '{}.json'.format(id_q)
#
# urlretrieve(url, filename)
