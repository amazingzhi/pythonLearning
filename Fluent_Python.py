from collections import Counter
# Part 2: Data Structures
# chapter 2: An array of sequences
# 2.1 ListComp and Generator Expressions
# 2.1.1 ListComp and Readability
import collections

symbols = '$%^&*('
codes = [ord(symbol) for symbol in symbols]
print(codes)
# 2.1.2 Listcomps vs map and filter
symbols = '$%^&*('
beyond_ascii = [ord(s) for s in symbols if ord(s) >= 40]  # listcomp
beyond_ascii = list(filter(lambda s: s >= 40, map(ord, symbols)))  # filter and map
print(beyond_ascii)
# 2.1.3 Cartesian Products (example of listcomp that has two or more iterables)
colors = ['red', 'yellow', 'white']
sizes = ['s', 'm', 'l']
tshirts = [(color, size) for color in colors for size in sizes]  # how to do listcomp in doulbe for loop
print(tshirts)  # [('red', 's'), ('red', 'm'), ('red', 'l'), ('yellow', 's'), ('yellow', 'm'), ('yellow', 'l'),
                    # ('white', 's'), ('white', 'm'), ('white', 'l')]
# 2.1.3 generator expression
    # you could also start from a listcomp to initialize tuples, arrays, and other types of sequences
symbols = '$%^&*('
print(tuple(ord(symbol) for symbol in symbols))
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))

# 2.2 Tuples are not just immutable lists
# 2.2.1 Tuples as Records (history, location that do not change)
lax_coordinates = (33.9425, -118.4080)  # latitude and longitude of the LA airport
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # data about tokyo: name, year,
                                                                        # population, population change, area
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]  # a list of tuples of
                                                                                # the form (country id, passport number)
for passport in sorted(traveler_ids):  # as we iterate over the list, passport is bound to each tuple
    print(passport)
for country, _ in traveler_ids:  # the for loop knows how to retrieve the items of a tuple separately--this is called
                                # unpacking. we are not interested in the second item,
                                # so it is assigned to _, a dummy variable.
    print(country)
# 2.2.2 tuple unpacking
# unpacking is an application of swapping the values of variables
a = 1
b = 2
a,b = b,a  # a = 2, b = 1
# prefixing an argument with a star when calling a function
def print_all(*numbers):
    return [number for number in numbers]
print(print_all(10,20,30,40))
# nested tuple unpacking
seq_nested = (('A', 'Apple'), ('B', 'Boat'), ('C', 'Cat'))
for i, (letter, word) in enumerate(seq_nested):
  print(i, letter, word)

# 2.3 Slicing
# 2.3.1 Using + and * with sequence
my_list = [[]] * 3
print(my_list)  # [[], [], []]
# 2.3.2 building list of lists
# comparison between for i in range(n) and * n
board_1 = [['_']*3 for i in range(3)]  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board_2 = [['_'] * 3] * 3  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']] all rows referencing to the same object
board_1[1][2] = 'X'
board_2[1][2] = 'X'
print(board_1)  # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
print(board_2)  # [['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]

# 2.4 Augmented assignment with sequences
# mutable
l = [1,2,3]
print(id(l))  # 2117702129152
l *= 2
print(id(l))  # 2117702129152
# immutable
l = (1,2,3)
print(id(l))  # 2117702118208
l *= 2
print(id(l))  # 2117702000800

# A += Assignment Puzzler
t = (1,2, [30,40])
t[2] += [50,60]  """Traceback (most recent call last):
  File "<input>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment"""
print(t)  # (1, 2, [30, 40, 50, 60])

# list..sort and the sorted Build-in Function
"""functions or methods that change an object in place should return None to make it clear to the caller that the
object itself was changed, and no new object was created."""

# 2.5 managing ordered sequences with bisect
# importing "bisect" for bisection operations
import bisect
"""1. bisect(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in 
argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the 
list, the right most position where element has to be inserted is returned. This function takes 4 arguments, list which
 has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered."""
# initializing list
li = [1, 3, 4, 4, 4, 6, 7]

# using bisect() to find index to insert new element
# returns 5 ( right most possible index )
print("The rightmost index to insert, so list remains sorted is  : ", end="")
print(bisect.bisect(li, 4))

# using bisect_left() to find index to insert new element
# returns 2 ( left most possible index )
print("The leftmost index to insert, so list remains sorted is  : ", end="")
print(bisect.bisect_left(li, 4))

# using bisect_right() to find index to insert new element
# returns 4 ( right most possible index )
print("The rightmost index to insert, so list remains sorted is  : ", end="")
print(bisect.bisect_right(li, 4, 0, 4))
"""Output:The rightmost index to insert, so list remains sorted is  : 5
The leftmost index to insert, so list remains sorted is  : 2
The rightmost index to insert, so list remains sorted is  : 4"""

# Python code to demonstrate the working of
# insort(), insort_left() and insort_right()

# importing "bisect" for bisection operations
import bisect

# initializing list
li1 = [1, 3, 4, 4, 4, 6, 7]

# initializing list
li2 = [1, 3, 4, 4, 4, 6, 7]

# initializing list
li3 = [1, 3, 4, 4, 4, 6, 7]

# using insort() to insert 5 at appropriate position
# inserts at 6th position
bisect.insort(li1, 5)

print("The list after inserting new element using insort() is : ")
for i in range(0, 7):
    print(li1[i], end=" ")

# using insort_left() to insert 5 at appropriate position
# inserts at 6th position
bisect.insort_left(li2, 5)

print("\r")

print("The list after inserting new element using insort_left() is : ")
for i in range(0, 7):
    print(li2[i], end=" ")

print("\r")

# using insort_right() to insert 5 at appropriate position
# inserts at 5th position
bisect.insort_right(li3, 5, 0, 4)

print("The list after inserting new element using insort_right() is : ")
for i in range(0, 7):
    print(li3[i], end=" ")
"""Output: The list after inserting new element using insort() is : 
1 3 4 4 4 5 6 
The list after inserting new element using insort_left() is : 
1 3 4 4 4 5 6 
The list after inserting new element using insort_right() is : 
1 3 4 4 5 4 6 """

# 2.6 when a list is not the answer
"""
List: for store data
Dict: for search data
array: for store only numeric
tuple: for records, packing and unpacking
set: for containment check
queue: constantly adding and removing items form the ends of a list as a FIFO"""
# 2.6.1 Array
# creating, saving, and loading a large array of floats
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
fp = open('float.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

# 2.6.2 deque and other queues
"""Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over a list 
in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an
 O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity."""

# Python code to demonstrate deque


from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB'])

print(queue)
# initializing deque
de = deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("The deque after appending at left is : ")
print(de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("The deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("The deque after deleting from left is : ")
print(de)

# initializing deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])

# using index() to print the first occurrence of 4
print("The number 4 first occurs at a position : ")
print(de.index(4, 2, 5))

# using insert() to insert the value 3 at 5th position
de.insert(4, 3)

# printing modified deque
print("The deque after inserting 3 at 5th position is : ")
print(de)

# using count() to count the occurrences of 3
print("The count of 3 in deque is : ")
print(de.count(3))

# using remove() to remove the first occurrence of 3
de.remove(3)

# printing modified deque
print("The deque after deleting first occurrence of 3 is : ")
print(de)

# Chapter 3 Dictionary and sets
# 1. Generic Mapping type
"""because dictionary belongs to so many datatypes, there are many ways to build a dictionry"""
a = dict(one=1, two=2, three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one','two','three'],[1,2,3]))
d = dict([('two',2), ('one',1), ('three',3)])
e = dict({'three':3, 'one':1, 'two': 2})
print(a==b==c==d==e)

# 2. dict comprehension
Dial_Codes = [(86, 'China'), (54, 'India'), (91, 'USA')]
country_code = {country:code for code, country in Dial_Codes}
print(country_code)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Check for items greater than 2
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}
print(dict1_cond)  # {'e': 5, 'c': 3, 'd': 4}

# multiple if conditions
dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
print(dict1_doubleCond)  # {'d': 4}

# if else condition
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
# Identify odd and even entries
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}
print(dict1_tripleCond)  # {'f': 'even', 'c': 'odd', 'b': 'even', 'd': 'even', 'e': 'odd', 'a': 'odd'}

# Nested Dictionary Comprehension
nested_dict = {'first':{'a':1}, 'second':{'b':2}}
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)  # {'first': {1.0}, 'second': {2.0}}

# 3. overview of common mapping methods
# 3.1 OrderedDict
"""An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. The only difference 
between dict() and OrderedDict() is that:
OrderedDict preserves the order in which the keys are inserted. A regular dict doesn’t track the insertion order and 
iterating it gives the values in an arbitrary order. By contrast, the order the items are inserted is remembered by 
OrderedDict."""

# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)
"""This is a Dict:
a 1
c 3
b 2
d 4

This is an Ordered Dict:
a 1
b 2
c 3
d 4"""

"""
some general rules
1. Key value Change: If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.
2. Deletion and Re-Inserting: Deleting and re-inserting the same key will push it to the back as OrderedDict, however, 
maintains the order of insertion.
"""
# methods additions compared to dict
# 1. move_to_end
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
od.move_to_end('a',['last'])
print(od)  # OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])
od.move_to_end('a',False)  # False: back to first
print(od) # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# reverse existing ordered dict
y = OrderedDict(reversed(list(od.items())))
print(y)
y.popitem()  # pop last item
y.popitem(last=False) # pop first item
# 3.2 defaultdict
"""Sometimes, when the KeyError is raised, it might become a problem. To overcome this Python introduces another 
dictionary like container known as Defaultdict which is present inside the collections module.
The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises
a KeyError. It provides a default value for the key that does not exists.
"""

"""Syntax: defaultdict(default_factory)
Parameters:  

default_factory: A function returning the default value for the dictionary defined. If this argument is absent then the
 dictionary raises a KeyError."""
from collections import defaultdict

# Defining the dict and passing
# lambda as default_factory argument
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])  # Not Present
# Provides the default value for the key
print(d.__missing__('a'))  # Not Present
print(d.__missing__('d'))  # Not Present

# Using List as default_factory
# Python program to demonstrate
# defaultdict
from collections import defaultdict
# Defining a dict
d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print("Dictionary with values as list:")
print(d)  # defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})

# 3.3 collection.Counter
"""A Counter is a subclass of dict. Therefore it is an unordered collection where elements and their respective count
 are stored as a dictionary. This is equivalent to a bag or multiset of other languages."""

# A Python program to show different ways to create

# Counter
from collections import Counter
# With sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))  # Counter({'B': 5, 'A': 3, 'C': 2})
# with dictionary
print(Counter({'A': 3, 'B': 5, 'C': 2}))  # Counter({'B': 5, 'A': 3, 'C': 2})
# with keyword arguments
print(Counter(A=3, B=5, C=2))  # Counter({'B': 5, 'A': 3, 'C': 2})

# empty counter and Updation :
# A Python program to demonstrate update()
from collections import Counter
coun = Counter()  # empty counter
coun.update([1, 2, 3, 1, 2, 1, 1, 2])  # insert values
print(coun)  # Counter({1: 4, 2: 3, 3: 1})
coun.update([1, 2, 4])  # update
print(coun)  # Counter({1: 5, 2: 4, 3: 1, 4: 1})

# Subtraction: Counts can be zero and negative also.
from collections import Counter
c1 = Counter(A=4, B=3, C=10)
c2 = Counter(A=10, B=3, C=4)
c1.subtract(c2)
print(c1)  #  Counter({'c': 6, 'B': 0, 'A': -6})

# We can use Counter to count distinct elements of a list or other collections.
# Create a list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
# Count distinct elements and print Counter aboject
print(Counter(z))  # Counter({'blue': 3, 'red': 2, 'yellow': 1})

# most_common
c2.most_common(2)  # [('A', 10), ('C', 4)]

#3.4 Chain Map
"""Python contains a container called “ChainMap” which encapsulates many dictionaries into one unit."""
from collections import ChainMap
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
# Defining the chainmap
c = ChainMap(d1, d2, d3)
print(c)  # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

# Operations
# printing chainMap using maps
print("All the ChainMap contents are : ")
print(c.maps)  # [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
# printing keys using keys()
print("All keys of ChainMap are : ")
print(list(c.keys()))  # ['e', 'f', 'c', 'd', 'a', 'b']
# printing keys using keys()
print("All values of ChainMap are : ")
print(list(c.values()))  # [5, 6, 3, 4, 1, 2]

# initializing dictionaries
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
dic3 = {'f': 5}
# initializing ChainMap
chain = ChainMap(dic1, dic2)
# printing chainMap using map
print("All the ChainMap contents are : ")
print(chain.maps)  # [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)
# printing chainMap using map
print("Displaying new ChainMap : ")
print(chain1.maps)  # [{'f': 5}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
# displaying value associated with b before reversing
print("Value associated with b before reversing is : ", end="")
print(chain1['b'])  # 2
# reversing the ChainMap
chain1.maps = reversed(chain1.maps)
# displaying value associated with b after reversing
print("Value associated with b after reversing is : ", end="")
print(chain1['b'])  # 3

# 3.5 UserDict
"""This class acts as a wrapper class around the dictionary objects. This class is useful when one wants to create a 
dictionary of their own with some modified functionality or with some new functionality. It can be considered as a way 
of adding new behaviors to the dictionary. This class takes a dictionary instance as an argument and simulates a 
dictionary that is kept in a regular dictionary. The dictionary is accessible by the data attribute of this class."""
import collections
# todo: Do not inherite from build-in datatypes!!! Use UserDict or UserList!!!
class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)
dd = DoppelDict2(one=1)  # {'one': [1,1]}
dd['two'] = 2  # {'two':[2,2], 'one':[1,1]}
dd.update(three=3)  # {'two':[2,2], 'three': [3,3], 'one':[1,1]}

class AnswerDict2(collections.UserDict):
    def __getitem__(self, item):
        return 42
ad = AnswerDict2(a='foo')
ad['a']  # 42
d = {}
d.update(ad)
d['a']  # 42
d  # {'a':42}
# 4. Immutable Mapping
"""mapping proxy instance is a read only but dynamic view of the orignal mapping!"""
from types import MappingProxyType
d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
d_proxy[2] = 'x'  # TypeError: 'mappingproxy' object does not support item assignment
d[2] = 'B'
print(d_proxy)  # {1: 'A', 2: 'B'}

# 5. Set theory
"""set elements must be hashable. The set type is not hashable, but frozenset is, so you can have frozenset elements 
inside a set."""
# 5.1 Set Comprehension
from unicodedata import name
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')})
# 5.2 Set Operation
# 5.2.1 Union
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1 | x2)  # {'quux', 'foo', 'bar', 'qux', 'baz'}
print(x1.union(x2))  # {'quux', 'foo', 'bar', 'qux', 'baz'}
"""When you use the | operator, both operands must be sets. The .union() method, on the other hand, will take any 
iterable as an argument, convert it to a set, and then perform the union."""
x1 | ('baz', 'qux', 'quux')  # TypeError: unsupported operand type(s) for |: 'set' and 'tuple'
x1.union(('baz', 'qux', 'quux'))  # {'baz', 'quux', 'qux', 'bar', 'foo'}
# More than two sets may be specified with either the operator or the method:
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
a.union(b, c, d)  # {1, 2, 3, 4, 5, 6, 7}
a | b | c | d  # {1, 2, 3, 4, 5, 6, 7}

# 5.2.2 Intersection
print(x1.intersection(x2))  # {'baz'}
x1 & x2  # {'baz'}

# 5.2.3 difference
x1.difference(x2)  # x1 - x2 {'foo', 'bar'}
a.difference(b, c)
a - b - c

# 5.2.4 symmetric difference (a + b - a intersect b)
x1.symmetric_difference(x2)  # {'foo', 'qux', 'quux', 'bar'}
x1 ^ x2  # {'foo', 'qux', 'quux', 'bar'}
a ^ b ^ c  # {100, 5, 10}
a.symmetric_difference(b, c)  # TypeError: symmetric_difference() takes exactly one argument (2 given)

# 5.2.5 disjoint &/issubset <=
x1.isdisjoint(x2)  # False
x1.isdisjoint(x2 - {'baz'})  # True
x1 & x2  # set()
x1.issubset({'foo', 'bar', 'baz', 'qux', 'quux'})  # True
x1 <= x2  # False

# 5.3 Modifying a set
x1.update(['corge', 'garply'])
x1 |= x2  # same as above
x1.intersection_update(['baz', 'qux'])
x1 &= x2 # same as above
x1.difference_update(['foo', 'bar', 'qux'])
x1 -= x2  # same as above
x1.symmetric_difference_update(['qux', 'corge'])
x1 ^= x2  # same as above

# other methods
x = {'foo', 'bar', 'baz'}
x.add('qux')
x.remove('baz')  # x.remove(<elem>) removes <elem> from x. Python raises an exception if <elem> is not in x:
x.discard('baz')  # x.discard(<elem>) also removes <elem> from x. However, if <elem> is not in x, this method quietly
# does nothing instead of raising an exception:
x.pop()  # x.pop() removes and returns an arbitrarily chosen element from x. If x is empty, x.pop() raises an exception:
x.clear()

# 5.4 frozenset
""" frozenset is immutable, cannot be modified"""

# 5.5 Python RegEx
"""RegEx can be used to check if a string contains the specified search pattern."""
import re
    # Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
    # The findall() Function:
            # Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)  # ['ai', 'ai']
            # Return an empty list if no match was found:
x = re.findall("Portugal", txt)
print(x)  # []
    # The search() Function: The search() function searches the string for a match, and returns a Match object if there is a match.
        # Search for the first white-space character in the string:
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())  # 3
        # Make a search that returns no match:
x = re.search("Portugal", txt)
print(x)  # None
    # The split() Function: The split() function returns a list where the string has been split at each match
        # Split at each white-space character:
x = re.split("\s", txt)
print(x)
        # Split the string only at the first occurrence:
x = re.split("\s", txt, 1)
print(x)
    # The sub() Function: The sub() function replaces the matches with the text of your choice:
        # Replace every white-space character with the number 9:
x = re.sub("\s", "9", txt)
print(x)
        # Replace the first 2 occurrences:
x = re.sub("\s", "9", txt, 2)
print(x)
    # Match Object
        # Do a search that will return a Match Object
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object  # <re.Match object; span=(5, 7), match='ai'>
    # .span() returns a tuple containing the start-, and end positions of the match.
        # Print the position (start- and end-position) of the first match occurrence.
x = re.search(r"\bS\w+", txt)
print(x.span())  # (12, 17)
    # .string returns the string passed into the function
        # Print the string passed into the function:
print(x.string)  # The rain in Spain
    # .group() returns the part of the string where there was a match
        # Print the part of the string where there was a match.
print(x.group())

