dict = {'Andy': 88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}
all_grades = dict.values()
max_grade = max(all_grades)
min_grade = min(all_grades)
mean_grade = sum(dict.values()) / float(len(dict))

print('The maximum grade is', max_grade)
print('The minimum grade is', min_grade)
print('The mean of grades is', mean_grade)
