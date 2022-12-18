class Coordinate(object):
    #attributes
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 
    #methods
    
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
    def __len__(self):
        return 2
    
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
    
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

        
c = Coordinate(3,4)
d = Coordinate(4,5)
# here c referes to the self.
# these are the two ways to call a method in python.
dist = c.distance(d)
dist_alt = Coordinate.distance(c, d) # here c refers to the self.
print((dist, dist_alt))
print(c)
print(isinstance(c, Coordinate))
print(c + d)
print(Coordinate.distance.__doc__)
# d = Coordinate(d,3,4)
# print(d.x)
from collections import Counter
a = "hello"
my_counter  = Counter(a)
print(my_counter) # this is a dictionary 

from itertools import product

a = [1,2]
b = [3]

prod = product(a, b,repeat = 2) # cartesian product
print(list(prod))

from itertools import permutations

a = [1, 2, 3]
print(tuple(permutations(a)))

from itertools import accumulate
import operator
a = [1, 2, 5, 4]
acc = accumulate(a , func = operator.mul)
acc_max = accumulate(a, func = max)
print(list(acc))
print(list(acc_max))


from itertools import groupby


def the_fun(x):
    return x < 3
a = [1,2,3, 4]
group_obj = groupby(a, key=the_fun)
# you can make this lmbda styke also
# print(dict(group_obj))
for key, value in group_obj:
    print(key,list(value))
    
## Lambda functions
func = lambda x: [a*3 for a in x]
print(func(a)) # will multiply each entry in x 

points2D = [(1,2), (15,1), (5,-1), (10,4)]
sorted_points = sorted(points2D, key = lambda x: x[1])
#sorts accirding to the second element in the tuple
print(sorted_points)

a = [1,2, 3, 4, 5]
b = map(lambda x: x**2, a) # for not using the list comprehenstion syntax
print(list(b))

c = filter(lambda x: x%2 == 0, a)
print(list(c))


