data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq_map = {}

for item in data:
    freq_map[item] = freq_map.get(item, 0) + 1

print(freq_map)