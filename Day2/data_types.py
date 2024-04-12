# ---------------primitive data types---------------------#
# string, int, float, bool
# string, string indexing, slicing.
# int: 23_343_34342_234, whole numbers.
# float: 324.23, 2.2, 1.0
# bool: True, False
# complex number: j/J. x = 4+2j or x = complex(4,5); x.real(), x.img()
# --------------------------------------------------------#

# type(), type errors, type conversions/casting.

# mathematical operations:
# (), **, *, /, %, //,  +, -  PEMDAS
# only division gives floor always irrespective of inputs.

# NUMBER manipulation:
# round(num, default=0)
# +=, -=, *=, /=, ...
# f string: 
# f'example1 {example2} example3 {example4}'

# string can be concatenated with + operator and repeated with *
# two or more string literals next to each other are automatically concatenated.
# 'sdf' 'sdfs' this works with string literals only not with variable or expression.
a = 'sfd' 'sdfsd'
print(a)
# index out of range is raised in indexing. while in slicing it is handled automatically.
# string is immutable. it doesn't support item assignment.
# len()

# list: mutable, ordered sequence of items.
# simple assignment never copies data, it just refers to the existing data.
a = [1,2,3]
b= a
print(id(a)==id(b))
# slicing returns new list containing requested elements.
c = a[:] # returns shallow copy
print(id(a)==id(c))
# assignment to slices is also possible.
a[1:2]=[1,2,2,2]
print(a)


# bool:
# any non-zero is true, while zero is false.
# any non-empty sequence is true, while empty is false.