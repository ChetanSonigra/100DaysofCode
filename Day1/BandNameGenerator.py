# print, input, string,variables, comment,len()
# print: sep=' ', end='\n', escaping ' or "  with \ 
# variables can start with _ or letters and contains only _, letters and digits. 
# variables are case sensitive and shouldn't be python keywords 

print('Welcome to the band name generator.')
city = input('Which city did you grow up in?')
pet = input('What is your pet name?')
print('Your band name could be: ',city,pet)

print("""\
Usage: thingy [OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to
""")

print("""
Usage: thingy [OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to
""")

print(r'C\SF\SFDS\SDF') # print('r'C\SF\SFDS\SDF\') - odd number of \ at end of raw string is not valid.

# invoking python iterpreter:
# 1. when invoked with "python" without filename or arguments. sys.argv will be ['']
# 2. when invoked with "python -" sys.argv will be ['-']
# 3. when invoked with "python -c 'print(43)'" sys.argv will be ['-c']
# 4. when invoked with "python -m Day3.control_flow" sys.argv will be ['full path of module']
import time
for i in range(15):
    print(i,end=' ',flush=True)
    time.sleep(0.6)
print('end')
print('sdflsfds')
time.sleep(5)
# file parameter is where we want to print.
# default = sys.stdout. can change to any file.