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
    
    
