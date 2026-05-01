import numpy

n = int(input())

matrix = numpy.array([input().split() for _ in range(n)], float)

det = numpy.linalg.det(matrix)

print(round(det, 2))



