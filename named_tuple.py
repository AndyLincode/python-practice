from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', ["x", "y"])

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# line_length = sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)
line_length = sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)
print(line_length)  # 3.8078865529319543

Worker = namedtuple('Worker', ["job", "salary", "workplace"])

# job, salary, work place
Mike = Worker("Engineer", 65000, "Taiwan")
print(type(Mike))
print(Mike)
print(Mike[0])
print(Mike.job)
# <class '__main__.Worker'>
# Worker(job='Engineer', salary=65000, workplace='Taiwan')
# Engineer
# Engineer
