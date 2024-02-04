# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

records = [['Harsh', 39], ['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41]]
grades = list(map(lambda s: s[1], records))
grades.sort()
lowest_grade = grades[0]
second_lowest_grade = list(filter(lambda score: score > lowest_grade, grades))[0]
second_lowest_students = list(filter(lambda student_ls: student_ls[1] == second_lowest_grade, records))
names = list(map(lambda s: s[0], second_lowest_students))
names.sort()
for name in names:
    print(name)

