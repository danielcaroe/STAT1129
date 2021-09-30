student_dict = {'Andy': 88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}
def student_grade(name):
    if name == 'Andy':
        print('88')
    elif name == 'Amy':
        print('66')
    elif name == 'James':
        print('90')
    elif name == 'Jules':
        print('55')
    elif name == 'Arthur':
        print('77')
    else:
        print("I cannot find this student's name")
        
student_grade('Jules')