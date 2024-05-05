# FileNotFound 
# KeyError
# IndexError
# TypeError
# try: except: else: finally: 

try:                            # doing something that might cause an exception
    f = open('a.txt','w')
    f.close()
    d = {'k':153}
    print(d['j'])
except FileNotFoundError:       # Do this if FileNotFound exception occurs.
    print("File doesn't exist.")
except KeyError as err:
    print(f"Key {err} doesn't exist")
else:                           # Do this if there were no exception.
    print('Everything went well.')
finally:                        # Do this no matter what happens.
    print('Final')
    

# Raise Exception: 

if 5>2:
    raise TypeError('This is example of raised error.')
    
    
# Handled exceptions in NATO alphabet project and improved password manager by using json file.
# Searching website details in password manager.
