import numpy
import numpy

n, m = map(int, input().split())

array_elements = [list(map(int, input().split())) for _ in range(n)]

my_array = numpy.array(array_elements)

transposed_array = numpy.transpose(my_array)

flattened_array = my_array.flatten()

print(transposed_array)

print(flattened_array)
