#PYTHON FUNCTIONS

#GET FUNCTION
#The get function is used to retrieve the values of a specified key in a dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1965
}
x = car.get("brand")
print(x)

#ROUND FUNCTION
#rounds numbers to a up or down. up if decimal is .5 or higher. else down
x = round(3.7)
x = round(3.4)

# APPEND FUNCTION
#add a value to a list
x = [9, 0]
x.append(8)

#.IS_INTEGER
#float.is_integer() is a built-in method used to check whether a float instance 
# represents a finite integer value (a whole number with no fractional part).
5.0.is_integer()
5.6.is_integer()

#LEN()
#To see the length of a list in Python
v = [9,0]
len(v)

#REMOVE()
#removes the first occurrence of the element with the specified value.
v = [0, 9, 8]
v.remove(0)

#POP()
#to delete by value, pop()
v = [1, 9, 8]
v.pop(0)

#DEL()
#Use the del keyword to delete an item at a specific index
v = [0, 9, 8]
del v[1]
del v[1:3]

#CLEAR
#deletes whole list
v = [0, 9, 8]
v.clear()

#SORT
#sorts list in ascending order
v = [0,9,8]
v.sort()

#Sorted
#returns new sorted list
#also works on sets
v = sorted([0, 9, 8])

#set
#eliminates duplicates in lists, seems to turn them to dict
v = set([9,9,4,5])

#discard
#removes elements from set
v = set([0,8])
v.discard(8)

#update
#inserts into a dictionary or set value
v = set([0,9])
v.update([9])

#list()
#converts iterables to list and can be used to make a list
b = list(set([9,0]))
b = list()

#|
#combines sets
b = {1, 2, 3}
n = {2, 3, 4}
m = b | n

#format
# The format() method formats the specified value(s) and 
# insert them inside the string's placeholder.
k = "p + {}".format(7)

#f
#In Python, the letter f placed before 
# a string literal denotes an f-string (short for formatted string literal)
l = "apple"
m = f"j + {l}"

#join
#The join() method in Python is a built-in string method used to merge an iterable of 
#strings (like a list, tuple, or set) into a single, cohesive string
letters = ["P", "y", "t", "h", "o", "n"] #strings work too
word = "".join(letters)

#\n
#\n is A newline character — 
# an invisible control code that tells output 
# to break the line and continue on the next one.
m = "hello\nworld"

#reverse()
#If you want to reverse the list in-place 
#to save memory, use the built-in .reverse() method. 
l = [8,9,9,7]
l.reverse()

#[::-1]
#same as reverse method
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]

#chr()
#converts integer to characters. ASCII charactersx
b = chr(3)

#sum
#sum takes iterable like list and add them up
p = [9,9,7,6]
k = sum(p)

#**
#takes the power to
n = 6**2

#[]
#can turn things to list
point1 = [6,7]
point2 = [9,8]
[(point1[i]-point2[i])**2 for i in range(len(point1))]

#endswith
#The Python endswith() method checks 
#whether a string finishes with a specified suffix
m = "Hi!"
k = m.endswith("!")

#[:-1]
#returns all elements except the last instance
m = "Hi!"
k = m[:-1]
 
#for reversing a string
word = "Hello"
reversed_word = ""
for i in word:
    reversed_word = i + reversed_word