
n, x = map(int, input().split())

subject_marks = []
for _ in range(x):
    subject_marks.append(map(float, input().split()))

for student_scores in zip(*subject_marks):
    # 4. Calculate and print the average for each student
    print(sum(student_scores) / x)
