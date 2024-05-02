import random

names = ['Alex','Beth','Caroline','Dave','Elanor','Freddie']

student_scores = {student:random.randint(1,100) for student in names}     
# from list
print(student_scores)

passed_students = {student:marks for student,marks in student_scores.items() if marks>40} 
# from dictionary
print(passed_students)

