from collections import namedtuple
n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
total_marks = 0
for _ in range(n):
    row_data = input().split()
    student = Student(*row_data)
    total_marks += int(student.MARKS)
print("{:.2f}".format(total_marks / n))
