import math
import random

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_dist_from_origin(self):
        dist_from_origin = math.sqrt((self.x **2) + (self.y **2))
        return dist_from_origin
    def __str__(self):
        return str(self.x)+','+str(self.y)

for i in range(5):
    thepoint = Point(random.random(), random.random())
    print("Sample",i,"is:",thepoint)
    print("Distance from origin:", thepoint.get_dist_from_origin(),'\n')

inside = 0
outside = 0
for i in range(1000000):
    apoint = Point(random.random(), random.random())
    dist = apoint.get_dist_from_origin()
    if  dist < 1:
        inside = inside + 1
    else:
        outside = outside + 1

print(inside,"of the 1000000 are inside.")
print("acutal pi is about 3.141592653589793")
estimate = 4*(inside/1000000)
print("estimated pi is about", estimate)
print("monte carlo simulation is off by", 3.141592653589793 - estimate)
