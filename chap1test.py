from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)



b = {}    # A regular dictionary
b.setdefault('a', []).append(1)
b.setdefault('a', []).append(2)
b.setdefault('b', []).append(4)

b.setdefault()