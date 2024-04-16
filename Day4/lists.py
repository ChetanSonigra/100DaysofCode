l = [1,2,'a',0.3,True]

print(l[0],l[4],l[-1],l[::-1]) # indexing

# assignment
l[1] = 200
print(l)

# append
l.append('b')
print(l)

# insert
l.insert(1,'c')
print(l)

# extend
l.extend([1,200,201,203])
print(l)

# reverse
l.reverse()
print(l)

# short
l = [1,2,4,1,2]
l.sort()
print(l)

# removes first item found in list.
l.remove(1)
print(l)

# pop(i)
l.pop(1)
print(l)

# clear() clears everything.
l.clear()

# index
l.index(2,3,4)
l.index(2)

# count
print(l.count(1))