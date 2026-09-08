data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq_map = {}

for item in data:
    freq_map[item] = freq_map.get(item, 0) + 1

print(freq_map)

print(freq_map.get('pal', 4))  # Output: 3

print(list(range(6)))  # Output: [0, 1, 2, 3, 4, 5]

a = 20
m = a
alist = list(range(a))
print(alist[::-1])
lck = []
for i in alist[::-1]:
    if m // 2 == i:
        lck.append(m % 2)
        m = i

print("".join(map(str, lck[::-1])))
print(lck[::-1])
print("".join(str(lck[::-1])))
j = str(lck)
print(type(j))
j = list(map(int, lck[::-1]))
print(j)
print(1%2)
k = 1
blist = list(range(1))
bbinlst = []
for i in blist[::-1]:
        if k // 2 == i:
            bbinlst.append(k % 2)
            k = i

print(bbinlst)