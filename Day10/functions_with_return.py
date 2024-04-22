def format_name(fname: str,lname: str) -> str:   # annotations
    """Takes a first and last name and format it to return title case version of name.
    """
    # Above docstring shows up as documentation when we call function.
    if fname=='' or lname=='':
        return 'You did not provide valid inputs.'
    
    formated_f_name = fname.title()
    formated_l_name = lname.title()
    
    return f'{formated_f_name} {formated_l_name}'

output_name = format_name('CHETAN','sonigra')

output_name = format_name(input('What is your first name? '), input('What is your last name? '))
print(output_name)

print(format_name.__doc__)
help(format_name)
print(format_name.__annotations__)
"""
multiline comment
multiline comment
"""

# execution of function introduces a new 
# local symbol table used for local variables of the function.
# variables are looked first in local function, then in enclosing function, 
# then in global variables and then in built in names.

# to access global variables, use 'global'. 
# To access variables of enclosing function, use 'nonlocal'.

