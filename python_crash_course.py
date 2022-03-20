# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:29:34 2021

@author: amazi
"""
# 2. Basics
# 2.1 variables
# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
# One Value to Multiple Variables
x = y = z = "Orange"
# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
# 2.1.1 Global Variables
# If you create a variable with the same name inside a function, this variable
# will be local, and can only be used inside the function. The global variable
# with the same name will remain as it was, global and with the original value.
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()


# The global Keyword
def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
# 2.1.2 data type
# 2.1.2.1 immutable data type:
x = "Hello World"  # str
x = 20  # int
x = 20.5  # float
x = 1j  # complex
x = True  # bool
x = b"Hello"  # bytes
x = ("apple", "banana", "cherry")  # tuple
x = frozenset({"apple", "banana", "cherry"})  # frozenset
# 2.1.2.2 mutable data type:
x = ["apple", "banana", "cherry"]  # list
x = range(6)  # range
x = {"name": "John", "age": 36}  # dict
x = {"apple", "banana", "cherry"}  # set
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview
# Setting the Specific Data Type
# 规则：
#   布尔值：True -> 1   False -> 0
#   浮点数：直接取整，省略小数点后的内容
#   字符串：合法的整数字符串，直接转换为对应的数字
#           如果不是一个合法的整数字符串，则报错 ValueError: invalid literal for int() with base 10: '11.5'
#   对于其他不可转换为整型的对象，直接抛出异常 ValueError
# float() 和 int()基本一致，不同的是它会将对象转换为浮点数
# str() 可以将对象转换为字符串
#  bool() 可以将对象转换为布尔值，任何对象都可以转换为布尔值
#   规则：对于所有表示空性的对象都会转换为False，其余的转换为True
#       哪些表示的空性：0 、 None 、 '' 。。。
# after transform data type, id changes
a = '10'
print(id(a))
b = int(a)
print(id(b))
x = str("Hello World")  # str
x = int(20)  # int
x = float(20.5)  # float
x = complex(1j)  # complex
x = list(("apple", "banana", "cherry"))  # list
x = tuple(("apple", "banana", "cherry"))  # tuple
x = range(6)  # range
x = dict(name="John", age=36)  # dict
x = set(("apple", "banana", "cherry"))  # set
x = frozenset(("apple", "banana", "cherry"))  # frozenset
x = bool(5)  # bool
x = bytes(5)  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview
# practice1
a = 'fuck'
print(a)
# practice2
a = 'fuck you'
print(a)

# 2.2 string
# 长字符串
# 单引号和双引号不能跨行使用
s = '锄禾日当午，\
汗滴禾下土，\
谁知盘中餐，\
粒粒皆辛苦'
# 使用三重引号来表示一个长字符串 ''' """
# 三重引号可以换行，并且会保留字符串中的格式

s = '''锄禾日当午，
汗滴禾下土，
谁知盘中餐，
粒粒皆辛苦'''
# 2.2.1 combining and concatenating strings
first_name = 'ada'
second_name = 'lovelace'
FullName = first_name + ' ' + second_name
print(FullName)
print("Hello, " + FullName.title() + "!")
# 2.2.2 adding whitespace to strings with tabs or newlines
# 2.2.2.1 add tab
print('\tPython')
# 2.2.2.2 add new line
print('Languages: \nPython\nC\nJavaScript')
# 2.2.2.3 add single and double quate
print('you\'re a dog')
print('you are \"jacky\"')
# 2.2.3 striping whitespace
FavoriteLanguages = ' python '
FavoriteLanguages.rstrip()
FavoriteLanguages.lstrip()
FavoriteLanguages.strip()
# 2.2.4 avoding syntax errors with strings(single and double quate)
message = "One of the python's strength is its diverse community."
print(message)
# 2.2.5 Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# 2.2.6 Strings are Arrays
a = "Hello, World!"
print(a[1])
# Looping Through a String
for x in "banana":
    print(x)
# String Length
a = "Hello, World!"
print(len(a))
# Check String
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
txt = "The best things in life are free!"
print("expensive" not in txt)
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
# Slicing
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[2:])
b = "Hello, World!"
print(b[-5:-2])
# Modify Strings
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"
a = "Hello, World!"
print(a.replace("H", "J"))  # The replace() method returns a copy of the string where the old substring is replaced
                            # with the new substring. The original string is unchanged.
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']
# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  # My name is John, and I am 36
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# Escape Characters
# \'	Single Quote
txt = 'It\'s alright.'
print(txt)  # It's alright.
# \\	Backslash
txt = "This will insert one \\ (backslash)."
print(txt)  # This will insert one \ (backslash).
# \n	New Line
txt = "Hello\nWorld!"
print(txt)  # Hello
# World!

# \r	Carriage Return
txt = "Hello\rWorld!"
print(txt)  # Hello
# World!
# \t	Tab
txt = "Hello\tWorld!"
print(txt)  # Hello   World!
# \b	Backspace
# This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)  # HelloWorld!
# \f	Form Feed

# \ooo	Octal value
# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)  # Hello

# \xhh	Hex value
# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)  # Hello

# string interpolation
name = 'Al'
age = 4000
print('My name is %s. I am %s years old.' % (name, age))
'My name is Al. I am 4000 years old.'
name = 'Al'
age = 4000
f'My name is {name}. Next year I will be {age + 1}.'
'My name is Al. Next year I will be 4001.'
# String Methods
# Python has a set of built-in methods that you can use on strings.
# Note: All string methods returns new values. They do not change the original string.
capitalize()  # Converts the first character to upper case
casefold()  # Converts string into lower case
center()  # Returns a centered string
count()  # Returns the number of times a specified value occurs in a string
encode()  # Returns an encoded version of the string
endswith()  # Returns true if the string ends with the specified value
'Hello, world!'.endswith('world!')
# True
expandtabs()  # Sets the tab size of the string
find()  # Searches the string for a specified value and returns the position of where it was found
format()  # Formats specified values in a string
format_map()  # Formats specified values in a string
index()  # Searches the string for a specified value and returns the position of where it was found
isalnum()  # Returns True if all characters in the string are alpha or numeric
'hello123'.isalnum()
True
isalpha()  # Returns True if all characters in the string are in the alphabet
'hello'.isalpha()
True
isdecimal()  # Returns True if all characters in the string are numeric
'123'.isdecimal()
True

isdigit()  # Returns True if all characters in the string are digits
isidentifier()  # Returns True if the string is an identifier
islower()  # Returns True if all characters in the string are lower case
isnumeric()  # Returns True if all characters in the string are numeric
isprintable()  # Returns True if all characters in the string are printable
isspace()  # Returns True if all characters in the string are whitespaces
'    '.isspace()
True
istitle()  # Returns True if the string follows the rules of a title
'This Is Title Case'.istitle()
True
'This Is Title Case 123'.istitle()
True
isupper()  # Returns True if all characters in the string are upper case
join()  # Joins the elements of an iterable to the end of the string
'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
ljust()  # Returns a left justified length of the string
'Hello'.ljust(10)
'Hello     '
'Hello'.ljust(20, '-')
'Hello---------------'
lower()  # Converts a string into lower case
lstrip()  # remove a left whitespace version of the string
maketrans()  # Returns a translation table to be used in translations
partition()  # Returns a tuple where the string is parted into three parts
'Hello, world!'.partition('w')
('Hello, ', 'w', 'orld!')
'Hello, world!'.partition('world')
('Hello, ', 'world', '!')
'Hello, world!'.partition('o')  # only first occurrence
('Hell', 'o', ', world!')
'Hello, world!'.partition('XYZ')  # return empty string if 'XYZ' doesn't exist
('Hello, world!', '', '')
before, sep, after = 'Hello, world!'.partition(' ')  # multiple assignment
replace()  # Returns a string where a specified value is replaced with a specified value
rfind()  # Searches the string for a specified value and returns the last position of where it was found
rindex()  # Searches the string for a specified value and returns the last position of where it was found
rjust()  # Returns a right justified total length of the string
'Hello'.rjust(10)
'     Hello'
'Hello'.rjust(20)
'              Hello'
'Hello, World'.rjust(20)
'         Hello, World'
'Hello'.rjust(20, '*')
'***************Hello'
rpartition()  # Returns a tuple where the string is parted into three parts
rsplit()  # Splits the string at the specified separator, and returns a list
rstrip()  # removes a right whitespace version of the string
split()  # Splits the string at the specified separator, and returns a list
'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
splitlines()  # Splits the string at line breaks and returns a list
startswith()  # Returns true if the string starts with the specified value
'Hello, world!'.startswith('Hello')
True
strip()  # removes a whitespace of the string
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
'BaconSpamEggs'
swapcase()  # Swaps cases, lower case becomes upper case and vice versa
title()  # Converts the first character of each word to upper case
translate()  # Returns a translated string
upper()  # Converts a string into upper case
zfill()  # Fills the string with a specified number of 0 values at the beginning

# practice1
name = 'Eric'
print('Hello ' + name + ', would you like to learn some python today?')
# 2
name1 = 'Fuck you'
print(name1.upper())
print(name1.lower())
print(name1.title())
# 3
a = 'I once said, "fuck you".'
print(a)
# 4
name = 'I'
message = name + ' once said, "Fuck You"!'
print(message)
# 5
name = '\tJacky\n\t'
print(name)
name.lstrip()
name.rstrip()
name.strip()

# 2.3 numbers
'''if number is too big, use underscore to link this number'''
c = 123_456_789
'''numbers cannot start from 0'''
# 其他进制的整数，只要是数字打印时一定是以十进制的形式显示的
# 二进制 0b开头
c = 0b10 # 二进制的10
# 八进制 0o开头
c = 0o10
# 十六进制 0x开头
c = 0x10
# 对浮点数进行运算时，可能会得到一个不精确的结果; because base_2 cannot handle float.
c = 0.1 + 0.2 # 0.30000000000000004
2 + 3
3 - 2
2 * 3
3 / 2
3 ** 2
10 ** 6
(2 + 3) * 4
2 % 3  # modulus = 2 yushu
2 // 3  # Floor division = 0 quzheng
# 2.3.1 float
0.1 + 0.1
0.2 + 0.2
2 * 0.1
2 * 0.2
0.2 + 0.1
3 * 0.1
# 2.3.2 avoid type error
age = 23
message = 'Happy ' + str(age) + 'rd Birthday'
print(message)
# 2.3.3 integers
3 / 2
# practice
print(2 + 6)
print(10 - 2)
print(2 * 4)
print(16 / 2)
print(2 ** 3)



# 2.4 comments
import this

# 3.0 introducing list
bicycles = ['trek', 'cannondale', 'readline', 'specialized']
print(bicycles)
# 3.1 accessing elements in a list
print(bicycles[0])
print(bicycles[0].title())
for i in bicycles:
    print(i.title())
print(bicycles[-1])
print(bicycles[-2])
# 3.2 using individual values form a list
message = 'my first bicycles was a ' + bicycles[0].title() + '.'
print(message)
# practice
# 1
names = ['dick', 'fuck', 'vagina', 'gan']
for i in range(4):  # the number in range can't be out of range of list.
    print(names[i])
# 2
for i in range(4):
    print('Hello ' + names[i] + '!')
# 3
transpotation = ['bicycle', 'car', 'plane']
print('I would like to own a ' + str(transpotation))
a = str(transpotation)  # we can string a whole list to become one string.
print(a[2])  # 对于一个list，【】可以选择某一个，但是对于一个string，【】可以选到第几个字符
print(transpotation[0][0])
# 3.3 changing adding and removing elements
# 3.3.1 modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
# 3.3.2 adding elements to a list
# 3.3.2.1 appending elements to the end of a list
motorcycles.append(1)  # we can append any variable type we want
print(motorcycles)
# 如果extend一个element，会把这个变量拆分，然后接到之前的list里。
# 如果extend一个list of element，会把这个list拆开接到之前的list里
# 但是不能extend一个数字,但是可以extend由数字组成的list。
# 因为数字不能拆开，但是一个list可以拆开
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
motorcycles.extend([2, 3, 4, 5, 6])
print(motorcycles)
# 3.3.2.2 inserting elements into a list
# insert的好处是你可以决定你insert到哪里
motor = ['honda', 'yamaha', 'suzuki']
# 这里写的数字就是list里的位置的前一个
# 如果想放到最后一个，就写最后一个位置的数字的下一个数字
# insert可以加数字
motor.insert(1, 1)
print(motor)
motor.insert(4, 'fuck')
print(motor)
# 3.3.2.3 removing elements from a list
del motor[0]
print(motor)
# 3.3.2.4 removing and item using the pop() method
# the pop() method removes the last item in a list, but
# it lets you work with that item after removing it.
poped_motor = motor.pop()
print(motor)
print(poped_motor)
# pop can also use to any position in a list
# but pop() can only use index, not exact item.
# pop也只能放一个argument
FirstPoped = motor.pop(0)
print(motor)
print(FirstPoped)

# 3.3.2.5 removing an item by value
a = ['I', 'want', 'to', 'fuck', 'you']
a.remove('fuck')
print(a)
# but remove can not use index to remove, only the exact item.
a.remove(0)  # error
print(a)
# remove deletes only the first occurrence of the value you specify.
# if there is a possibility the value appears more than once in the list,
# you'll need to use a loop to determine if all occurrences of the value
# have been removed
a.remove('to', 'you')  # error, remove() takes exactly one argument
a.remove(['to', 'you'])  # error, list.remove(x): x not in list

# practice
# 1
NameList = ['dick', 'fuck', 'vagina']
for i in range(3):
    print(NameList[i].title() + ', I want to invite you to dinner.')
# 2
NameList[0] = 'gan'
print(NameList)
for i in range(3):
    print(NameList[i].title() + ', I want to invite you to dinner.')
# 3
NameList.insert(0, 'dick')
NameList.insert(2, 'stupid')
NameList.append('shit')
for i in range(6):
    print(NameList[i].title() + ', I want to invite you to dinner.')
# 4
import random
from scipy.stats import uniform, truncnorm, randint

for i in range(4):
    PopedName = NameList.pop(random.randint(0, 5 - i))
    print("I am sorry, but I can't invite " + PopedName + " to dinner.")
for i in range(2):
    print(NameList[i] + ', you are still invited.')
# 总结：1. 随机数要random。randint（）
# 2. 随机数的范围要随着循环产生变化
for i in range(2):
    del NameList[0]
print(NameList)

# 3.4 organizing a list
# 3.4.1 sorting a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
a = [4, 3, 2, 1]
a.sort()
print(a)
b = {4: 'c', 3: 'o', 2: 'p', 1: 'a'}
b.sort()  # error:'dict' object has no attribute 'sort'
print(b)
c = (4, 3, 2, 1)
c.sort()  # error: 'tuple' object has no attribute 'sort'
print(c)
# reverse sort
a.sort(reverse=True)
print(a)
# 3.4.2 sorting a list temporarily with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)
# 基本上来说，list.function()是发生永久变化，function（list）是短暂变化
# printing a list in reverse order,但是不再排序了，单纯reverse
cars.reverse()
print(cars)
# length
# 如果只有单行，系统默认print，所以在一行的情况下，len（）也能出结果
for i in range(5):
    print(len(cars))


# Customize Sort Function
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]

thislist.sort(key=myfunc)

print(thislist)  # [50, 65, 23, 82, 100]
# Copy a List
# You cannot copy a list simply by typing list2 = list1, because:
# list2 will only be a reference to list1, and changes made in list1 will 
# automatically also be made in list2.
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# practice
# 1
Place = ['China', 'USA', 'UK', 'EU', 'Ruassia']
print(Place)
sorted(Place)
print(Place)
Place.reverse()
print(Place)
Place.reverse()
print(Place)
Place.sort()
print(Place)
Place.sort(reverse=True)
print(Place)
# 2
print(len(NameList))

# 4.0 working with list

# 4.1 looping through an entire list
magicians = ['alice', 'david', 'carolina']
for i in magicians:
    print(i)
# 4.1.1 doing sth after a loop
for i in magicians:
    print(i.title() + ", that was a great trick")
    print("I can't wait to see your next trick, " + i.title() + ".\n")
# practice1
pizzas = ['a', 'b', 'c']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza.')
print('I really love pizzas.')
# practice2
animals = ['cat', 'dog', 'pig']
for animal in animals:
    print('A ' + animal + ' would make a great pet.')
print('Any of these animals would make a great pet.')

# 4.2 making numeric lists
# 4.2.1 using range() function
# the range() function cause python to start counting
# at the first value you gice it, and stops when it reach
# the second value you provide, never contain the second value.
for value in range(1, 5):
    print(value)
for value in range(5):
    print(value)
# 4.2.2 using range() to make a list of numbers
numbers = list(range(5))
print(numbers)
# range(start,stop,step)
EvenNumbers = list(range(0, 5, 2))
print(EvenNumbers)
# real problem
cubes = []
for i in range(11):
    cube = i ** 2
    cubes.append(cube)
    print(cubes)
# 4.2.3 simple statistics with a list of numbers
digits = list(range(1, 10))
digits.append(0)
print(digits)
min(digits)
max(digits)
sum(digits)
# 4.2.4list comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)
[print(i) for i in range(10)]
# practice1
for i in range(1, 21):
    print(i)
# practice2
a = list(range(1, 1000001))
for i in a:
    print(i)
# practice3
min(a)
max(a)
sum(a)
# practice4
for i in range(1, 20, 2):
    print(i)
# practice5
for i in range(1, 11):
    print(3 * i)
# practice6
for i in range(1, 11):
    print(i ** 3)
# practice7
TenCubes = [i ** 3 for i in range(1, 11)]
print(TenCubes)

# 4.2.5 generator
import sys

nums_squared_lc = [i * 2 for i in range(10000)]
sys.getsizeof(nums_squared_lc)  # 87624

nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))  # 120

# count hashable objects cith collections.Counter
from collections import Counter

my_list = [10, 10, 10, 5, 5, 2, 9, 9, 9, 9, 9, 9]
counter = Counter(my_list)
print(counter)
print(counter[10])  # 3
print(counter[11])  # 0
most_common = counter.most_common(1)  # 1: count most common number; 2: most 2 common numbers.
print(most_common)

# 4.3 working with part of a list
# 4.3.1 slicing a list
# 切片包括左不包括右
players = ['a', 'b', 'c', 'd', 'e']
print(players[:-2])
# 4.3.2 looping through a slice
for player in players[:3]:
    print(player.title())
# 4.3.3 copying a list
# 这里不能用=，因为=的意思是这两个变量一直一样。
playersB = players[:]
print(playersB)
a = players
a.append('f')
print(players)
a = 1
b = a
b += 1
print(a)
print(b)
# practice1
print(players[:3])
print(players[3:6])
print(players[-3:])

# 4.4 tuples(a list of item that can't change (immutable))
# 当元组不是空元组时，括号可以省略
# 如果元组不是空元组，它里边至少要有一个,
my_tuple = 10,20,30,40
my_tuple = 40,
# 元组的解包（解构）
# 解包指就是将元组当中每一个元素都赋值给一个变量
a,b,c,d = my_tuple
# 交互a 和 b的值，这时我们就可以利用元组的解包
a , b = b , a
# 在对一个元组进行解包时，变量的数量必须和元组中的元素的数量一致
# 也可以在变量前边添加一个*，这样变量将会获取元组中所有剩余的元素
a , b , *c = my_tuple
a , *b , c = my_tuple
*a , b , c = my_tuple
a , b , *c = [1,2,3,4,5,6,7]
a , b , *c = 'hello world'
# 不能同时出现两个或以上的*变量
# *a , *b , c = my_tuple SyntaxError: two starred expressions in assignment
print('a =',a)
print('b =',b)
print('c =',c)
# 4.4.1 an immutable list is called a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
dimensions[0] = 250  # error: tuple object doesn't support item assignment
# 4.4.2 looping through all values in a tuple
for dimension in dimensions:
    print(dimension)
# 4.4.3 writing over a tuple
# although you can't modify a tuple, you can assign a
# new value to a variable that holds a tuple.
dimensions = (200, 50)
print(dimensions)
dimensions = (400, 100)
print(dimensions)
# 4.5 Using the random.choice() and random.shuffle() Functions with Lists
import random

pets = ['dog', 'cat', 'moose']
random.choice(pets)
# same effect
pets[random.randint(0, 3)]
# shuffle
random.shuffle(pets)
pets
# practice
foods = ('hamburger', 'sandiwich', 'steak', 'pasta', 'pizza')
for food in foods:
    print(food)
foods = ('hamburger', 'sandiwich', 'steak', 'Fish and Chips', 'Shrimp')
for food in foods:
    print(food)

# 4.6 Sequence Data Types
name = 'Zophie'
name[0]
name[-2]
name[0:4]
# case sensitive
'Zo' in name
'z' in name

# 4.7 Mutable and Immutable Data Types
# A list value is a mutable data type: it can have values added, removed, or changed. However, a string is immutable
name = 'Zophie a cat'
name[7] = 'the'  # TypeError: 'str' object does not support item assignment
# The proper way to “mutate” a string
newName = name[0:7] + 'the' + name[8:12]
# List Method (change original list)
append()  # Adds an element at the end of the list
clear()  # Removes all the elements from the list
extend()  # Add the elements of a list (or any iterable), to the end of the current list
insert()  # Adds an element at the specified position
pop()  # Removes the element at the specified position
remove()  # Removes the item with the specified value
reverse()  # Reverses the order of the list
sort(reverse=False)  # Sorts the list, default value False, can change to true. cannot sort between str and int; capital
# at first and then lower case.
sort(key=str.lower)  # doesn't consider upper or lower case for strings.
# sort dictionary
data = [{'name': 'max', 'age': 6},
        {'name': 'lisa', 'age': 20},
        {'name': 'ben', 'age': 9}]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)
# doesn't change list
copy()  # Returns a copy of the list
count()  # Returns the number of elements with the specified value
index()  # Returns the index of the first element with the specified value

# 5 if statement
# 关系运算符
# 关系运算符用来比较两个值之间的关系，总会返回一个布尔值
# 如果关系成立，返回True，否则返回False
# > 比较左侧值是否大于右侧值
# >= 比较左侧的值是否大于或等于右侧的值
# < 比较左侧值是否小于右侧值
# <= 比较左侧的值是否小于或等于右侧的值
# == 比较两个对象的值是否相等
# != 比较两个对象的值是否不相等
#   相等和不等比较的是对象的值，而不是id
# is 比较两个对象是否是同一个对象，比较的是对象的id
# is not 比较两个对象是否不是同一个对象，比较的是对象的id
# 在Python中可以对两个字符串进行大于（等于）或小于（等于）的运算，
#   当对字符串进行比较时，实际上比较的是字符串的Unicode编码
#   比较两个字符串的Unicode编码时，是逐位比较的
#   利用该特性可以对字符串按照字母顺序进行排序，但是对于中文来说意义不是特别大
#   注意：如果不希望比较两个字符串的Unicode编码，则需要将其转换为数字然后再比较
#   0061 > 0062
# not 逻辑非
#   not可以对符号右侧的值进行非运算
#       对于布尔值，非运算会对其进行取反操作，True变False，False变True
#       对于非布尔值，非运算会先将其转换为布尔值，然后再取反
#
# and 逻辑与
#   and可以对符号两侧的值进行与运算
#    只有在符号两侧的值都为True时，才会返回True，只要有一个False就返回False
#    与运算是找False的
#    Python中的与运算是短路的与，如果第一个值为False，则不再看第二个值
#
# or 逻辑或
#   or 可以对符号两侧的值进行或运算
#    或运算两个值中只要有一个True，就会返回True
#    或运算是找True的
#    Python中的或运算是短路的或，如果第一个值为True，则不再看第二个值
# True and True
result = 1 and 2 # 2
# True and False
result = 1 and 0 # 0
# False and True
result = 0 and 1 # 0
# False and False
result = 0 and None # 0

# True or True
result = 1 or 2 # 1
# True or False
result = 1 or 0 # 1
# False or True
result = 0 or 1 # 1
# False or False
result = 0 or None # None
# 通过条件运算符获取三个值中的最大值
# max = a if a > b else b
# max = max if max > c else c

max = a if (a > b and a > c) else (b if b > c else c) # 不推荐这么使用
# 运算符的优先级
# 和数学中一样，在Python运算也有优先级，比如先乘除 后加减
# 运算符的优先级可以根据优先级的表格来查询，
#   在表格中位置越靠下的运算符优先级越高，优先级越高的越优先计算
#   如果优先级一样则自左向右计算
#  关于优先级的表格，你知道有这么一个东西就够了，千万不要去记 https://www.programiz.com/python-programming/precedence-associativity
#  在开发中如果遇到优先级不清楚的,则可以通过小括号来改变运算顺序
# 逻辑运算符（补充）
# 逻辑运算符可以连着使用
result = 1 < 2 < 3 # 相当于 1 < 2 and 2 < 3
result = 10 < 20 > 15


# 5.1 a simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# 5.2 conditional test
# 5.2.1 checking for equality
# a single equal line is a statement
# a double equal line is a condition
car = 'bmw'
car == 'bmw'  # true
car == 'audi'  # false
# 5.2.1.1 ignoring case when checking for equality
car == 'BMW'  # false
# if case doesn't matter and you want to test the value
# of a variable, you can convert the variable case.
car.upper() == 'BMW'  # True
# 5.2.2 checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies')
# 5.2.3 Numerical Comparisons
age = 18
age == 18
answer = 17
if answer != 42:
    print('That is not correct answer. Please try again!')
age = 19
age < 21
age <= 21
age > 21
age >= 21
# 5.2.4 checking multiple conditions (and, or)
Age0 = 22
Age1 = 18
Age0 >= 21 and Age1 >= 21
Age1 = 22
Age0 >= 21 and Age1 >= 21
Age0 >= 21 or Age1 >= 21
Age0 = 18
Age1 = 18
Age0 >= 21 or Age1 >= 21
# 5.2.5 checking whether a value is in a list
a = ['c', 'v', 'b', 'n', 'm']
'c' in a
't' in a
# 5.2.6 checking whether a value is not in a list
'c' not in a
't' not in a
# 5.2.7 boolean expressions
# most values are true
# In fact, there are not many values that evaluate to False,
# except empty values, such as (), [], {}, "", the
# number 0, and the value None. And of course the value
# False evaluates to False.
bool()


# function can return boolean
def myFunction():
    return True


print(myFunction())
# You can execute code based on the Boolean answer of a function
if myFunction():
    print('yes')
else:
    print('no')
# Python also has many built-in functions that return
# a boolean value, like the isinstance() function,
# which can be used to determine if an object is of
# a certain data type:
x = 200
print(isinstance(x, int))

# 5.3 If statement
# 5.3.1 simple if statements
age = 19
if age >= 18:
    print('you are old enough to vote!')
# 5.3.2 if-else statements
age = 17
if age >= 18:
    print('you are old enough to vote!')
else:
    print('sorry, you are too young to vote.')
# if-elif-else
age = 12
if age < 4:
    print('your admission cost is 0.')
elif age < 18:
    print('your admission cost is 5.')
else:
    print('you admission cost is 10.')
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:  # elif can be anything not in if condition!
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:  # elif can cover if range, this is equal to 100 < age < 2000.
    print('You are not Alice, grannie.')
# using multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print(price)
# else doesn't have to be in the if-elif chain.
# practice1
AlienColors = ['green', 'yellow', 'red']
for AlienColor in AlienColors:
    if AlienColor == 'green':
        print('the player just earned 5 points.')
    elif AlienColor == 'yellow':
        print('the player just earned 10 points.')
    elif AlienColor == 'red':
        print('the player just earned 15 points.')
# practice2
age = 32
if age < 2:
    print('baby')
elif age < 4:
    print('toddler')
elif age < 13:
    print('kid')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adult')
else:
    print('elder')
# practice3
fruits = ['apple', 'banana', 'Mangle']
if 'apple' in fruits:
    print('apple is in the list.')
if 'banana' in fruits:
    print('banana is in the list.')
if 'Mangle' in fruits:
    print('Mangle is in the list.')
if 'apple' not in fruits:
    print('apple is not in the list.')

# 5.4 using if statements with list
# 5.4.1 checking for special items
foods = ['a', 'b', 'c', 'd', 'e']
for food in foods:
    if food == 'c':
        print('Sorry, we are running out of c right now.')
    else:
        print(food.title() + ' is ready for you.')
# 5.4.2 checking that a list is not empty
# check whether a list is empty before running a for loop.
# 如果if加空值，会直接跑到else的结果
foods = []
if foods:
    for food in foods:
        print('adding ' + food + '.')
    print('\nFinished making your pizza!')
else:
    print('are u sure u want a plain pizza?')
# 5.4.3 using multiple lists
AvaliableFoods = ['a', 'b', 'c', 'd', 'e', 'f']
RequestedFoods = ['a', 'r', 'f']
for food in RequestedFoods:
    # 如果in的话，return True，执行if的statement；
    # 否则，return False，执行else的statement。
    if food in AvaliableFoods:
        print('Adding ' + food + '.')
    else:
        print("Sorry, we don't have " + food + ".")
print('\nFinished making your pizza!')
# practice1
usernames = ['a', 'b', 'c', 'd', 'e', 'admin']
for name in usernames:
    if name != 'admin':
        print('Hello ' + name + ', thank you for logging in again.')
    else:
        print('Hello admin, would you like o see a status report?')
# practice2
for i in range(6):
    usernames.pop(0)
print(usernames)
if usernames:
    for name in names:
        print('adding ' + name + '.')
else:
    print('we need to find some users!')
# practice3
CurrentUsers = ['a', 'b', 'c', 'd', 'e', 'admin']
NewUsers = ['a', 'b', 'f', 'g', 'h']
for user in CurrentUsers:
    user.lower()
for user in NewUsers:
    user.lower()
for user in NewUsers:
    if user in CurrentUsers:
        print('You need a new username.')
    else:
        print('Your username is avaliable.')
# practice4
Numberlist = list(range(1, 10))
for i in Numberlist:
    if i == 1:
        print('1st')
    elif i == 2:
        print('2nd')
    elif i == 3:
        print('3rd')
    else:
        print(str(i) + 'th')

# 5.5 condition in loop
for item in mylist:
    if item.flavor == 'banana':  # if none of the item's flavor is banana, go to else.
        break
else:  # the else block will run only if and when the for loop runs to completion.
    raise ValueError('No banana flavor found!')

try:
    dangerous_call()
except OSError:
    log('OSError...')
else:  # the else block will run only if no exception is raised in the try block
    after_call()

# 6.0 dictionaries
# - 字典属于一种新的数据结构，称为映射（mapping）
# - 字典的作用和列表类似，都是用来存储对象的容器
# - 列表存储数据的性能很好，但是查询数据的性能的很差
# - 在字典中每一个元素都有一个唯一的名字，通过这个唯一的名字可以快速的查找到指定的元素
# - 在查询元素时，字典的效率是非常快的
# 使用 dict()函数来创建字典
# 每一个参数都是一个键值对，参数名就是键，参数名就是值（这种方式创建的字典，key都是字符串）
d = dict(name='孙悟空',age=18,gender='男')
# 也可以将一个包含有双值子序列的序列转换为字典
# 双值序列，序列中只有两个值，[1,2] ('a',3) 'ab'
# 子序列，如果序列中的元素也是序列，那么我们就称这个元素为子序列
# [(1,2),(3,5)]
d = dict([('name','孙悟饭'),('age',18)])
# 6.1 a simple dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# 6.2 adding new key value pair
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 6.3 starting with an empty dictionary
# key or value can also be integer
a = {}
a[1] = []
a[2] = []
a[1].append(2)
a[1].append(3)
print(a)
# 6.4 modifying values in a dictionary
alien_0['color'] = 'yellow'
print(alien_0)
alien_0['speed'] = 'medium'
print(alien_0)
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be fast
    x_increment = 3
# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0)
# 6.5 removing key value pair
del alien_0['points']
print(alien_0)
# 6.6 a dictionary of similar objects
FavoriteLanguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(FavoriteLanguages)
# practice1
Susan = {'FirstName': 'Susan',
         'LastName': 'Tang',
         'age': 22,
         'city': 'Auckland'}
print(Susan)
# practice2
Numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for key, value in Numbers.items():
    print(key, value)
# practice3
programs = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 6.7 looping through a dictionary
# 6.7.1 looping through all key-value pairs
User0 = {'username': 'Susan',
         'first': 'Susan',
         'last': 'Tang'}
for key, value in User0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)
# code can also be
for k, v in User0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

for name, languages in FavoriteLanguages.items():
    print(name.title() +
          "'s favorite language is "
          + languages.title() + '.')
# 6.7.2 looping through all the keys in a dictionary
for name in FavoriteLanguages.keys():
    print(name.title())
# it is the same as
for name in FavoriteLanguages:
    print(name.title())
# complex
friend = ['phil', 'sarah']
for name in FavoriteLanguages.keys():
    print(name.title())
    if name in friend:
        print(' Hi ' + name.title() +
              ', I see your favourite language is '
              + FavoriteLanguages[name].title() + '!')
# 6.7.3 looping through a dictionary's keys in order
for name in sorted(FavoriteLanguages.keys()):
    print(name.title() + ', thank you for taking the poll.')
# 6.7.4 looping through all values in a dictionary
for language in FavoriteLanguages.values():
    print(language.title())
# for value without repetation: set()
for language in set(FavoriteLanguages.values()):
    print(language.title())
a = {1: [1, 2, 3], 2: [2, 3, 4], 3: [3, 4, 5]}
for i in a.values():
    for i1 in i:
        print(i1)

a = {1: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]}
# 通过key取出来的value是list
a[1]
for i in a[1]:
    print(i)
    for i1 in i:
        print(i1)
b = a.values()
# 这里的values包含两个中括号，[[[1, 2, 3], [2, 3, 4], [3, 4, 5]]]
print(type(b))
# <class 'dict_values'>
# 这里可以看出dictionary的value并不直接是list
# 所以要先变成list
c = list(b)
print(c[0])
# c在转成list后可以通过【0】拆一个括号
# [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
# 最后再遍历所有里面的值
for i in c[0]:
    for i1 in i:
        print(i1)

# practice1
a = {'a': 1, 'b': 2, 'c': 3}
for k, v in a.items():
    print(k + ' is equal to ' + str(v) + '.')
for key in a.keys():
    print(key)
for value in a.values():
    print(value)
# practice2
friend = ['phil', 'sarah', 'a', 'b']
for i in friend:
    if i in FavoriteLanguages.keys():
        print('thank ' + i)
    else:
        print('invite ' + i)

# 6.8 Nesting
# 6.8.1 A list of Dictionary
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 4, 'b': 5, 'c': 6}
d3 = {'a': 7, 'b': 8, 'c': 9}
L = [d1, d2, d3]
for i in L:
    print(i)
# 6.8.2 A list in Dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra chess']
}
print('You ordered a ' + pizza['crust'] +
      '-crust pizza ' + 'with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)
FavoriteLanguages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']}
for name, languages in FavoriteLanguages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
# 6.8.3 A dictionary in dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for UserName, UserInfo in users.items():
    print("\nUsername: " + UserName)
    FullName = UserInfo['first'] + " " + UserInfo['last']
    location = UserInfo['location']

    print("\tFull name: " + FullName.title())
    print("\tlocation: " + location.title())
# practice1
cat = {
    'kind': 'cat',
    'OwnerName': 'Jack'
}
mouse = {
    'kind': 'mouse',
    'OwnerName': 'Susan'
}
dog = {
    'kind': 'dog',
    'OwnerName': 'Emily'
}
pets = [cat, mouse, dog]
for pet in pets:
    print(pet)
# practice2
FavoritePlace = {
    1: [1, 2, 3],
    2: [2, 3, 4],
    3: [3, 4, 5]
}
for k, v in FavoritePlace.items():
    print(str(k) + "'s favorite place is ")
    for v1 in v:
        print(v1)
# practice3
cities = {
    'Beijing': {
        'country': 'china',
        'population': '100',
        'fact': 'busy'
    },
    'Tianjin': {
        'country': 'china',
        'population': '200',
        'fact': 'relax'
    },
    'Hebei': {
        'country': 'china',
        'population': '300',
        'fact': 'polluted'
    }
}
for k, v in cities.items():
    print(k)
    for v1 in v:
        print(v)

# 6.9 the get() method
picnicItems = {'apples': 5, 'cups': [2, 9]}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')

'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'  # if no this key, get() give 0.

# setdefault() method
# set a value in a dictionary for a certain key only if that key does not already have a value
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
# short program that counts the number of occurrences of each letter in a string
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
import pprint

pprint.pprint(count)

# 6.10 merge two dictionary
d1 = {"name": ["Alex", "Jack"], "age": 25}
d2 = {"name": ["Alex"], "city": "new york"}
merged_dic = {**d1, **d2}
print(merged_dic)


# Merge two dictionaries and add values of common keys
def mergeDict(dict1, dict2):
    ''' Merge dictionaries and keep values of common keys in list'''
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = [value, dict1[key]]
    return dict3


dict3 = mergeDict(d1, d2)
print('Dictionary 3 :')
print(dict3)

# 7.0 using input and while loop
# 7.1 how the input() function work
message = input('tell me sth, and i will: ')
print(message)
# 7.1.1 writing clear prompts
name = input('please enter your name: ')
print('Hello, ' + name + '!')
# 7.1.2 using int() to accept numeric input
age = input('How old are you? ')
age = int(age)
# 7.2 the modulo operator
4 % 3
5 % 3
6 % 3
# 7.3 while loop
# 7.3.1 the while loop runs as long as a certain condition is true
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# 7.3.2 using a flag
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
# 7.3.3 using whole loop with lists and dictionaries
# 7.3.3.1 moving items from one list to another
# while can be connectted to a list to run until
# nothing in this list.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# 7.3.3.2 removing all instances of specific value from a list
pets = [1, 2, 3, 2, 4, 5, 2]
while 2 in pets:
    pets.remove(2)
print(pets)
# 7.3.3.3 filling a dictionary with user input
responses = {}
# set a flag to indicate that polling is active
polling_active = True
while polling_active:
    # prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("which mountain you like? ")
    # store response in the dictionary
    responses[name] = response
    # find out if anyone else is going to take the poll
    repeat = input("u wanna another respond? ")
    if repeat == 'no':
        polling_active = False
for name, response in responses.items():
    print(name + response)
# practice1
sandiwich_orders = [1, 2, 3, 4, 5]
finished_sandiwiches = []
while sandiwich_orders:
    finished_sandiwiches.append(sandiwich_orders.pop())
print(finished_sandiwiches)


# 7.4 Set集合
"""- 集合和列表非常相似
- 不同点：
    1.集合中只能存储不可变对象
    2.集合中存储的对象是无序（不是按照元素的插入顺序保存）
    3.集合中不能出现重复的元素"""
# 使用 {} 来创建集合
s = {10,3,5,1,2,1,2,3,1,1,1,1} # <class 'set'>
# s = {[1,2,3],[4,6,7]} TypeError: unhashable type: 'list'
# 使用 set() 函数来创建集合
s = set() # 空集合
# 可以通过set()来将序列和字典转换为集合
s = set([1,2,3,4,5,1,1,2,3,4,5])  # there is no replicate in set
s = set('hello')
s = set({'a':1,'b':2,'c':3}) # 使用set()将字典转换为集合时，只会包含字典中的键

# 创建集合
s = {'a' , 'b' , 1 , 2 , 3 , 1}

# 使用in和not in来检查集合中的元素
print('c' in s)  # False

# 使用len()来获取集合中元素的数量
print(len(s))  # 5

# add() 向集合中添加元素, has to be one element
s.add(10)
s.add(30)

# update() 将一个集合中的元素添加到当前集合中
#   update()可以传递序列或字典作为参数，字典只会使用键
s2 = set('hello')
s.update(s2)
s.update((10,20,30,40,50))
s.update({10:'ab',20:'bc',100:'cd',1000:'ef'})

# {1, 2, 3, 100, 40, 'o', 10, 1000, 'a', 'h', 'b', 'l', 20, 50, 'e', 30}
# pop()随机删除并返回一个集合中的元素
# result = s.pop()

# remove()删除集合中的指定元素
s.remove(100)
s.remove(1000)

# clear()清空集合
s.clear()

# copy()对集合进行浅复制

# 在对集合做运算时，不会影响原来的集合，而是返回一个运算结果
# 创建两个集合
s = {1,2,3,4,5}
s2 = {3,4,5,6,7}

# & 交集运算
result = s & s2 # {3, 4, 5}

# | 并集运算
result = s | s2 # {1,2,3,4,5,6,7}

# - 差集
result = s - s2 # {1, 2}

# ^ 异或集 获取只在一个集合中出现的元素
result = s ^ s2 # {1, 2, 6, 7}

# <= 检查一个集合是否是另一个集合的子集
# 如果a集合中的元素全部都在b集合中出现，那么a集合就是b集合的子集，b集合是a集合超集
a = {1,2,3}
b = {1,2,3,4,5}

result = a <= b # True
result = {1,2,3} <= {1,2,3} # True
result = {1,2,3,4,5} <= {1,2,3} # False

# < 检查一个集合是否是另一个集合的真子集
# 如果超集b中含有子集a中所有元素，并且b中还有a中没有的元素，则b就是a的真超集，a是b的真子集
result = {1,2,3} < {1,2,3} # False
result = {1,2,3} < {1,2,3,4,5} # True

# >= 检查一个集合是否是另一个的超集
# > 检查一个集合是否是另一个的真超集
print('result =',result)


# 8.0 functions
"""函数简介（function）
- 函数也是一个对象
- 对象是内存中专门用来存储数据的一块区域  # fn是函数对象  fn()调用函数 print是函数对象 print()调用函数
- 函数可以用来保存一些可执行的代码，并且可以在需要时，对这些语句进行多次的调用
- 创建函数：
    def 函数名([形参1,形参2,...形参n]) :
        代码块
    - 函数名必须要符号标识符的规范
        （可以包含字母、数字、下划线、但是不能以数字开头）    
- 函数中保存的代码不会立即执行，需要调用函数代码才会执行
- 调用函数：
    函数对象()
- 定义函数一般都是要实现某种功能的    
函数的参数
- 在定义函数时，可以在函数名后的()中定义数量不等的形参，
    多个形参之间使用,隔开
- 形参（形式参数），定义形参就相当于在函数内部声明了变量，但是并不赋值
- 实参（实际参数）
    - 如果函数定义时，指定了形参，那么在调用函数时也必须传递实参，
        实参将会赋值给对应的形参，简单来说，有几个形参就得传几个实参
    
函数式编程
- 在Python中，函数是一等对象
- 一等对象一般都会具有如下特点：
    ① 对象是在运行时创建的
    ② 能赋值给变量或作为数据结构中的元素
    ③ 能作为参数传递
    ④ 能作为返回值返回

- 高阶函数
    - 高阶函数至少要符合以下两个特点中的一个
      ① 接收一个或多个函数作为参数
      ② 将函数作为返回值返回 

- 装饰器         """

def greet_user():
    print('hello')
greet_user()

# Local Scopes Cannot Use Variables in Other Local Scopes
def bacon():
    ham = 101
    eggs = 0

def spam():
    eggs = 99
    bacon()
    print(eggs)
spam()

# The global Statement
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

# 8.1 passing information to a function
def greet_user(username):
    print('hello, ' + username.title() + '!')

greet_user('Jacky')

# pracrtice1
def display_message(message):
    print(message)

message1 = 'I learn nothing.'
display_message(message1)

# practice2
def favorite_books(title):
    print('one of my favorite book is ' + title.title() + '.')

name = 'machine learning'
favorite_books(name)

# 8.1 passing argument
def describe_pet(pet_type, name):
    if pet_type[0] != 'a' and pet_type[0] != 'e' and pet_type[0] != 'i' and pet_type[0] != 'o' and pet_type[0] != 'u':
        print('my pet is a ' + pet_type
              + ', and its name is ' + name.title() + '.')
    else:
        print('my pet is an ' + pet_type
              + ', and its name is ' + name.title() + '.')

describe_pet('cat', 'kitty')
describe_pet('elephant', 'ele')
# 8.2 key word arguments
# you don't have to consider order but you need specify parameter name.
describe_pet(name='ele', pet_type='elephant')

# 8.3 Default values
# put value in braces of the function as default value
"""if we need mutable parameter, we must give None to default value"""
def describe_pet(pet_type='dog', name='doggy'):
    if pet_type[0] != 'a' and pet_type[0] != 'e' and pet_type[0] != 'i' and pet_type[0] != 'o' and pet_type[0] != 'u':
        print('my pet is a ' + pet_type
              + ', and its name is ' + name.title() + '.')
    else:
        print('my pet is an ' + pet_type
              + ', and its name is ' + name.title() + '.')

describe_pet()

# 8.4 equivalent function calls
# if there are two parameters in a function, one
# has default, but one not. When you call function,
# you can just give one value to the parameter 
# that doesn't have default value.
def describe_pet(pet_type, name='doggy'):
    if pet_type[0] != 'a' and pet_type[0] != 'e' and pet_type[0] != 'i' and pet_type[0] != 'o' and pet_type[0] != 'u':
        print('my pet is a ' + pet_type
              + ', and its name is ' + name.title() + '.')
    else:
        print('my pet is an ' + pet_type
              + ', and its name is ' + name.title() + '.')

describe_pet('dog')

# 8.5 avoiding argument error
# if there is no default value, you have to give 
# value to parameters
# practice1
def make_shirt(size, text):
    print(size + text)

# 8.6 return values
# 返回值，返回值就是函数执行以后返回的结果
# 可以通过 return 来指定函数的返回值
# 可以之间使用函数的返回值，也可以通过一个变量来接收函数的返回值

def sum(*nums):
    # 定义一个变量，来保存结果
    result = 0
    # 遍历元组，并将元组中的数进行累加
    for n in nums:
        result += n
    print(result)

sum(123,456,789)

# return 后边跟什么值，函数就会返回什么值
# return 后边可以跟任意的对象，返回值甚至可以是一个函数
def fn():
    # return 'Hello'
    # return [1,2,3]
    # return {'k':'v'}
    def fn2():
        print('hello')
    return fn2  # 返回值也可以是一个函数

r = fn()  # 这个函数的执行结果就是它的返回值

r()
print(fn())
print(r)

# 如果仅仅写一个return 或者 不写return，则相当于return None
def fn2():
    a = 10
    return


# 在函数中，return后的代码都不会执行，return 一旦执行函数自动结束
def fn3():
    print('hello')
    return
    print('abc')


r = fn3()
print(r)

def fn4():
    for i in range(5):
        if i == 3:
            # break 用来退出当前循环
            # continue 用来跳过当次循环
            return  # return 用来结束函数
        print(i)
    print('循环执行完毕！')

fn4()

def sum(*nums):
    # 定义一个变量，来保存结果
    result = 0
    # 遍历元组，并将元组中的数进行累加
    for n in nums:
        result += n
    return result

r = sum(123, 456, 789)
print(r + 778)

def fn5():
    return 10

# fn5 和 fn5()的区别
print(fn5)  # fn5是函数对象，打印fn5实际是在打印函数对象 <function fn5 at 0x05771BB8>
print(fn5())  # fn5()是在调用函数，打印fn5()实际上是在打印fn5()函数的返回值 10


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('Jacky', 'Liu')
print(musician)

# 8.6.1 making an argument option
# have to have a default argument after default argument
def get_formatted_name(first_name, middle_name='', last_name='Liu'):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'Lee', 'hooker')
print(musician)
musician1 = get_formatted_name('john', 'Lee')
print(musician1)

# returning a dictionary
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jacky', 'liu')
print(musician)

def build_person(first_name, last_name, age=8):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jacky', 'liu')
misucian1 = build_person('Jacky', 'Liu', 27)
print(musician)
print(misucian1)

# using a function with a while loop
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

while True:
    f_name = input("firstname: ")
    l_name = input("lastname: ")
    print(build_person(f_name, l_name))
    if f_name == 'q' or l_name == 'q':
        break

# practice1
def city_country(city, country):
    print(city + ' ' + country)

cc = {'beijing': 'China', 'Auckland': 'Newzealand',
      'glasgow': 'UK'}
for city, country in cc.items():
    city_country(city, country)

# practice2
def make_album(artist, album):
    person = {'first': artist, 'last': album}
    return person

# 8.6.2 passing a list
def greet_user(names):
    for name in names:
        msg = name.title()
        print(msg)

usernames = ['a', 'b', 'c']
greet_user(usernames)

# 8.6.2.1 modifying a list in a function
# you can input an empty list into a function
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)

def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['a', 'b', 'c']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.6.2.2 preventing a function from modifying a list
# if we don't wanna change the original list,
# we can use copied list to proceed function by [:].
print_models(unprinted_designs[:], completed_models)

# 8.7 passing an arbitrary number of arguments
# the asterisk in the parameter tells python to 
# make an empty tuple called toppings and pack 
# whatever values it recieves into this tuple.
# 不定长的参数
# 定义一个函数，可以求任意个数字的和
def sum(*nums):
    # 定义一个变量，来保存结果
    result = 0
    # 遍历元组，并将元组中的数进行累加
    for n in nums:
        result += n
    print(result)

sum(123,456,789,10,20,30,40)

# 在定义函数时，可以在形参前边加上一个*，这样这个形参将会获取到所有的实参
# 它将会将所有的实参保存到一个元组中
a,b,*c = (1,2,3,4,5,6)

# *a会接受所有的位置实参，并且会将这些实参统一保存到一个元组中（装包）
def fn(*a):
    print("a =",a,type(a))

fn(1,2,3,4,5)
# 带星号的形参只能有一个
# 带星号的参数，可以和其他参数配合使用
# 第一个参数给a，第二个参数给b，剩下的都保存到c的元组中
def fn2(a,b,*c):
    print('a =',a)
    print('b =',b)
    print('c =',c)

# 可变参数不是必须写在最后，但是注意，带*的参数后的所有参数，必须以关键字参数的形式传递
# 第一个参数给a，剩下的位置参数给b的元组，c必须使用关键字参数
def fn2(a,*b,c):
    print('a =',a)
    print('b =',b)
    print('c =',c)

# 所有的位置参数都给a，b和c必须使用关键字参数
def fn2(*a,b,c):
    print('a =',a)
    print('b =',b)
    print('c =',c)

# 如果在形参的开头直接写一个*,则要求我们的所有的参数必须以关键字参数的形式传递
def fn2(*,a,b,c):
    print('a =',a)
    print('b =',b)
    print('c =',c)
fn2(a=3,b=4,c=5)

# *形参只能接收位置参数，而不能接收关键字参数
def fn3(*a) :
    print('a =',a)

def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 8.8 mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    print(str(size))
    for topping in toppings:
        print(topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.9 using arbitrary keyword arguments
# **形参可以接收其他的关键字参数，它会将这些参数统一保存到一个字典中
#   字典的key就是参数的名字，字典的value就是参数的值
# **形参只能有一个，并且必须写在所有参数的最后
def fn3(b,c,**a) :
    print('a =',a,type(a))
    print('b =',b)
    print('c =',c)

fn3(b=1,d=2,c=3,e=10,f=20)

# 参数的解包（拆包）
def fn4(a,b,c):
    print('a =',a)
    print('b =',b)
    print('c =',c)

# 创建一个元组
t = (10,20,30)

# 传递实参时，也可以在序列类型的参数前添加星号，这样他会自动将序列中的元素依次作为参数传递
# 这里要求序列中元素的个数必须和形参的个数的一致
fn4(*t)

# 创建一个字典
d = {'a':100,'b':200,'c':300}
# 通过 **来对一个字典进行解包操作
fn4(**d)
# 2 asterisk helps accept as many name-value pairs
# as we want
def build_profile(first, last, **user_info):
    profile = {}
    profile['fist_name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Jacky', 'Liu',
                             location='China',
                             field='finance')
print(user_profile)

# 8.9half how to add instructions to a function:
# help()是Python中的内置函数
# 通过help()函数可以查询python中的函数的用法
# 语法：help(函数对象)
# help(print) # 获取print()函数的使用说明

# 文档字符串（doc str）
# 在定义函数时，可以在函数内部编写文档字符串，文档字符串就是函数的说明
#   当我们编写了文档字符串时，就可以通过help()函数来查看函数的说明
#   文档字符串非常简单，其实直接在函数的第一行写一个字符串就是文档字符串
def fn(a:int,b:bool,c:str='hello') -> int:
    '''
    这是一个文档字符串的示例

    函数的作用：。。。。。
    函数的参数：
        a，作用，类型，默认值。。。。
        b，作用，类型，默认值。。。。
        c，作用，类型，默认值。。。。
    '''
    return 10

help(fn)

# 8.9halfhalf 作用域（scope）
# 作用域指的是变量生效的区域
b = 20  # 全局变量


def fn():
    a = 10  # a定义在了函数内部，所以他的作用域就是函数内部，函数外部无法访问
    print('函数内部：', 'a =', a)
    print('函数内部：', 'b =', b)

fn()

print('函数外部：','a =',a)  # not defined
print('函数外部：','b =',b)

# 在Python中一共有两种作用域
#  全局作用域
#   - 全局作用域在程序执行时创建，在程序执行结束时销毁
#   - 所有函数以外的区域都是全局作用域
#   - 在全局作用域中定义的变量，都属于全局变量，全局变量可以在程序的任意位置被访问
#
#  函数作用域
#   - 函数作用域在函数调用时创建，在调用结束时销毁
#   - 函数每调用一次就会产生一个新的函数作用域
#   - 在函数作用域中定义的变量，都是局部变量，它只能在函数内部被访问
#
#  变量的查找
#   - 当我们使用变量时，会优先在当前作用域中寻找该变量，如果有则使用，
#       如果没有则继续去上一级作用域中寻找，如果有则使用，
#       如果依然没有则继续去上一级作用域中寻找，以此类推
#       直到找到全局作用域，依然没有找到，则会抛出异常
#           NameError: name 'a' is not defined
a = 100
def fn2():
    a = 10
    def fn3():
        a = 20
        print('fn3中:', 'a =', a)
    fn3()
    print('fn2中:', 'a =', a)
fn2()
print('global中:', 'a =', a)
# fn3中: a = 20
# fn2中: a = 10
# global中: a = 100

a = 20
def fn3():
    # a = 10 # 在函数中为变量赋值时，默认都是为局部变量赋值
    # 如果希望在函数内部修改全局变量，则需要使用global关键字，来声明变量
    global a  # 声明在函数内部的使用a是全局变量，此时再去修改a时，就是在修改全局的a
    a = 10  # 修改全局变量
    print('函数内部：', 'a =', a)

fn3()
print('函数外部：','a =',a)


# 命名空间（namespace）
# 命名空间指的是变量存储的位置，每一个变量都需要存储到指定的命名空间当中
# 每一个作用域都会有一个它对应的命名空间
# 全局命名空间，用来保存全局变量。函数命名空间用来保存函数中的变量
# 命名空间实际上就是一个字典，是一个专门用来存储变量的字典

# locals()用来获取当前作用域的命名空间
# 如果在全局作用域中调用locals()则获取全局命名空间，如果在函数作用域中调用locals()则获取函数命名空间
# 返回的是一个字典
scope = locals()  # 当前命名空间
print(type(scope))
print(a)
print(scope['a'])
# 向scope中添加一个key-value
scope['c'] = 1000  # 向字典中添加key-value就相当于在全局中创建了一个变量（一般不建议这么做）


print(c)

def fn4():
    a = 10
    scope = locals() # 在函数内部调用locals()会获取到函数的命名空间
    scope['b'] = 20 # 可以通过scope来操作函数的命名空间，但是也是不建议这么做

    # globals() 函数可以用来在任意位置获取全局命名空间
    global_scope = globals()
    print(global_scope['a'])
    global_scope['a'] = 30
    print(scope)


fn4()
# 8.9halfhalfhalf
# 尝试求10的阶乘（10!）
# 1! = 1
# 2! = 1*2 = 2
# 3! = 1*2*3 = 6
# 4! = 1*2*3*4 = 24

# print(1*2*3*4*5*6*7*8*9*10)

# 创建一个变量保存结果
# n = 10
# for i in range(1,10):
#     n *= i

# print(n)

# 创建一个函数，可以用来求任意数的阶乘
def factorial(n):
    '''
        该函数用来求任意数的阶乘

        参数：
            n 要求阶乘的数字
    '''

    # 创建一个变量，来保存结果
    result = n

    for i in range(1, n):
        result *= i

    return result


# 求10的阶乘
# print(factorial(20))

# 递归式的函数
# 从前有座山，山里有座庙，庙里有个老和尚讲故事，讲的什么故事呢？
#   从前有座山，山里有座庙，庙里有个老和尚讲故事，讲的什么故事呢？....
# 递归简单理解就是自己去引用自己！
# 递归式函数，在函数中自己调用自己！

# 无穷递归，如果这个函数被调用，程序的内存会溢出，效果类似于死循环
# def fn():
#     fn()
# fn()

# 递归是解决问题的一种方式，它和循环很像
#   它的整体思想是，将一个大问题分解为一个个的小问题，直到问题无法分解时，再去解决问题
# 递归式函数的两个要件
#   1.基线条件
#       - 问题可以被分解为的最小问题，当满足基线条件时，递归就不在执行了
#   2.递归条件
#       - 将问题继续分解的条件
# 递归和循环类似，基本是可以互相代替的，
#   循环编写起来比较容易，阅读起来稍难
#   递归编写起来难，但是方便阅读
# 10! = 10 * 9!
# 9! = 9 * 8!
# 8! = 8 * 7!
# ...
# 1! = 1

def factorial(n):
    '''
        该函数用来求任意数的阶乘

        参数：
            n 要求阶乘的数字
    '''
    # 基线条件 判断n是否为1，如果为1则此时不能再继续递归
    if n == 1:
        # 1的阶乘就是1，直接返回1
        return 1

    # 递归条件
    return n * factorial(n - 1)


# print(factorial(10))

# 练习
#   创建一个函数 power 来为任意数字做幂运算 n ** i
#   10 ** 5 = 10 * 10 ** 4
#   10 ** 4 = 10 * 10 ** 3
#   ...
#   10 ** 1 = 10
def power(n, i):
    '''
        power()用来为任意的数字做幂运算

        参数：
            n 要做幂运算的数字
            i 做幂运算的次数
    '''
    # 基线条件
    if i == 1:
        # 求1次幂
        return n
    # 递归条件
    return n * power(n, i - 1)


# print(power(8,6))


#
# 练习
#   创建一个函数，用来检查一个任意的字符串是否是回文字符串，如果是返回True，否则返回False
#   回文字符串，字符串从前往后念和从后往前念是一样的
#       abcba
#   abcdefgfedcba
#   先检查第一个字符和最后一个字符是否一致，如果不一致则不是回文字符串
#       如果一致，则看剩余的部分是否是回文字符串
#   检查 abcdefgfedcba 是不是回文
#   检查 bcdefgfedcb 是不是回文
#   检查 cdefgfedc 是不是回文
#   检查 defgfed 是不是回文
#   检查 efgfe 是不是回文
#   检查 fgf 是不是回文
#   检查 g 是不是回文

def hui_wen(s):
    '''
        该函数用来检查指定的字符串是否回文字符串，如果是返回True，否则返回False

        参数：
            s：就是要检查的字符串
    '''
    # 基线条件
    if len(s) < 2:
        # 字符串的长度小于2，则字符串一定是回文
        return True
    elif s[0] != s[-1]:
        # 第一个字符和最后一个字符不相等，不是回文字符串
        return False
    # 递归条件
    return hui_wen(s[1:-1])


# def hui_wen(s):
#     '''
#         该函数用来检查指定的字符串是否回文字符串，如果是返回True，否则返回False

#         参数：
#             s：就是要检查的字符串
#     '''
#     # 基线条件
#     if len(s) < 2 :
#         # 字符串的长度小于2，则字符串一定是回文
#         return True
#     # 递归条件
#     return s[0] == s[-1] and hui_wen(s[1:-1])

print(hui_wen('abcdefgfedcba'))
# 8.9halfhalfhalfhalf
# 高阶函数
# 接收函数作为参数，或者将函数作为返回值的函数是高阶函数
# 当我们使用一个函数作为参数时，实际上是将指定的代码传递进了目标函数

# 创建一个列表
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 定义一个函数
#   可以将指定列表中的所有的偶数，保存到一个新的列表中返回

# 定义一个函数，用来检查一个任意的数字是否是偶数
def fn2(i):
    if i % 2 == 0:
        return True

    return False

# 这个函数用来检查指定的数字是否大于5
def fn3(i):
    if i > 5:
        return True
    return False

def fn(func, lst):
    '''
        fn()函数可以将指定列表中的所有偶数获取出来，并保存到一个新列表中返回

        参数：
            lst：要进行筛选的列表
    '''
    # 创建一个新列表
    new_list = []

    # 对列表进行筛选
    for n in lst:
        # 判断n的奇偶
        if func(n):
            new_list.append(n)
        # if n > 5 :
        #     new_list.append(n)

    # 返回新列表
    return new_list

def fn4(i):
    if i % 3 == 0:
        return True
    return False

def fn4(i):
    return i % 3 == 0

print(fn(fn4 , l))

# filter()
# filter()可以从序列中过滤出符合条件的元素，保存到一个新的序列中
# 参数：
#  1.函数，根据该函数来过滤序列（可迭代的结构）
#  2.需要过滤的序列（可迭代的结构）
# 返回值：
#   过滤后的新序列（可迭代的结构）
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)
# fn4是作为参数传递进filter()函数中
#   而fn4实际上只有一个作用，就是作为filter()的参数
#   filter()调用完毕以后，fn4就已经没用
# 匿名函数 lambda 函数表达式 （语法糖）
#   lambda函数表达式专门用来创建一些简单的函数，他是函数创建的又一种方式
#   语法：lambda 参数列表 : 返回值
#   匿名函数一般都是作为参数使用，其他地方一般不会使用
adults = filter(lambda a: a >= 18, ages)

def fn5(a, b):
    return a + b


# (lambda a,b : a + b)(10,20)
# 也可以将匿名函数赋值给一个变量，一般不会这么做
fn6 = lambda a, b: a + b
# print(fn6(10,30))


r = filter(lambda i: i > 5, l)
# print(list(r))

# expand filter to filtering generator functions examples
def vowel(c):
    return c.lower() in 'aeiou'
print(list(filter(vowel, 'Aardvark')))  # ['A', 'a', 'a']
import itertools
# list of chrs that are not filtered by function.
print(list(itertools.filterfalse(vowel, 'Aardvark')))  # ['r', 'd', 'v', 'r', 'k']
# The dropwhile() function of Python returns an iterator only after the func. in argument returns false for the first
# time.
print(list(itertools.dropwhile(vowel, 'Aardvark')))  # ['r', 'd', 'v', 'a', 'r', 'k']
# If the elements on the specified predicate, evaluates to true, it is returned. Otherwise, the loop is terminated.
print(list(itertools.takewhile(vowel, 'Aardvark')))  # ['A', 'a']
# pick chrs based on the second parameter ()
print(list(itertools.compress('Aardvark', (1,0,1,1,0,1))))  # ['A', 'r', 'd', 'a']
# before four
print(list(itertools.islice('Aardvark', 4)))  # ['A', 'a', 'r', 'd']
# from four to seven
print(list(itertools.islice('Aardvark', 4, 7)))  # ['v', 'a', 'r']
# 1 to 7, 2 steps
print(list(itertools.islice('Aardvark', 1, 7, 2)))  # ['a', 'd', 'a']

# mapping generator function
# 1. accumulate
sample = [5,4,2,8,7,6,3,0,9,1]
# running sum
print(list(itertools.accumulate(sample)))  # [5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
# running minimum
print(list(itertools.accumulate(sample, min)))  # [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
# running maximum
print(list(itertools.accumulate(sample, max))) # [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
import operator
print(list(itertools.accumulate(sample, operator.mul)))
print(list(itertools.accumulate(range(1,11), operator.mul())))

#2. enumerate
# number the letters in the word, starting from 1.
print(list(enumerate('albatroz', 1)))  #[(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]

#3. map()
# map()函数可以对可跌dai对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回
    # squares of integers from 0 to 10
list(map(operator.mul, range(11), range(11)))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    # multiplying numbers from two iterables in parallel: results stop when the shortest iterable ends.
list(map(operator.mul, range(11), [2,4,8]))  # [0, 4, 16]
    # original zip function
list(map(lambda a,b: (a,b), range(11), [2,4,8]))  # [(0, 2), (1, 4), (2, 8)]
    # map for single iterator
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = map(lambda i: i ** 2, l)
# starmap
    # repeat each letter in the word according to its place in it, starting from 1.
list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))  # ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']
    # running average
sample = [5,4,2,8,7,6,3,0,1,9]
print(list(itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))))  # [5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333, 5.0, 4.375, 4.0, 4.5]

# generator fnctions that merge multiple input iterable
list(itertools.chain('ABC',range(2)))  # ['A', 'B', 'C', 0, 1]
list(itertools.chain(enumerate('ABC')))  # [(0, 'A'), (1, 'B'), (2, 'C')]
list(itertools.chain.from_iterable(enumerate('ABC')))  # [0, 'A', 1, 'B', 2, 'C']
list(zip('ABC', range(5)))  # ('A', 0), ('B', 1), ('C', 2)]
list(zip('ABC', range(5), [10,20,30,40]))  # [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
list(itertools.zip_longest('ABC', range(5), [10,20,30,40], fillvalue='?'))  # [('A', 0, 10), ('B', 1, 20), ('C', 2, 30), ('?', 3, 40), ('?', 4, '?')]
list(itertools.product('ABC', range(2)))  # [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
list(itertools.product('ABC'))  # [('A',), ('B',), ('C',)]
list(itertools.product('ABC', repeat=2))  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
list(itertools.product(range(2), repeat=3))  # [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
list(itertools.product('AB', range(2), repeat=2))  # [('A', 0, 'A', 0), ('A', 0, 'A', 1), ('A', 0, 'B', 0),
# ('A', 0, 'B', 1), ('A', 1, 'A', 0), ('A', 1, 'A', 1), ('A', 1, 'B', 0), ('A', 1, 'B', 1), ('B', 0, 'A', 0),
# ('B', 0, 'A', 1), ('B', 0, 'B', 0), ('B', 0, 'B', 1), ('B', 1, 'A', 0), ('B', 1, 'A', 1), ('B', 1, 'B', 0), ('B', 1, 'B', 1)]

# generator functions that expand each input item into multiple output items
    # count(start=0, step=1): yeild numbers starting at start, incremented by step.
ct = itertools.count()
next(ct)  # 0, 1, 2, 3
list(itertools.islice(itertools.count(1, .3), 3))  # [1, 1.3, 1.6]
    # cycle(it): yield items from it storing a copy of each, then yields the entire sequence repeatedly, indefinitely.
cy = itertools.cycle('ABC')
list(itertools.islice(cy, 7))
    # repeat(item, [times]) yield the given item repeadedly, indefinetly unless a number of times is given.
rp = itertools.repeat(7)
list(itertools.repeat(8,4))  # [8, 8, 8, 8]
list(map(operator.mul, range(11), itertools.repeat(5)))  # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    # combination
list(itertools.combinations("ABC", 2))  # no order no replacement: [('A', 'B'), ('A', 'C'), ('B', 'C')]
list(itertools.combinations_with_replacement("ABC", 2))  # no order with replacement: [('A', 'A'), ('A', 'B'), ('A',
# 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
list(itertools.permutations("ABC", 2))  # order no replacement: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'),
# ('C', 'A'), ('C', 'B')]
list(itertools.product("ABC", repeat=2))  # order with replacement: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'),
# ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# rearranging generator functions
list(itertools.groupby('LLLLAAGGG'))  # [('L', <itertools._grouper object at 0x0000017FD08E6160>), ('A',
    # <itertools._grouper object at 0x0000017FD08E6430>), ('G', <itertools._grouper object at 0x0000017FD08E6C40>)]
for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))  # L -> ['L', 'L', 'L', 'L']
                                    # A -> ['A', 'A', 'A']
                                    # G -> ['G', 'G']
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))  # 3 -> ['rat', 'bat']
                                    # 4 -> ['duck', 'bear', 'lion']
                                    # 5 -> ['eagle', 'shark']
                                    # 7 -> ['giraffe', 'dolphin']
for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))  # 7 -> ['dolphin', 'giraffe']
                                    # 5 -> ['shark', 'eagle']
                                    # 4 -> ['lion', 'bear', 'duck']
                                    # 3 -> ['bat', 'rat']

# iterate reducing functions
all([1,2,3])  # True
all([1,0,3])  # False
all([])  # True
any([1,2,3])  # True
any([1,0,3])  # True
any([])  # False
g = (n for n in [0, 0.0, 7, 8])
any(g)  # True
next(g)  # 8
# sort()
# 该方法用来对列表中的元素进行排序
# sort()方法默认是直接比较列表中的元素的大小
# 在sort()可以接收一个关键字参数 ， key
#   key需要一个函数作为参数，当设置了函数作为参数
#   每次都会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小
l = ['bb', 'aaaa', 'c', 'ddddddddd', 'fff']
l.sort(key=len)

l = [2, 5, '1', 3, '6', '4']
l.sort(key=int)
print(l)

# sorted()
# 这个函数和sort()的用法基本一致，但是sorted()可以对任意的序列进行排序
#   并且使用sorted()排序不会影响原来的对象，而是返回一个新对象

l = [2, 5, '1', 3, '6', '4']
l = "123765816742634781"

print('排序前:', l)
print(sorted(l, key=int))
print('排序后:', l)

# apply()
"""similar to map(), but works for pandas"""
import pandas as pd
import numpy as np
df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
df.apply(np.sqrt)
df.apply(np.sum, axis=0)
df.apply(np.sum, axis=1)

# reduce()
"""It applies a function of two arguments repeatedly on the elements of a sequence so as to reduce the sequence to a 
single value. For example, reduce(lambda x, y: x^y, [1, 2, 3, 4]) calculates (((1^2)^3)^4). If the initial is present, 
it is placed first in the calculation, and if the default result when the sequence is empty."""

from functools import reduce
list1 = [2, 4, 7, 9, 1, 3]
sum_of_list1 = reduce(lambda a, b: a + b, list1)
list2 = ["abc", "xyz", "def"]
max_of_list2 = reduce(lambda a, b: a if a > b else b, list2)
print('Sum of list1 :', sum_of_list1)  # Sum of list1 : 26
print('Maximum of list2 :', max_of_list2)  # Maximum of list2 : xyz

# 8.9halfhalfhalfhalfhalf 闭包
# 将函数作为返回值返回，也是一种高阶函数
# 这种高阶函数我们也称为叫做闭包，通过闭包可以创建一些只有当前函数能访问的变量
#   可以将一些私有的数据藏到的闭包中

def fn():

    a = 10

    # 函数内部再定义一个函数
    def inner():
        print('我是fn2' , a)

    # 将内部函数 inner作为返回值返回
    return inner

# r是一个函数，是调用fn()后返回的函数
# 这个函数实在fn()内部定义，并不是全局函数
# 所以这个函数总是能访问到fn()函数内的变量
r = fn()

# r()

# 求多个数的平均值
# nums = [50,30,20,10,77]

# sum()用来求一个列表中所有元素的和
# print(sum(nums)/len(nums))

# 形成闭包的要件
#   ① 函数嵌套
#   ② 将内部函数作为返回值返回
#   ③ 内部函数必须要使用到外部函数的变量
def make_averager():
    # 创建一个列表，用来保存数值
    nums = []

    # 创建一个函数，用来计算平均值
    def averager(n) :
        # 将n添加到列表中
        nums.append(n)
        # 求平均值
        return sum(nums)/len(nums)

    return averager

averager = make_averager()

print(averager(10))
print(averager(20))
print(averager(30))
print(averager(40))

#8.9 装饰器
# 创建几个函数

def add(a , b):
    '''
        求任意两个数的和
    '''
    r = a + b
    return r


def mul(a , b):
    '''
        求任意两个数的积
    '''
    r = a * b
    return r

# 希望函数可以在计算前，打印开始计算，计算结束后打印计算完毕
#  我们可以直接通过修改函数中的代码来完成这个需求，但是会产生以下一些问题
#   ① 如果要修改的函数过多，修改起来会比较麻烦
#   ② 并且不方便后期的维护
#   ③ 并且这样做会违反开闭原则（OCP）
#           程序的设计，要求开发对程序的扩展，要关闭对程序的修改


# r = add(123,456)
# print(r)

# 我们希望在不修改原函数的情况下，来对函数进行扩展
def fn():
    print('我是fn函数....')

# 只需要根据现有的函数，来创建一个新的函数
def fn2():
    print('函数开始执行~~~')
    fn()
    print('函数执行结束~~~')

# fn2()

def new_add(a,b):
    print('计算开始~~~')
    r = add(a,b)
    print('计算结束~~~')
    return r

# r = new_add(111,222)
# print(r)

# 上边的方式，已经可以在不修改源代码的情况下对函数进行扩展了
#   但是，这种方式要求我们每扩展一个函数就要手动创建一个新的函数，实在是太麻烦了
#   为了解决这个问题，我们创建一个函数，让这个函数可以自动的帮助我们生产函数

def begin_end(old):
    '''
        用来对其他函数进行扩展，使其他函数可以在执行前打印开始执行，执行后打印执行结束

        参数：
            old 要扩展的函数对象
    '''
    # 创建一个新函数
    def new_function(*args , **kwargs):
        print('开始执行~~~~')
        # 调用被扩展的函数
        result = old(*args , **kwargs)
        print('执行结束~~~~')
        # 返回函数的执行结果
        return result

    # 返回新函数
    return new_function

f = begin_end(fn)
f2 = begin_end(add)
f3 = begin_end(mul)

# r = f()
# r = f2(123,456)
# r = f3(123,456)
# print(r)
# 向begin_end()这种函数我们就称它为装饰器
#   通过装饰器，可以在不修改原来函数的情况下来对函数进行扩展
#   在开发中，我们都是通过装饰器来扩展函数的功能的
# 在定义函数时，可以通过@装饰器，来使用指定的装饰器，来装饰当前的函数
#   可以同时为一个函数指定多个装饰器，这样函数将会安装从内向外的顺序被装饰

def fn3(old):
    '''
        用来对其他函数进行扩展，使其他函数可以在执行前打印开始执行，执行后打印执行结束

        参数：
            old 要扩展的函数对象
    '''
    # 创建一个新函数
    def new_function(*args , **kwargs):
        print('fn3装饰~开始执行~~~~')
        # 调用被扩展的函数
        result = old(*args , **kwargs)
        print('fn3装饰~执行结束~~~~')
        # 返回函数的执行结果
        return result

    # 返回新函数
    return new_function

@fn3
@begin_end
def say_hello():
    print('大家好~~~')

say_hello()

# 8.10 storing your function in modules
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers',
                 'extra cheese')
# 8.11 importing specific function
from pizza import make_pizza
from pizza import make_pizza, make_pizza1, make_pizza2

# 8.12 using as to give a function an Alias
# or use as to give a module an Alias
# or import all functions in a module
from pizza import make_pizza as mp

mp(12, 'mushrooms', 'green peppers', 'extra cheese')

import pizza as p

p.make_pizza(12, 'mushroom')

from pizza import *

make_pizza(12, 'mushroom')

# 8.13 styling function
# no space in function's argument when use =
# when you define or call functions

# 8.14 lambda small function
x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))

# annotation function declaration
# Python program to print Fibonacci series
def fib(n:'int', output:'list'=[])-> 'list':
    if n == 0:
        return output
    else:
        if len(output)< 2:
            output.append(1)
            fib(n-1, output)
        else:
            last = output[-1]
            second_last = output[-2]
            output.append(last + second_last)
            fib(n-1, output)
        return output
print(fib.__annotations__)

def clip(text:str, max_len:'int>0'=80) -> str:
    """return text clipped at the last space before or after max_len"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()
print(clip.__annotations__)


## 9.0 class
"""第六章 对象（Object）
什么是对象？
- 对象是内存中专门用来存储数据的一块区域。
- 对象中可以存放各种数据（比如：数字、布尔值、代码）
- 对象由三部分组成：
    1.对象的标识（id）
    2.对象的类型（type）
    3.对象的值（value）
面向对象（oop）
- Python是一门面向对象的编程语言
- 所谓的面向对象的语言，简单理解就是语言中的所有操作都是通过对象来进行的
- 面向过程的编程的语言
    - 面向过程指将我们的程序的逻辑分解为一个一个的步骤，
        通过对每个步骤的抽象，来完成程序
    - 例子：
        - 孩子上学
            1.妈妈起床
            2.妈妈上厕所
            3.妈妈洗漱
            4.妈妈做早饭
            5.妈妈叫孩子起床
            6.孩子上厕所
            7.孩子要洗漱
            8.孩子吃饭
            9.孩子背着书包上学校

    - 面向过程的编程思想将一个功能分解为一个一个小的步骤，
        我们通过完成一个一个的小的步骤来完成一个程序
    - 这种编程方式，符合我们人类的思维，编写起来相对比较简单
    - 但是这种方式编写代码的往往只适用于一个功能，
        如果要在实现别的功能，即使功能相差极小，也往往要重新编写代码，
        所以它可复用性比较低，并且难于维护 

- 面向对象的编程语言
    - 面向对象的编程语言，关注的是对象，而不关注过程 
    - 对于面向对象的语言来说，一切都是对象       
    - 例子：
        1.孩他妈起床叫孩子上学

    - 面向对象的编程思想，将所有的功能统一保存到对应的对象中
        比如，妈妈功能保存到妈妈的对象中，孩子的功能保存到孩子对象中
        要使用某个功能，直接找到对应的对象即可
    - 这种方式编写的代码，比较容易阅读，并且比较易于维护，容易复用。
    - 但是这种方式编写，不太符合常规的思维，编写起来稍微麻烦一点 

- 简单归纳一下，面向对象的思想
    1.找对象
    2.搞对象
类(class)
- 我们目前所学习的对象都是Python内置的对象
- 但是内置对象并不能满足所有的需求，所以我们在开发中经常需要自定义一些对象
- 类，简单理解它就相当于一个图纸。在程序中我们需要根据类来创建对象
- 类就是对象的图纸！
- 我们也称对象是类的实例（instance）
- 如果多个对象是通过一个类创建的，我们称这些对象是一类对象
- 像 int() float() bool() str() list() dict() .... 这些都是类
- a = int(10) # 创建一个int类的实例 等价于 a = 10
- 我们自定义的类都需要使用大写字母开头，使用大驼峰命名法（帕斯卡命名法）来对类命名

- 类也是一个对象！
- 类就是一个用来创建对象的对象！
- 类是type类型的对象，定义类实际上就是定义了一个type类型的对象
使用类创建对象的流程（参考图1）
1.创建一个变量
2.在内存中创建一个新对象
3.将对象的id赋值给变量
类的定义（参考图2）
- 类和对象都是对现实生活中的事物或程序中的内容的抽象
- 实际上所有的事物都由两部分构成：
    1.数据（属性）
    2.行为（方法）

- 在类的代码块中，我们可以定义变量和函数，
    变量会成为该类实例的公共属性，所有的该类实例都可以通过 对象.属性名 的形式访问 
    函数会成为该类实例的公共方法，所有该类实例都可以通过 对象.方法名() 的形式调用方法

- 注意：
    方法调用时，第一个参数由解析器自动传递，所以定义方法时，至少要定义一个形参！ 

- 实例为什么能访问到类中的属性和方法
    类中定义的属性和方法都是公共的，任何该类实例都可以访问

    - 属性和方法查找的流程
        当我们调用一个对象的属性时，解析器会先在当前对象中寻找是否含有该属性，
            如果有，则直接返回当前的对象的属性值，
            如果没有，则去当前对象的类对象中去寻找，如果有则返回类对象的属性值，
            如果类对象中依然没有，则报错！

    - 类对象和实例对象中都可以保存属性（方法）
        - 如果这个属性（方法）是所有的实例共享的，则应该将其保存到类对象中
        - 如果这个属性（方法）是某个实例独有，则应该保存到实例对象中     

    - 一般情况下，属性保存到实例对象中
        而方法需要保存到类对象中    
创建对象的流程
p1 = Person()的运行流程
    1.创建一个变量
    2.在内存中创建一个新对象
    3.__init__(self)方法执行
    4.将对象的id赋值给变量
类的基本结构
class 类名([父类]) :

    公共的属性... 

    # 对象的初始化方法
    def __init__(self,...):
        ...

    # 其他的方法    
    def method_1(self,...):
        ...

    def method_2(self,...):
        ...

    ..."""
# todo class introduction
a = int(10) # 创建一个int类的实例
b = str('hello') # 创建一个str类的实例

# print(a , type(a))
# print(b , type(b))

# 定义一个简单的类
# 使用class关键字来定义类，语法和函数很像！
# class 类名([父类]):
#   代码块
# <class '__main__.MyClass'>
class MyClass():
    pass

# print(MyClass)
# 使用MyClass创建一个对象
# 使用类来创建对象，就像调用一个函数一样
mc = MyClass() # mc就是通过MyClass创建的对象，mc是MyClass的实例
mc_2 = MyClass()
mc_3 = MyClass()
mc_4 = MyClass()
# mc mc_2 mc_3 mc_4 都是MyClass的实例，他们都是一类对象
# isinstance()用来检查一个对象是否是一个类的实例
result = isinstance(mc_2,MyClass)
result = isinstance(mc_2,str)

# print(mc , type(mc))
# print('result =',result)

# print(id(MyClass) , type(MyClass))

# 现在我们通过MyClass这个类创建的对象都是一个空对象
# 也就是对象中实际上什么都没有，就相当于是一个空的盒子
# 可以向对象中添加变量，对象中的变量称为属性
# 语法：对象.属性名 = 属性值
mc.name = '孙悟空'
mc_2.name = '猪八戒'

print(mc_2.name)
# todo define a class
# 尝试定义一个表示人的类
class Person:
    # 在类的代码块中，我们可以定义变量和函数
    # 在类中我们所定义的变量，将会成为所有的实例的公共属性
    # 所有实例都可以访问这些变量
    name = 'swk'  # 公共属性，所有实例都可以访问

    # 在类中也可以定义函数，类中的定义的函数，我们称为方法
    # 这些方法可以通过该类的所有实例来访问

    def say_hello(self):
        # 方法每次被调用时，解析器都会自动传递第一个实参
        # 第一个参数，就是调用方法的对象本身，
        #   如果是p1调的，则第一个参数就是p1对象
        #   如果是p2调的，则第一个参数就是p2对象
        # 一般我们都会将这个参数命名为self

        # say_hello()这个方法，可以显示如下格式的数据：
        #   你好！我是 xxx
        #   在方法中不能直接访问类中的属性
        print('你好！我是 %s' % self.name)


# 创建Person的实例
p1 = Person()
p2 = Person()

# print(p2.name)

# 调用方法，对象.方法名()
# 方法调用和函数调用的区别
# 如果是函数调用，则调用时传几个参数，就会有几个实参
# 但是如果是方法调用，默认传递一个参数，所以方法中至少要定义一个形参


# 修改p1的name属性
p1.name = '猪八戒'
p2.name = '沙和尚'

p1.say_hello()  # '你好！我是 猪八戒'
p2.say_hello()  # '你好！我是 沙和尚'


# del p2.name # 删除p2的name属性

# print(p1.name)
# print(p2.name)
# todo _init_
class Person :
    # 在类中可以定义一些特殊方法（魔术方法）
    # 特殊方法都是以__开头，__结尾的方法
    # 特殊方法不需要我们自己调用，不要尝试去调用特殊方法
    # 特殊方法将会在特殊的时刻自动调用
    # 学习特殊方法：
    #   1.特殊方法什么时候调用
    #   2.特殊方法有什么作用
    # 创建对象的流程
    # p1 = Person()的运行流程
    #   1.创建一个变量
    #   2.在内存中创建一个新对象
    #   3.__init__(self)方法执行
    #   4.将对象的id赋值给变量

    # init会在对象创建以后离开执行
    # init可以用来向新创建的对象中初始化属性
    # 调用类创建对象时，类后边的所有参数都会依次传递到init()中
    def __init__(self,name):
        # print(self)
        # 通过self向新建的对象中初始化属性
        self.name = name

    def say_hello(self):
        print('大家好，我是%s'%self.name)


# 目前来讲，对于Person类来说name是必须的，并且每一个对象中的name属性基本上都是不同
# 而我们现在是将name属性在定义为对象以后，手动添加到对象中，这种方式很容易出现错误
# 我们希望，在创建对象时，必须设置name属性，如果不设置对象将无法创建
#   并且属性的创建应该是自动完成的，而不是在创建对象以后手动完成
# p1 = Person()
# # 手动向对象添加name属性
# p1.name = '孙悟空'

# p2 = Person()
# p2.name = '猪八戒'

# p3 = Person()
# p3.name = '沙和尚'

# p3.say_hello()

p1 = Person('孙悟空')
p2 = Person('猪八戒')
p3 = Person('沙和尚')
p4 = Person('唐僧')
# p1.__init__() 不要这么做

# print(p1.name)
# print(p2.name)
# print(p3.name)
# print(p4.name)

p4.say_hello()
# 9.1 creating a class
# 9.1.1 creating the dog class
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " roll over!")


my_dog = Dog('willie', 6)

# 9.1.2 accessing attributesl
my_dog.name
# 9.1.3 calling method
my_dog.sit()
my_dog.roll_over()
# 9.1.4 create multiple instances
your_dog = Dog('lucy', 3)

print('my dog name is ' + my_dog.name.title() + '.')
print('my dog is ' + str(my_dog.age) + ' years old.')
my_dog.sit()
print('\nYour dog name is ' + your_dog.name.title() + '.')
print('your dog is ' + str(your_dog.age) + ' years old.')
your_dog.sit()


# excercise
# 1.
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(self.name + self.cuisine)

    def open_restaurant(self):
        print(self.name + ' is open.')


restaurant = Restaurant('Plaza', 'silk')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 2.
restaurant1 = Restaurant('A', 'X')
restaurant2 = Restaurant('B', 'Y')
restaurant3 = Restaurant('C', 'Z')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# 3.
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name + ' ' + self.last_name)

    def greet_user(self):
        print('hi, ' + self.first_name + ' ' + self.last_name)


user1 = User('A', 'B')
user2 = User('C', 'D')
user3 = User('E', 'F')
users = [user1, user2, user3]
for i in users:
    i.describe_user()
    i.greet_user()


# 9.2 working with classes and instances
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year + ' ' +
                        self.make + ' ' +
                        self.model)
        return long_name.title()


my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())


# 9.2.1 Setting a Default value for an Attribute
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year + ' ' +
                        self.make + ' ' +
                        self.model)
        return long_name.title()

    def read_odometer(self):
        print('This car has ' +
              str(self.odometer_reading) +
              ' miles on it.')


my_new_car = Car('audi', 'a4', '2016')
my_new_car.read_odometer()
# 9.2.2 Modifying Attribute Values
# 9.2.2.1 modifying an attribute's value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# 9.2.2.2 modifying an attribute's value through a method
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year + ' ' +
                        self.make + ' ' +
                        self.model)
        return long_name.title()

    def read_odometer(self):
        print('This car has ' +
              str(self.odometer_reading) +
              ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cannot roll back an odometer.')


my_new_car = Car('audi', 'a4', '2016')
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(22)


# 9.2.2.3 incrementing an Attribute's value through a method
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' +
              str(self.odometer_reading) +
              ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cannot roll back an odometer.')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', '2013')
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# practice
# 1.
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name + self.cuisine)

    def open_restaurant(self):
        print(self.name + ' is open.')

    def read_number_served(self):
        print(str(self.number_served))

    def set_number_serverd(self, number_served):
        self.number_served = number_served

    def add_number_served(self, add):
        self.number_served += add


restaurant = Restaurant('Plaza', 'silk')
restaurant.set_number_serverd(23)
restaurant.add_number_served(5)
restaurant.read_number_served()
# Todo 三大特性
# todo 封装是面向对象的三大特性之一
# 封装指的是隐藏对象中一些不希望被外部所访问到的属性或方法
# 如何隐藏一个对象中的属性？
#   - 将对象的属性名，修改为一个外部不知道的名字
# 如何获取（修改）对象中的属性？
#   - 需要提供一个getter和setter方法使外部可以访问到属性
#   - getter 获取对象中的指定属性（get_属性名）
#   - setter 用来设置对象的指定属性（set_属性名）
# 使用封装，确实增加了类的定义的复杂程度，但是它也确保了数据的安全性
#   1.隐藏了属性名，使调用者无法随意的修改对象中的属性
#   2.增加了getter和setter方法，很好的控制的属性是否是只读的
#       如果希望属性是只读的，则可以直接去掉setter方法
#       如果希望属性不能被外部访问，则可以直接去掉getter方法
#   3.使用setter方法设置属性，可以增加数据的验证，确保数据的值是正确的
#   4.使用getter方法获取属性，使用setter方法设置属性
#       可以在读取属性和修改属性的同时做一些其他的处理
#   5.使用getter方法可以表示一些计算的属性

class Dog:
    '''
        表示狗的类
    '''
    def __init__(self , name , age):
        self.hidden_name = name
        self.hidden_age = age

    def say_hello(self):
        print('大家好，我是 %s'%self.hidden_name)

    def get_name(self):
        '''
            get_name()用来获取对象的name属性
        '''
        # print('用户读取了属性')
        return self.hidden_name

    def set_name(self , name):
        # print('用户修改了属性')
        self.hidden_name = name

    def get_age(self):
        return self.hidden_age

    def set_age(self , age):
        if age > 0 :
            self.hidden_age = age


d = Dog('旺财',8)

# d.say_hello()

# 调用setter来修改name属性
d.set_name('小黑')
d.set_age(-10)

# d.say_hello()
print(d.get_age())


class Rectangle:
    '''
        表示矩形的类
    '''

    def __init__(self, width, height):
        self.hidden_width = width
        self.hidden_height = height

    def get_width(self):
        return self.hidden_width

    def get_height(self):
        return self.hidden_height

    def set_width(self, width):
        self.hidden_width = width

    def set_height(self, height):
        self.hidden_height = height

    def get_area(self):
        return self.hidden_width * self.hidden_height

    # r = Rectangle(5,2)


# r.set_width(10)
# r.set_height(20)

# print(r.get_area())


# 可以为对象的属性使用双下划线开头，__xxx
# 双下划线开头的属性，是对象的隐藏属性，隐藏属性只能在类的内部访问，无法通过对象访问
# 其实隐藏属性只不过是Python自动为属性改了一个名字
#   实际上是将名字修改为了，_类名__属性名 比如 __name -> _Person__name
# class Person:
#     def __init__(self,name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set_name(self , name):
#         self.__name = name

# p = Person('孙悟空')

# print(p.__name) __开头的属性是隐藏属性，无法通过对象访问
# p.__name = '猪八戒'
# print(p._Person__name)
# p._Person__name = '猪八戒'

# print(p.get_name())

# 使用__开头的属性，实际上依然可以在外部访问，所以这种方式我们一般不用
#   一般我们会将一些私有属性（不希望被外部访问的属性）以_开头
#   一般情况下，使用_开头的属性都是私有属性，没有特殊需要不要修改私有属性
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


p = Person('孙悟空')

print(p._name)


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # property装饰器，用来将一个get方法，转换为对象的属性
    # 添加为property装饰器以后，我们就可以像调用属性一样使用get方法
    # 使用property装饰的方法，必须和属性名是一样的
    @property
    def name(self):
        print('get方法执行了~~~')
        return self._name

    # setter方法的装饰器：@属性名.setter
    @name.setter
    def name(self, name):
        print('setter方法调用了')
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


p = Person('猪八戒', 18)

p.name = '孙悟空'
p.age = 28

print(p.name, p.age)

# 9.3 todo 继承
# 继承

# 定义一个类 Animal（动物）
#   这个类中需要两个方法：run() sleep()
class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')

    # def bark(self):
    #     print('动物嚎叫~~~')

# 定义一个类 Dog（狗）
#   这个类中需要三个方法：run() sleep() bark()
# class Dog:
#     def run(self):
#         print('狗会跑~~~')

#     def sleep(self):
#         print('狗睡觉~~~')

#     def bark(self):
#         print('汪汪汪~~~')

# 有一个类，能够实现我们需要的大部分功能，但是不能实现全部功能
# 如何能让这个类来实现全部的功能呢？
#   ① 直接修改这个类，在这个类中添加我们需要的功能
#       - 修改起来会比较麻烦，并且会违反OCP原则
#   ② 直接创建一个新的类
#       - 创建一个新的类比较麻烦，并且需要大量的进行复制粘贴，会出现大量的重复性代码
#   ③ 直接从Animal类中来继承它的属性和方法
#       - 继承是面向对象三大特性之一
#       - 通过继承我们可以使一个类获取到其他类中的属性和方法
#       - 在定义类时，可以在类名后的括号中指定当前类的父类（超类、基类、super）
#           子类（衍生类）可以直接继承父类中的所有的属性和方法
#
#  通过继承可以直接让子类获取到父类的方法或属性，避免编写重复性的代码，并且也符合OCP原则
#   所以我们经常需要通过继承来对一个类进行扩展

class Dog(Animal):
    def bark(self):
        print('汪汪汪~~~')

    def run(self):
        print('狗跑~~~~')

class Hashiqi(Dog):
    def fan_sha(self):
        print('我是一只傻傻的哈士奇')

d = Dog()
h = Hashiqi()

# d.run()
# d.sleep()
# d.bark()

# r = isinstance(d , Dog)
# r = isinstance(d , Animal)
# print(r)

# 在创建类时，如果省略了父类，则默认父类为object
#   object是所有类的父类，所有类都继承自object
class Person(object):
    pass

# issubclass() 检查一个类是否是另一个类的子类
# print(issubclass(Animal , Dog))
# print(issubclass(Animal , object))
# print(issubclass(Person , object))

# isinstance()用来检查一个对象是否是一个类的实例
#   如果这个类是这个对象的父类，也会返回True
#   所有的对象都是object的实例
print(isinstance(print , object))
# 继承

# 定义一个类 Animal（动物）
#   这个类中需要两个方法：run() sleep()
class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')


class Dog(Animal):
    def bark(self):
        print('汪汪汪~~~')

    def run(self):
        print('狗跑~~~~')


# 如果在子类中如果有和父类同名的方法，则通过子类实例去调用方法时，
#   会调用子类的方法而不是父类的方法，这个特点我们成为叫做方法的重写（覆盖，override）
# 创建Dog类的实例
# d = Dog()

# d.run()

# 当我们调用一个对象的方法时，
#   会优先去当前对象中寻找是否具有该方法，如果有则直接调用
#   如果没有，则去当前对象的父类中寻找，如果父类中有则直接调用父类中的方法，
#   如果没有，则去父类的父类中寻找，以此类推，直到找到object，如果依然没有找到，则报错
#   todo: Do not inherit from build-in data type!!!
class A(object):
    def test(self):
        print('AAA')

class B(A):
    def test(self):
        print('BBB')

class C(B):
    def test(self):
        print('CCC')

# 创建一个c的实例
c = C()
c.test()
class Animal:
    def __init__(self,name):
        self._name = name

    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

# 父类中的所有方法都会被子类继承，包括特殊方法，也可以重写特殊方法
class Dog(Animal):

    def __init__(self,name,age):
        # 希望可以直接调用父类的__init__来初始化父类中定义的属性
        # super() 可以用来获取当前类的父类，
        #   并且通过super()返回对象调用父类方法时，不需要传递self
        super().__init__(name)
        self._age = age

    def bark(self):
        print('汪汪汪~~~')

    def run(self):
        print('狗跑~~~~')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = name

d = Dog('旺财',18)

print(d.name)
print(d.age)

# multiple inheritence
class A(object):
    def test(self):
        print('AAA')

class B(object):
    def test(self):
        print('B中的test()方法~~')

    def test2(self):
        print('BBB')

# 在Python中是支持多重继承的，也就是我们可以为一个类同时指定多个父类
#   可以在类名的()后边添加多个类，来实现多重继承
#   多重继承，会使子类同时拥有多个父类，并且会获取到所有父类中的方法
# 在开发中没有特殊的情况，应该尽量避免使用多重继承，因为多重继承会让我们的代码过于复杂
# 如果多个父类中有同名的方法，则会现在第一个父类中寻找，然后找第二个，然后找第三个。。。
#   前边父类的方法会覆盖后边父类的方法
class C(A,B):
    pass

# 类名.__bases__ 这个属性可以用来获取当前类的所有父类
# print(C.__bases__) (<class '__main__.B'>,)
# print(B.__bases__) (<class 'object'>,)

# print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>)

c = C()

c.test()
# 9.3.1 the __init__() method for a child class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # the super() function is a speacial function that helps
        # python make connections between the parent and child
        # class
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


# 9.3.2 defining attributes and methods for the child class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # the super() function is a speacial function that helps
        # python make connections between the parent and child
        # class
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):  # if this function has the same name with parent class's method, when you call this
        # function name, it will call child class's method.
        print('this car has a ' + str(self.battery_size) + '-KWH battery')


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# 9.3.3 overriding method from the parent class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    # if fill_gas_tank() is in the Car (parent class),
    # and you don't want it in your child class,
    # then you can override this function like this:
    def fill_gas_tank():
        print('this car does not need a gas tank.')


# 9.3.4 instances as attributes
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('this car has a ' + str(self.battery_size) + '-KWH battery.')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

# todo 多态
# 多态是面向对象的三大特征之一
# 多态从字面上理解是多种形态
# 狗（狼狗、藏獒、哈士奇、古牧 。。。）
# 一个对象可以以不同的形态去呈现

# 定义两个类
class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class C:
    pass


a = A('孙悟空')
b = B('猪八戒')
c = C()


# 定义一个函数
# 对于say_hello()这个函数来说，只要对象中含有name属性，它就可以作为参数传递
#   这个函数并不会考虑对象的类型，只要有name属性即可
def say_hello(obj):
    print('你好 %s' % obj.name)


# 在say_hello_2中我们做了一个类型检查，也就是只有obj是A类型的对象时，才可以正常使用，
#   其他类型的对象都无法使用该函数，这个函数就违反了多态
# 违反了多态的函数，只适用于一种类型的对象，无法处理其他类型对象，这样导致函数的适应性非常的差
# 注意，向isinstance()这种函数，在开发中一般是不会使用的！
def say_hello_2(obj):
    # 做类型检查
    if isinstance(obj, A):
        print('你好 %s' % obj.name)
    # say_hello(b)


# say_hello_2(b)

# 鸭子类型
# 如果一个东西，走路像鸭子，叫声像鸭子，那么它就是鸭子

# len()
# 之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法__len__
# 换句话说，只要对象中具有__len__特殊方法，就可以通过len()来获取它的长度
l = [1, 2, 3]
s = 'hello'

# print(len(l))
# print(len(s))
print(len(b))
print(len(c))


# 面向对象的三大特征：
#   封装
#       - 确保对象中的数据安全
#   继承
#       - 保证了对象的可扩展性
#   多态
#       - 保证了程序的灵活性

# 9.4 class attribute and class method
class Person:
    # class attributes
    number_of_people = 0
    gravity = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod  # decorator
    def number_of_people_(cls):  # cls is similar to self, but this time the class itself is feed in not a instance feed in.
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


print(Person.number_of_people_())
p1 = Person('tim')
p2 = Person('Tom')
print(Person.number_of_people_())


# 9.5 stacking class
class Math:  # we need a class to stack a lot of function, but we don't want to build andy instance.

    @staticmethod  # static means not changing. This kind of method helps you to do something but not change
    # anything. Don't need an instance. It acts like a function. And we don't need cls.
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print('run')


Math.pr()

# 9.6 special methods
# 特殊方法，也称为魔术方法
# 特殊方法都是使用__开头和结尾的
# 特殊方法一般不需要我们手动调用，需要在一些特殊情况下自动执行

# 定义一个Person类
class Person(object):
    """人类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__（）这个特殊方法会在尝试将对象转换为字符串的时候调用
    # 它的作用可以用来指定对象转换为字符串的结果  （print函数）
    def __str__(self):
        return 'Person [name=%s , age=%d]' % (self.name, self.age)

        # __repr__()这个特殊方法会在对当前对象使用repr()函数时调用

    # 它的作用是指定对象在 ‘交互模式’中直接输出的效果
    def __repr__(self):
        return 'Hello'

        # object.__add__(self, other)

    # object.__sub__(self, other)
    # object.__mul__(self, other)
    # object.__matmul__(self, other)
    # object.__truediv__(self, other)
    # object.__floordiv__(self, other)
    # object.__mod__(self, other)
    # object.__divmod__(self, other)
    # object.__pow__(self, other[, modulo])
    # object.__lshift__(self, other)
    # object.__rshift__(self, other)
    # object.__and__(self, other)
    # object.__xor__(self, other)
    # object.__or__(self, other)

    # object.__lt__(self, other) 小于 <
    # object.__le__(self, other) 小于等于 <=
    # object.__eq__(self, other) 等于 ==
    # object.__ne__(self, other) 不等于 !=
    # object.__gt__(self, other) 大于 >
    # object.__ge__(self, other) 大于等于 >=

    # __len__()获取对象的长度

    # object.__bool__(self)
    # 可以通过bool来指定对象转换为布尔值的情况
    def __bool__(self):
        return self.age > 17

    # __gt__会在对象做大于比较的时候调用，该方法的返回值将会作为比较的结果
    # 他需要两个参数，一个self表示当前对象，other表示和当前对象比较的对象
    # self > other
    def __gt__(self, other):
        return self.age > other.age


# 创建两个Person类的实例
p1 = Person('孙悟空', 18)
p2 = Person('猪八戒', 28)

# 打印p1
# 当我们打印一个对象时，实际上打印的是对象的中特殊方法 __str__()的返回值
# print(p1) # <__main__.Person object at 0x04E95090>
# print(p1)
# print(p2)

# print(repr(p1))

# t = 1,2,3
# print(t) # (1, 2, 3)

# print(p1 > p2)
# print(p2 > p1)

# print(bool(p1))

# if p1 :
#     print(p1.name,'已经成年了')
# else :
#     print(p1.name,'还未成年了')

# create a well designed 2d array
from array import array
import math
class Vector2d:
    __slots__ = ('_x', '_y')  # by default, python stores instance attributes in dictionary. dic uses a lot memory.
    # slot class attribute can save a lot memory by letting the interpreter store the instance attributes in a tuple
    # instead of a dict.
    typecode = 'd'  # typecode is a class attribute we will use when converting Vector2d instances to/from bytes.
    def __init__(self,x,y):
        # create read only property
        self._x = float(x)
        self._y = float(y)
    @property  # property decorator marks the getter method of a property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @name.setter
    def name(self, name):
        self._x = name
    @name.setter
    def name(self, name):
        self._y = name
    # now that our vectors are reasonably immutable, we can implement the __hash__ method. Because hash value of an
    # instance is never supposed to change.
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
# v1 = Vector(3,4)
# v2 = Vector(3.1, 4.2)
# hash(v1), hash(v2) --- (7, 384307168202284039)
# set([v1, v2]) --- {Vector2d(3.1, 4.2), Vector2d(3.0, 4.0)}
    def __iter__(self):  # make Vector2d iterable; this is what makes unpacking work (x,y = my_vector)
        return (i for i in (self.x, self.y))
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)  # *self feed x, y because Vector2d is iterable.
    def __str__(self):
        return str(tuple(self))
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __format__(self, fmt_spec=''):
        # normal format method:
        # components = (format(c, fmt_spec) for c in self)
        # return '({}, {})'.format(*components)  # format(1/2.43, '0.4f') --- '0.4115'/ format(2/3, '.1%') --- '66.7%'/
                                            # format(datetime.now(), '%H:%M:%S') --- '18:49:05'
        # how to extend format specification methods?
        # costum format method (end with p representing angle)
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
# format(Vector2d(1,1), 'p')  # '<1.41421..., 0.785398...>'
# format(Vector2d(1,1), '.3ep')  # '<1.414e+00, 0.7854e-01>'
    def angle(self):
        return math.atan2(self.x, self.y)
    """to define a method that operates on the class and not on instances, classmethod changes the way the method is 
    called, so it receives the class it self as the first argument, instead of an instance. its most common use is for
    alternative constructors, like frombytes."""
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    """in contrast, static method has nothing to do with this class."""
    @staticmethod
    def add(a, b):
        return a + b
    # a hashable 2d vector

# Vector: Create a user defined sequence type
from array import array
import reprlib
import math
import functools
import operator

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)
    def __getattr__(self, item):
        cls = type(self)
        if len(name) == 1:  # if the name is one character, it may be one of the shortcut_names.
            pos = cls.shortcut_name.find(name)  # find position of 1-letter name
            if 0 <= pos < len(self._components):  # if position is within range, return the array element
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))
    def __setattr__(self, key, value):
        cls = type(self)
        if len(name) == 1:  # special handing for single-character attribute names.
            if name in cls.shortcut_names:  # if name is one of xyzt, set specific message.
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():  # if name is lowercase, set error message about all single-letter names.
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:  # otherwise, set blink error message
                error = ''
            if error:  # if there is a nonblank error message, raise AttributeError.
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)  # Default case: call__setattr__ on superclass for standard behavior.
    # def __getitem__(self, index):  # make slicing work, but can only get array after slicing, not our new class type Vector
    #     return self._components[index]
    def __getitem__(self, index):  # sequence use getitem, non-sequence use getattr
        cls = type(self)  # get the class of the instance for later use
        if isinstance(index, slice):  # if the index is a slice (if we need a sequence slice)
            return cls(self._components[index])  # build another Vector with slicing.
        elif isinstance(index, numbers.Integral):  # if the index is a int (if we only need slice one number)
            return self._components[index]  # return that number
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))
    def __len__(self):
        return len(self._components)
    def __iter__(self):
        return iter(self._components)
    def __repr__(self):
        components = reprlib.repr(self._components)  # to get limited length representation of self._components
        components = components[components.find('['):-1]  # remove the array 'd' (typecode) before plugging the
                                                            # string into Vector constructor call
        return 'Vector({})'.format(components)
    def __str__(self):
        return str(tuple(self))
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):  # a is each value in object, b is each value in other. use for loop to unzip
                                        # and compare
            if a != b:
                return False
        return True
        # return len(self) == len(other) and all(a == b for a, b in zip(self, other)) # use one line in short.
    def __hash__(self):  # eq always works with hash
        hashes = (hash(x) for x in self._components)  # create generator expression to lazily compute the hash of each..
        return functools.reduce(operator.xor, hashes, 0)  # xor: lambda a,b: a^b; 0 is the initializer.
        """when using reduce, it's good practice to provide the third argument, reduce(function, iterable, initializer)
        to prevent this exception: TypeError: reduce() of empty sequence with no initial value. The initializer is the 
        value returned if the sequence is empty and is used as the first argument in the reducing loop, so it should be
        the identity value of the operation."""
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))
    def __bool__(self):
        return bool(abs(self))
    def angle(self, n):
        r = math.sqrt(sum(x * x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a
    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        # normal format method:
        # components = (format(c, fmt_spec) for c in self)
        # return '({}, {})'.format(*components)  # format(1/2.43, '0.4f') --- '0.4115'/ format(2/3, '.1%') --- '66.7%'/
        # format(datetime.now(), '%H:%M:%S') --- '18:49:05'
        # how to extend format specification methods?

        ## costum format method (end with p representing angle)
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)  # we don't need unpacking with * as we did before.
#9.7 module
# 模块（module）
# 模块化，模块化指将一个完整的程序分解为一个一个小的模块
#   通过将模块组合，来搭建出一个完整的程序
# 不采用模块化，统一将所有的代码编写到一个文件中
# 采用模块化，将程序分别编写到多个文件中
#   模块化的有点：
#       ① 方便开发
#       ② 方便维护
#       ③ 模块可以复用！

# 在Python中一个py文件就是一个模块，要想创建模块，实际上就是创建一个python文件
# 注意：模块名要符号标识符的规范

# 在一个模块中引入外部模块
# ① import 模块名 （模块名，就是python文件的名字，注意不要py）
# ② import 模块名 as 模块别名
#   - 可以引入同一个模块多次，但是模块的实例只会创建一个
#   - import可以在程序的任意位置调用，但是一般情况下，import语句都会统一写在程序的开头
#   - 在每一个模块内部都有一个__name__属性，通过这个属性可以获取到模块的名字
#   - __name__属性值为 __main__的模块是主模块，一个程序中只会有一个主模块
#       主模块就是我们直接通过 python 执行的模块
import test_module as test

# print(test.__name__)
print(__name__)
# import m

# # 访问模块中的变量：模块名.变量名
# # print(m.a , m.b)

# # m.test2()

# p = m.Person()

# print(p.name)

def test2():
    print('这是主模块中的test2')


# 也可以只引入模块中的部分内容
# 语法 from 模块名 import 变量,变量....
# from m import Person
# from m import test
# from m import Person,test
# from m import * # 引入到模块中所有内容，一般不会使用
# p1 = Person()
# print(p1)
# test()
# test2()

# 也可以为引入的变量使用别名
# 语法：from 模块名 import 变量 as 别名
# from m import test2 as new_test2

# test2()
# new_test2()

from m import *
# print(_c)

# import xxx
# import xxx as yyy
# from xxx import yyy , zzz , fff
# from xxx import *
# from xxx import yyy as zz

#9.8 package
# 包 Package
# 包也是一个模块
# 当我们模块中代码过多时，或者一个模块需要被分解为多个模块时，这时就需要使用到包
# 普通的模块就是一个py文件，而包是一个文件夹
#   包中必须要一个一个 __init__.py 这个文件，这个文件中可以包含有包中的主要内容
from hello import a , b

print(a.c)
print(b.d)

# __pycache__ 是模块的缓存文件
# py代码在执行前，需要被解析器先转换为机器码，然后再执行
#   所以我们在使用模块（包）时，也需要将模块的代码先转换为机器码然后再交由计算机执行
#   而为了提高程序运行的性能，python会在编译过一次以后，将代码保存到一个缓存文件中
#   这样在下次加载这个模块（包）时，就可以不再重新编译而是直接加载缓存中编译好的代码即可

# python standard packages
# 开箱即用
# 为了实现开箱即用的思想，Python中为我们提供了一个模块的标准库
# 在这个标准库中，有很多很强大的模块我们可以直接使用，
#   并且标准库会随Python的安装一同安装
# sys模块，它里面提供了一些变量和函数，使我们可以获取到Python解析器的信息
#   或者通过函数来操作Python解析器
# 引入sys模块
import sys

# pprint 模块它给我们提供了一个方法 pprint() 该方法可以用来对打印的数据做简单的格式化
import pprint

# sys.argv
# 获取执行代码时，命令行中所包含的参数
# 该属性是一个列表，列表中保存了当前命令的所有参数
# print(sys.argv)

# sys.modules
# 获取当前程序中引入的所有模块
# modules是一个字典，字典的key是模块的名字，字典的value是模块对象
# pprint.pprint(sys.modules)

# sys.path
# 他是一个列表，列表中保存的是模块的搜索路径
# ['C:\\Users\\lilichao\\Desktop\\resource\\course\\lesson_06\\code',
# 'C:\\dev\\python\\python36\\python36.zip',
# 'C:\\dev\\python\\python36\\DLLs',
# 'C:\\dev\\python\\python36\\lib',
# 'C:\\dev\\python\\python36',
# 'C:\\dev\\python\\python36\\lib\\site-packages']
# pprint.pprint(sys.path)

# sys.platform
# 表示当前Python运行的平台
# print(sys.platform)

# sys.exit()
# 函数用来退出程序
# sys.exit('程序出现异常，结束！')
# print('hello')

# os 模块让我们可以对操作系统进行访问
import os

# os.environ
# 通过这个属性可以获取到系统的环境变量
# pprint.pprint(os.environ['path'])

# os.system()
# 可以用来执行操作系统的名字
# os.system('dir')
os.system('notepad')

# 10 files and exceptions
"""第七章 异常和文件
异常
程序在运行过程当中，不可避免的会出现一些错误，比如：
    使用了没有赋值过的变量
    使用了不存在的索引
    除0
    ...
这些错误在程序中，我们称其为异常。
程序运行过程中，一旦出现异常将会导致程序立即终止，异常以后的代码全部都不会执行！    
处理异常
程序运行时出现异常，目的并不是让我们的程序直接终止！
Python是希望在出现异常时，我们可以编写代码来对异常进行处理！    

try语句
    try:
        代码块（可能出现错误的语句）
    except 异常类型 as 异常名:
        代码块（出现错误以后的处理方式）
    except 异常类型 as 异常名:
        代码块（出现错误以后的处理方式）
    except 异常类型 as 异常名:
        代码块（出现错误以后的处理方式）
    else：
        代码块（没出错时要执行的语句）    
    finally:
        代码块（该代码块总会执行）    

    try是必须的 else语句有没有都行
    except和finally至少有一个    

可以将可能出错的代码放入到try语句，这样如果代码没有错误，则会正常执行，
    如果出现错误，则会执行expect子句中的代码，这样我们就可以通过代码来处理异常
    避免因为一个异常导致整个程序的终止            
异常的传播（抛出异常）
当在函数中出现异常时，如果在函数中对异常进行了处理，则异常不会再继续传播,
    如果函数中没有对异常进行处理，则异常会继续向函数调用处传播,
    如果函数调用处处理了异常，则不再传播，如果没有处理则继续向调用处传播
    直到传递到全局作用域（主模块）如果依然没有处理，则程序终止，并且显示异常信息

当程序运行过程中出现异常以后，所有的异常信息会被保存一个专门的异常对象中，
    而异常传播时，实际上就是异常对象抛给了调用处
    比如 ： ZeroDivisionError类的对象专门用来表示除0的异常
            NameError类的对象专门用来处理变量错误的异常
            ....

在Python为我们提供了多个异常对象            
抛出异常
- 可以使用 raise 语句来抛出异常，
    raise语句后需要跟一个异常类 或 异常的实例
文件（File）
- 通过Python程序来对计算机中的各种文件进行增删改查的操作
- I/O(Input / Output)
- 操作文件的步骤：
    ① 打开文件
    ② 对文件进行各种操作（读、写），然后保存
    ③ 关闭文件"""
# Files and File Paths
from pathlib import Path

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))
    # C:\Users\Al\accounts.txt
    # C:\Users\Al\details.csv
    # C:\Users\Al\invite.docx
# The Current Working Directory
from pathlib import Path
import os

Path.cwd()
# WindowsPath('C:/Users/jliu471/PycharmProjects/pythonNBAProject')'
os.chdir('C:\\Windows\\System32')  # change working directory
Path.cwd()

# The Home Directory
Path.home()  # WindowsPath('C:/Users/jliu471')

# Absolute vs. Relative Paths
# An absolute path, which always begins with the root folder
# A relative path, which is relative to the program’s current working directory

# Creating New Folders Using the os.makedirs() Function
import os

os.makedirs('C:\\delicious\\walnut\\waffles')
from pathlib import Path

Path(r'C:\Users\Al\spam').mkdir()

# Handling Absolute and Relative Paths
Path.cwd()
# WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')
Path.cwd().is_absolute()
# True
Path('spam/bacon/eggs').is_absolute()
# False

Path('my/relative/path')  # relative path
# WindowsPath('my/relative/path')
Path.cwd() / Path('my/relative/path')  # absolute path
# WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37/my/relative/path')

# 10.1 reading an entire file
with open('C:/Users/jliu471/Desktop/python project 1/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)  # use print(cintents,rstrip()) to remove last empty line.
# 10.2 reading line by line
filename = 'C:/Users/jliu471/Desktop/python project 1/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())  # eliminates extra blink
# readlines function
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
# 10.3 working with a file's contents
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
# use strip to get rid of whitespace
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

# 10.4 writing to a file
# 10.4.1 writing to an empty file
filename = 'programming.txt'
with open(filename, 'w') as file_object:  # w means we want to open the file in write mode.
    # read mode: r (default value)
    # write mode: w
    # append mode: a
    # read and write model: r+
    file_object.write("I love programming.")
# add lines on separate lines
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love programming.\n")

# appending to a file
filename = 'programming.txt'
with open(filename, 'a') as file_object:  # you will add two lines to the existing filename.
    file_object.write("I love programming.\n")
    file_object.write("I love programming.\n")
# 10.5 exceptions
# 10.5.1 handling the ZeroDivisionError Exception
try:
    print(5 / 0)
except ZeroDivisionError:
    print('you cannot divide by zero!')

# 10.5.2 using exceptions to prevents crashes
while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input("second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('cannot divided by zero.')
    else:
        print(answer)
# 10.5.3 handling FileNotFoundError exception
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"{filename} does not exist"
    print(msg)


# 10.5.4 multiple files
def count_words(filename) -> string:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "doesn't exist"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print(num_words)


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


# 10.5.5 failing silently
def count_words(filename) -> string:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(num_words)


# 10.6 store data
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)  # data and filename

import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
# 10.7 saving and reading user-generated data
username = input("what is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print(f"we will remember {username}")


# 11 testing your code
def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()


# 12 organizing files

# 12.1 Copying Files and Folders
import shutil, os
from pathlib import Path

p = Path.home()
shutil.copy(p / 'spam.txt', p / 'some_folder')  # shutil.copy() call copies the file at C:\Users\Al\spam.txt to the
# folder C:\Users\Al\some_folder.
shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')  # gives the copied file the name eggs2.txt.

import shutil, os
from pathlib import Path

p = Path.home()
shutil.copytree(p / 'spam', p / 'spam_backup')  # creates a new folder named spam_backup with the same content as the
# original spam folder

# 12.2 Moving and Renaming Files and Folders
import shutil

shutil.move('C:\\bacon.txt', 'C:\\eggs')  # Move C:\bacon.txt into the folder C:\eggs. If there had been a bacon.txt
# file already in C:\eggs, it would have been overwritten. But if there is no eggs folder, then move() will rename
# bacon.txt to a file named eggs.
'C:\\eggs\\bacon.txt'
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')  # or change file name

# 12.3 Permanently Deleting Files and Folders
import os
from pathlib import Path

for filename in Path.home().glob('*.rxt'):
    # os.unlink(filename) # then uncomment this line to delete file
    print(filename)
# 12.3.1 Safe Deletes with the send2trash Module Using send2trash is much safer than Python’s regular delete
# functions, because it will send folders and files to your computer’s trash or recycle bin instead of permanently
# deleting them.
import send2trash

baconFile = open('bacon.txt', 'a')  # creates the file
baconFile.write('Bacon is not a vegetable.')
25
baconFile.close()
send2trash.send2trash('bacon.txt')

# 12.4 Walking a Directory Tree
import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\jliu471'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')

# 12.5 Compressing Files with the zipfile Module
import zipfile, os
# Reading ZIP Files
from pathlib import Path

p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.namelist()
# ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
# 13908
spamInfo.compress_size
# 3828
f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!'
# 'Compressed file is 3.63x smaller!'
exampleZip.close()

# Extracting from ZIP Files
import zipfile, os
from pathlib import Path

p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.extractall()
exampleZip.close()

# Creating and Adding to ZIP Files
import zipfile

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

# 13 Web Scraping
import webbrowser

webbrowser.open('https://inventwithpython.com/')
# 13.1 Project: mapIt.py with the webbrowser Module
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
# 13.2 Downloading Files from the Web with the requests Module
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])
# 13.3 Checking for Errors
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

  File "C:\Users\Al\AppData\Local\Programs\Python\Python37\lib\site-packages\requests\models
.py", line 940, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://inventwithpython
.com/page_that_does_not_exist.html"""
# 13.4 Saving Downloaded Files to the Hard Drive
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')  # wb means write binary mode, to maintain the Unicode encoding of the text.
for chunk in res.iter_content(100000):
    playFile.write(chunk)

"""100000
78981"""

playFile.close()
# 13.5 Creating a BeautifulSoup Object from HTML
import requests, bs4

res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup)

# 13.6 Starting a selenium-Controlled Browser (elenium module is better than requests when These sites may refuse to
# serve pages to you after a while, breaking any scripts you’ve made)
from selenium import webdriver

browser = webdriver.Firefox()
type(browser)
browser.get('https://inventwithpython.com')

# 13.7 Downloading with concurrent.futures
import os
import time
import sys
from concurrent import futures
POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR CD FR')  # 20 most popular countries
BASE_URL = 'http://flupy.org/data/flags'  # the website with the flag image
DEST_DIR = 'downloads/'  # local directory where images are saved
MAX_WORKERS = 20  # maximum number of threads to be used in the ThreadPoolExecutor
def save_flag(img, filename):  # inputs: images data and their names; save to DEST_DIR/name.
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)
def get_flag(cc):  # given a country code, build the URL and download the image, returning the binary contents of the response.
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower)
    resp = requests.get(url)
    return resp.content
def show(text):  # display a string and flush sys.stdout so we can see progress in a one-line display.
    print(text, end='')
    sys.stdout.flush()
def download_one(cc):  # function to download a single image; this is what each thread will execute
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ' .gif')
    return cc
def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))  # set number of workers threads so no unnecessary threads are created.
    with futures.ThreadPoolExecutor(workers) as executor:  # instantiate the ThreadPoolExecutor with that number of
        # worker threads; the executor.__exit__ method will call executor.shutdown(wait=True), which will block until
        # all threads are done.
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))
def main(download_many):  # main records and reports the elapsed time after running donwnload_many.
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))
main(download_many)
# additional learning from python basics
# 1 set
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is both unordered and unindexed.

# Sets are written with curly brackets.
myset = {"apple", "banana", "cherry"}

# join and split
# iterable objects can be joined
a = ['moose', 'cat', 'dog']
s = '==='
b = s.join(a)
# split
b.split('===', maxsplit=1)

# reference (ID)
# for all basic data type, same value has same id for all variables
a = 1
b = 1  # a and b have same id

a = 'abc'
b = 'abc'  # a and b have same id
# for all aggregate data type, same value has differnt ids for all variables
a = [1, 2, 3]
id(a)
a = [1, 2, 3]  # a and b have different ids
id(a)

# mutable and immutable:
"""developers encode immutable objects and use immutable objects to make mutable objects. for 
all immutable objects, they have unique reference/address, same content same address; for mutable objects, 
same content have different address mutable: list, dict, set immutable: int, float, bool, string, unicode, 
tuple"""
a = [1, 2, 3]
b = a
b.append(4)
a  # a also has 4
# how to copy list, dict, and set content not address:
b = a[:]  # list
original = {1:'one', 2:'two'}
new = original.copy()  # dict
first = {'g', 'e', 'e', 'k', 's'}
second = first.copy()  # set
print(id(first),id(second))
# shallow copy and deep copy
id(y)
import copy

a = [[1, 2, 3], [4, 5, 6]]
b = copy.deepcopy(a)
b[0][0] = 9
print(a)  # a[0][0] is 1, not 9.
c = copy.copy(a)
c[0][0] = 9
print(a)  # a[0][0] is 9, not 1.

# Ending a Program Early with the sys.exit() Function
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

# decimal to character and character to decimal
"""a = [1,2,3]
print(id(a))
a[0] = 2
print(id(a))"""

# size of different data type
import sys
print(sys.getsizeof('10'),  # 56
sys.getsizeof(['10']),  # 64
sys.getsizeof({1:'10'}),  # 232
sys.getsizeof({'10'}),  # 216
sys.getsizeof(10))  # 28

a = [1,2,3,3,4,5,6,6,7]
b = a[2:5]
print(id(a),id(b))
