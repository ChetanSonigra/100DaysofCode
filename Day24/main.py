file = open('Day24/my_file.txt','r')
contents = file.read()
print(contents)
file.close()

with open('Day24/my_file.txt','+w') as f:  # open creates a file if it doesn't exist.
    contents = f.read()
    print(contents)
    f.write('New Text 3')
    f.seek(0)
    contents=f.read()
    print(contents)
    print(dir(f))
    print(f.name,f.closed,f.mode)    
    

# methods: read(), readline(), readlines(), write(), writelines(list_of_lines), 
# flush(), seek(offset,from),tell(), readable(),writable()
# Use mode = rb/wb for binary files.
# f.seek(offset,from)  -    f.seek(3,0),f.seek(3,1),f.seek(-3,2) - 0=beginning, 1=current, 2=end

# pickle - unpickle = serialize - unserialize
# for storing and unstoring objects.

class Student:
    def __init__(self,name,roll,dept) -> None:
        self.name = name
        self.roll = roll
        self.dept = dept
        
    def display(self):
        print(f'Roll: {self.roll}\nName: {self.name}\nDepartment: {self.dept}')
        
import pickle
students = [Student('Chetan',1,'IT'),Student('Ram',2,'Mech'),Student('Hiren',3,'ECE')]
with open('100DaysofCode/Day24/students.data','wb') as f:
    for s in students:
        pickle.dump(s,f)
    
with open('100DaysofCode/Day24/students.data','rb') as f:
    for i in range(3):
        s = pickle.load(f)
        s.display()

# Zip and Unzip files:

from zipfile import *
f =  ZipFile('100DaysofCode/Day24/output/letters.zip','w',ZIP_DEFLATED)
f.write('100DaysofCode/Day24/output/ready_to_send/letter_for_Aung.txt','letter_for_Aung.txt')
f.write('100DaysofCode/Day24/output/ready_to_send/letter_for_Chetan.txt','letter_for_Chetan.txt')
f.write('100DaysofCode/Day24/output/ready_to_send/letter_for_Fong.txt','letter_for_Fong.txt')
f.close()

f = ZipFile('100DaysofCode/Day24/output/letters.zip')
f.extractall('100DaysofCode/Day24/output')
f.close()