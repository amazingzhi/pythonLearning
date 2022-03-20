# easy
# 1. Two Sum
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:  # dictionary takes (1) to search value.
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

# 9. Palindrome Number
"""Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not."""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])  # reverse slicing
class Solution:  # faster than above
    def isPalindrome(self, x: int) -> bool:
        if len(str(x)) < 2:
            return True
        elif str(x)[0] != str(x)[-1]:
            return False
        return self.isPalindrome(str(x)[1:-1])
# Follow up: Could you solve it without converting the integer to a string?
class Solution:
    def isPalindrome(self, x):
        if x > 0:
            temp = x
            rev_int_elements = []
            while temp > 0:
                digit = temp % 10
                rev_int_elements.append(digit)
                temp = temp // 10
            org_int_elements = rev_int_elements[::-1]
            return rev_int_elements == org_int_elements
        elif x == 0:
            return True
        else:
            return False
# 13. Roman to Integer
"""Given a roman numeral, convert it to an integer."""
class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}

        size = len(s)
        current = 0
        old = 0
        total = 0
        i = 0
        while i < size:
            current = rom[s[i]]
            i += 1
            if current <= old:
                total += old
                old = current
                continue
            old = current - old
        total += old
        return total

# 14. Longest Common Prefix
"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        res = ''
        strs = sorted(strs)  # after sorted, the difference between first and last item is the biggest. So we can
        # compare the first and last to get the common for the whole list.
        for i in strs[0]:
            if strs[-1].startswith(res + i):
                res += i
            else:
                break
        return res

# 20. Valid Parentheses
"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order."""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0  # 3

# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket

# 21. Merge Two Sorted Lists
"""ou are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists."""
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

# 53. Maximum Subarray
"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest 
sum and return its sum. 

A subarray is a contiguous part of an array."""


class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)  # compare whether add next number or use next number
            maxSum = max(maxSum, curSum)  # compare whether use last number or new number

        return maxSum


# 66. Plus One
"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the 
integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer 
does not contain any leading 0's. 

Increment the large integer by one and return the resulting array of digits.
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - 1 - i))
        return [int(i) for i in str(num + 1)]  # int to string and then split to int


# 70. Climbing Stairs
"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""
from functools import lru_cache, reduce


class Solution:
    @lru_cache(None)
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 118. Pascal's Triangle
"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        elif numRows == 3:
            return [[1], [1, 1], [1, 2, 1]]
        last = self.generate(numRows - 1)
        last_last = last[-1]
        new_list = [last_last[i] + last_last[i + 1] for i in range(len(last_last) - 1)]
        last.append([1] + new_list + [1])
        return last


# 121. Best time to buy and sell stock
"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
to sell that stock. 

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)  # for each price, keep changing minimum price.
            profit = price - min_price  # calculate current profit by current price.
            max_profit = max(max_profit, profit)  # see if current profit is bigger than past max profit.
        return max_profit


# 136. Single Number
"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)  # Bitwise xor operator: Returns 1 if one of the bits is 1 and the
        # other is 0 else returns false. todo: that means x ^ x = 0.


# 168. Excel Sheet Column Title
"""Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet."""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1  # 26 -> "Z"
            res += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26
        return res[::-1]


# 171. Excel Sheet Column Number
"""Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number."""


def titleToNumber(self, s):
    return reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x) - ord('A') + 1, s))


# 190. Reverse Bits
"""Reverse bits of a given 32 bits unsigned integer."""


class Solution:
    def reverseBits(self, n: int) -> int:
        oribin = '{0:032b}'.format(n)
        reversebin = oribin[::-1]
        return int(reversebin, 2)


# 202. Happy Number
"""rite an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy."""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1  # if the final n is not 1, that means this number is endless because it goes to an internal
        # loop again


# 205. Isomorphic Strings (same as 290)
"""Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No 
two characters may map to the same character, but a character may map to itself. """


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# 290. Word Pattern (same as 205)
"""Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s."""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s1 = pattern
        t = s.split()
        return len(set(zip(s1, t))) == len(set(s1)) == len(set(t)) and len(s1) == len(t)

# 217. Contains Duplicate
"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if 
every element is distinct. """


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


# 219. Contains Duplicate II
"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k. """


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False


# 231. Power of Two
"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x."""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) and (n & (n - 1)) == 0  # binary operation

# 326. Power of Three
"""Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x."""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return  n > 0 == 3**19 % n

# # 326. Power of Three
"""Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x."""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n != 0 and n &(n-1) == 0 and n & 1431655765== n
# 258. Add Digits
"""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it."""


class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = reduce(lambda a, b: int(a) + int(b), list(str(num)))
        return num


# 263. Ugly Number
"""An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number."""


class Solution:
    def isUgly(self, n: int) -> bool:
        for p in 2, 3, 5:
            while n % p == 0 < n:
                n /= p
        return n == 1


# 268. Missing Number
"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is 
missing from the array. """


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = set(range(len(nums) + 1)) - set(nums)
        return res.pop()


# 278. First Bad Version (binary search)
"""You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version 
of your product fails the quality check. Since each version is developed based on the previous version, 
all the versions after a bad version are also bad. 

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following 
ones to be bad. 

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find 
the first bad version. You should minimize the number of calls to the API. """
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        badVersion = -1

        while low <= high:

            mid = low + (high - low) // 2

            if isBadVersion(mid) == True:
                badVersion = mid
                high = mid - 1

            else:
                low = mid + 1

        return badVersion

# 283. Move Zeroes
"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero 
elements. 
Note that you must do this in-place without making a copy of the array."""
# solution only for 0s.
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=bool, reverse=True)
# solution for all
# in-place
def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
# 345. Reverse Vowels of a String
"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases."""
import re
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

# 349. Intersection of Two Arrays
"""Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must 
be unique and you may return the result in any order. """
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))  # binary intersection is faster than set.intersection(set)

# 350. Intersection of Two Arrays II
"""Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must 
appear as many times as it shows in both arrays and you may return the result in any order. """
from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())
class Solution(object):  # twice faster than first one.
    def intersect(self, nums1, nums2):

        counts = Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res
# 367. Valid Perfect Square
"""Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt."""
def NewtonMethod(num):
    r = num
    while r * r > num:
        r = (r + num / r) // 2
    return r * r == num

# 383. Ransom Note
"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false 
otherwise. 
Each letter in magazine can only be used once in ransomNote."""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

# 389. Find the Difference
"""You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t."""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        return list(Counter(t) - Counter(s))[0]

# 392. Is Subsequence
"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of 
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence 
of "abcde" while "aec" is not). """
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)  # once you used iter() object, it is gone.
        return all(c in t for c in s)