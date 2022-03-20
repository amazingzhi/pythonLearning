# Lesson 1 - Binary Search, Linked Lists and Complexity
"""Here's a systematic strategy we'll apply for solving problems:

1. State the problem clearly. Identify the input & output formats.
2. Come up with some example inputs & outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6."""

"""QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given
number by turning over as few cards as possible. Write a function to help Bob locate the card. """

# 1. State the problem clearly. Identify the input & output formats.
"""Problem We need to write a program to find the position of a given number in a list of numbers arranged in 
    decreasing order. We also need to minimize the number of times we access elements from the list. 
    Input
        cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
        query: A number, whose position in the array is to be determined. E.g. 7
    Output
        position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)"""


# Based on the above, we can now create the signature of our function:
def locate_card(cards, query):
    pass


# 2. Come up with some example inputs & outputs (build test cases). Try to cover all edge cases (list all possible
# variations).
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
# The function can now be tested as follows.
print(locate_card(**test['input']) == test['output'])
# list all possible variations
"""The number query occurs somewhere in the middle of the list cards.
query is the first element in cards.
query is the last element in cards.
The list cards contains just one element, which is query.
The list cards does not contain number query.
The list cards is empty.
The list cards contains repeating numbers.
The number query occurs at more than one position in cards.
(can you think of any more variations?)"""
# create some more test cases for the variations listed above for easier testing.
tests = []
# query occurs in the middle
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})
# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})
# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})
# cards does not contain query
# We will assume that our function will return -1 in case cards does not contain query.
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})
# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})
# numbers can repeat in cards (In the case where query occurs multiple times in cards, we'll expect our function to
# return the first occurrence of query).
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})
# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})
"""Tip: Don't stress it if you can't come up with an exhaustive list of test cases though. You can come back to this 
section and add more test cases as you discover them. Coming up with good test cases is a skill that takes practice. """

# 3. Come up with a correct solution for the problem. State it in plain English.
"""In this problem, coming up with a correct solution is quite easy: Bob can simply turn over cards in order one by 
one, till he find a card with the given number on it. Here's how we might implement it: 

Create a variable position with the value 0.
Check whether the number at index position in card equals query.
If it does, position is the answer and can be returned from the function
If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
If the number was not found, return -1."""


# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
def locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0

    # Set up a loop for repetition
    while position < len(cards):

        # Check if element at the current position matche the query
        if cards[position] == query:
            # Answer found! Return and exit..
            return position

        # Increment the position
        position += 1

    # Check if we have reached the end of the array
    return -1


# To help you test your functions easily the jovian Python library provides a helper function evalute_test_case
from jovian.pythondsa import evaluate_test_cases

evaluate_test_cases(locate_card, tests)

# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.

# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3-6

# 7. Come up with a correct solution for the problem. State it in plain English.
"""Here's how binary search can be applied to our problem:

Find the middle element of the list.
If it matches queried number, return the middle position as the answer.
If it is less than the queried number, then search the first half of the list
If it is greater than the queried number, then search the second half of the list
If no more elements remain, return -1."""


# 8. Implement the solution and test it using example inputs. Fix bugs, if any.
def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'


def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

    return -1


evaluate_test_cases(locate_card, tests)

# 9. Analyze the algorithm's complexity and identify inefficiencies, if any.
"""
linear search: N
Binary search: log N
"""


# Generic Binary Search
def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


# We can now rewrite the locate_card function more succinctly using the binary_search function.
def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)


# practice one: rotate list
"""You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to 
determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function 
should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the 
numbers in the list are unique. 

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. 
rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4]. 

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7]."""

import math


def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while (left <= right):
        mid = math.floor(left + (right - left) / 2)
        print(mid)
        if (nums[mid] == target):
            return mid
        if (nums[0] <= nums[mid]):  # mid was originally after pivot point
            if (target >= nums[0] and target < nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        else:  # mid was originally before pivot point
            if (target <= nums[len(nums) - 1] and target > nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
    return -1
# practice 2
"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to 
search target in nums. If target exists, then return its index. Otherwise, return -1. """
def search(nums: list[int], target: int) -> int:
    def bSearch(nums, low, high, targ):
        if high >= low:
            mid = low+(high-low)//2
            if nums[mid] == targ:
                return mid
            elif nums[mid] > targ:
                return bSearch(nums, low, mid-1, targ)
            else:
                return bSearch(nums, mid+1, high, targ)
        else:
				return -1
	return bSearch(nums, 0, len(nums)-1, target)
# practice 3
