# from collections import Counter
#Stores elements as key and it's count as value

# a = "aaaabbbbbbcccccd"
# myCounter = Counter(a) #items(),keys(),values()
# print(myCounter)
# print(myCounter.most_common(1))
# print(list(myCounter.elements()))

# from collections import namedtuple

# Point = namedtuple("Point",'x,y')
# pt=Point(5,6)
# print(pt.x)

# from collections import OrderedDict

# ordDict = OrderedDict() #Normal Dict is capable sing py 3.7

from collections import defaultdict

d = defaultdict(int) #default is a int (0)
print(d["l"]) 

from collections import deque
#Double ended queue

d=deque()
d.append(5)
d.append(6)
d.appendleft(7)
# d.popleft()

d.rotate(2) #Move elements 2 places to right
d.rotate(-2) #Move elements 2 places to left

print(d)


 





