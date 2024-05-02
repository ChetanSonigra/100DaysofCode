import pandas as pd
import random
names = ['Alex','Beth','Caroline','Dave','Elanor','Freddie']

student_scores = {
                    "students": [student for student in names],
                    "scores": [random.randint(1,100) for i in range(len(names))],
                    "status": [1 for name in names]
                    } 
 

students_df = pd.DataFrame(student_scores)
print(students_df)
for k,v in students_df.items():           
    print(k)                    # gives column names
    
for k,v in students_df.items():
    print(v)                    # gives all column values as series.
    
for k,v in students_df.iterrows():
    print(k)                    # gives row indexes
    
for k,v in students_df.iterrows():
    print(v)                    # gives one row 
    print(v.students)           # gives specific value for a row.  

