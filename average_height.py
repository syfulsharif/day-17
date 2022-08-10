# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# print(student_heights)
i = 0
total_height = 0
for height in student_heights:
    i += 1
    total_height += height
    # Write your code below this row 👇
# print(total_height)
# print(i)
average_height_students = round(total_height / i)
print(average_height_students)
