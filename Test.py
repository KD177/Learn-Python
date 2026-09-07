data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq_map = {}

for item in data:
    freq_map[item] = freq_map.get(item, 0) + 1

print(freq_map)

print(freq_map.get('pal', 4))  # Output: 3

nums = [1, 2, 3, 4, 5]
l = nums[::-2]
# k = nums.append(nums[1:3])
print(l)