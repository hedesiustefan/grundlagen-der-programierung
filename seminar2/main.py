d = {'a': 10, 'b': 20}

for key, value in d.items():
    print(key, value)

for key in d:
    print(key, d[key])

print('a' in d)
print(10 in d.values())

t = 1,2,3

print(t)

x = t[0]
y = t[1]
z = t[2]

x, _, z = t

print(x, 0, z)
print(['a']*5)
l1 = [1,2,3]
l2 = l1[:]
l1[0] = '?'
print(l1, l2)
print(id(l1), id(l2))