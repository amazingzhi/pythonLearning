## Python for Probability
# Vectorized operations
import numpy as np

samples = np.random.binomial(10, 0.2, size=10000)
samples.shape  # Get array shape: (10000,)
np.mean(samples)  # Mean over array: 1.9961
# Counting Operations
import math

print(math.factorial(20))  # Compute n! as an integer.
from math import comb

print(comb(10, 5))  # compute (nm) from the math module
# Using SciPy
# Binomial distribution
from scipy import stats

X = stats.binom(10, 0.2)  # Declare X to be a binomial random variable
print(X.pmf(3))  # P(X = 3)
print(X.cdf(4))  # P(X <= 4)
print(X.mean())  # E[X]
print(X.var())  # Var(X)
print(X.std())  # Std(X)
print(X.rvs())  # Get a random sample from X
print(X.rvs(10))  # Get 10 random samples form X
# Poisson distribution
from scipy import stats

Y = stats.poisson(2)  # Declare Y to be a poisson random variable
print(Y.pmf(3))  # P(Y = 3)
print(Y.rvs())  # Get a random sample from Y
# Geometric distribution
from scipy import stats

X = stats.geom(0.75)  # Declare X to be a geometric random variable
print(X.pmf(3))  # P(X = 3)
print(X.rvs())  # Get a random sample from Y
# Normal
import math
from scipy import stats

A = stats.norm(3, math.sqrt(16))  # Declare A to be a normal random variable
print(A.pdf(4))  # f(3), the probability density at 3
print(A.cdf(2))  # F(2), which is also P(Y < 2)
print(A.rvs())  # Get a random sample from A
# Exponential
from scipy import stats

B = stats.expon(4)  # Declare B to be an exponential random variable
print(B.pdf(1))  # f(1), the probability density at 1
print(B.cdf(2))  # F(2) which is also P(B < 2)
print(B.rvs())  # Get a random sample from B
# Beta
from scipy import stats

X = stats.beta(1, 3)  # Declare X to be a beta random variable
print(X.pdf(0.5))  # f(0.5), the probability density at 1
print(X.cdf(0.7))  # F(0.7) which is also P(X < 0.7)
print(X.rvs())  # Get a random sample from X

# 1. Core Probability
# 1.1 Counting
# 1.2 Combinatorics
import itertools

# 1.2.1 permutation of distinct object
# get all 4! = 24 permutations of 1,2,3,4 as a list:
list(itertools.permutations([1, 2, 3, 4]))
list(itertools.permutations([1, 1, 2]))
# 1.2.2 permutation of indistinct object
# get all 3!/2! = 3 unique permutations of 1,1,2 as a set:
set(itertools.permutations([1, 1, 2]))
# 1.2.3 Combinations of Distinct Objects
# Get all ways of chosing three numbers from [1,2,3,4,5]
list(itertools.combinations([1, 2, 3, 4, 5], 3))


# 2.2 Probability Mass Function
def pmf_sum_two_dice(y):
    # Returns the probability that the sum of two dice is y
    if y < 2 or y > 12:
        return 0
    if y <= 7:
        return (y - 1) / 36
    else:
        return (13 - y) / 36
# 2.3 expectations
def expectation_sum_two_dice():
    exp_sum_two_dice = 0
    # sum of dice can take on the values 2 through 12
    for x in range(2, 13):
        pr_x = pmf_sum_two_dice(x) # pmf gives Pr(x)
        exp_sum_two_dice += x * pr_x
    return exp_sum_two_dice
print(expectation_sum_two_dice())
from collections import Counter
(Counter("abcde") - Counter("abcd")).keys()

