numbers = [1,2,3,4]
print(numbers)
new_numbers = [n*2 for n in numbers]
print(new_numbers)
range_list = [n*2 for n in range(1,9) if n%2==0]
print(range_list)

names = ['Alex','Beth','Caroline','Dave','Elanor','Freddie']

short_names = [name for name in names if len(name)<5]
print(short_names)

long_names = [name.upper() for name in names if len(name)>4]
print(long_names)

new_numbers = ['even' if x%2==0 else 'odd' for x in numbers]  # with if else
print(new_numbers)

numbers = [[1,2,3],[4,5,6],[7,8,9]]
new_numbers = [n for row in numbers for n in row]             # Nested for loops.
print(new_numbers)