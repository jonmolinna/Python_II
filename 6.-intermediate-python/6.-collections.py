# collections: Counter, namedtuple, orderedict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaaaabbbbbbbbccccccc"
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.most_common(1))


Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)


d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
print(d['a'])


m = deque()
m.append(1)
m.append(2)
m.appendleft(3)
print(m)

m.extendleft([4, 5, 6])
print(m)
m.rotate(-1)
print(m)