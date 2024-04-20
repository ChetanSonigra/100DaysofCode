programming_dictionary = {
    'bug': 'An error in program that prevents program from running as expected.',
    'function': 'A piece of code that you can call over and over again.'
}

# retriving.
print(programming_dictionary['bug']) # keyerror if key doesn't exist

# adding or reassigning value.
programming_dictionary['loop'] = 'The action of doing something over and over again.'

# create an empty dictionary or clear existing one.
new_dict = {}
# programming_dictionary = {}

# Loop through dictionary.
for key in programming_dictionary:
    print(key,programming_dictionary[key])
    
print(programming_dictionary.items())  # list of tuples

print(programming_dictionary.keys())   # list

print(programming_dictionary.values()) # list


capitals = {
    'France': 'Paris',
    'Germany':'Berlin'
}

# Nesting list in dictionary
travel_log = {
    'France': ['Paris','Lille','Dijon'],
    'Germany': ['Berlin','Hamburg','Stuttgart']
}

# Nesting dictionary in a dictionary.
travel_log = {
    'France': {'cities_visited': ['Paris','Lille','Dijon'], 'total_visits': 12},
    'Germany': {'cities_visited': ['Berlin','Hamburg','Stuttgart'], 'total_visits': 10}
}

# Nesting dictionary in a list.
travel_log = [
    {
        'country': 'France', 
        'cities_visited': ['Paris','Lille','Dijon'], 
        'total_visits': 12
    },
    {
        'country': 'Germany', 
        'cities_visited': ['Berlin','Hamburg','Stuttgart'], 
        'total_visits': 10
     }
]

print(list(programming_dictionary)) # gives keys of dictionary


# dictionary comprehenstion
d = {x: x**2 for x in (2, 4, 6)}

# with keyword arguments - useful when keys are strings.
d = dict(a=1,b=2,c=3)
print(d)

del d['a']
print(d)

print(len(d))

x = iter(d) # returns iterator object

d.pop('d',0)
d.popitem()    # removes last item in LIFO order.

d.update({'c':3,'d':4})      # union of 2 dictionaries.
print(d)

d.setdefault('c') # returns existing key's value
d.setdefault('f') # inserts key if doesn't exist with None value
d.setdefault('f',0) # doesn't change key's value if key exist
d.setdefault('g',0) # inserts key if doesn't exist with default value provided.

f = dict(a=22,b=22,m=8)
print(d|f)          # merge 2 dict. dict after | take priority.
d|=f                # updates d with values of merged dict.
print(d)
d.copy()  # shallow copy
d.clear() # clears dictionary
