t = (1,2,3)
l=[1,2,3]
print(type(t))
print(type(l))
print(len(t))
t = ('one',2)
# slicing and indexing
print(t[0])
print(t[-1])
# build in methods
    # 1.count
t=('a','a','b')
print(t.count('a'))
    # 2.index
print(t.index('a'))

# immutability possible with list but not with tuple
l = [1,2,3]
print(l)
l[0] = 'NEW'
print(l)

print(t)
t[0] = 'NEW'