# C1: get started with scientific python
# 1.2 Numpy
import numpy as np
x = np.array([1,2,3],dtype=np.float32)  # array([1.,2.,3.], dtype=float32): creates an array of 32 bit floating-point
                                        # numbers.
print(x.itemsize)  # 4: shows number of bytes per item
    # element-wise sine using numpy
print(np.sin(np.array([1,2,3],dtype=np.float32)))  # [0.841471  0.9092974 0.14112  ]: numpy is faster than buildin
                                                    # math because no looping
    # 2d array (the maximum is 32 dimensions)
x = np.array([[1,2,3],[4,5,6]])  # construct 2d array
x.shape  # (2,3)
x.size  # 6
x.dtype  # dtype(int64)

    # np.identity() to create a square 2d array with 1's across the diagonal
np.identity(n = 5)      # Size of the array

    # np.eye() to create a 2d array with 1's across a specified diagonal
np.eye(N = 3,  # Number of rows
       M = 5,  # Number of columns
       k = 1)  # Index of the diagonal (main diagonal (0) is default)

    # slicing: similar to list
x[:,0]
x[:,1]
x[0,:]
x[1,:]
x[:,1:]
x[:,::2]
x[:,::-1]  # reverse columns

    # Reshaping Arrays
np.reshape(a=x,        # Array to reshape
           newshape=(6,3))       # Dimensions of the new array
    # Unravel a multi-dimensional into 1 dimension with np.ravel():
np.ravel(a=x,
         order='C')         # Use C-style unraveling (by rows)
np.ravel(a=x,
         order='F')         # Use Fortran-style unraveling (by columns)
    # Alternatively, use ndarray.flatten() to flatten a multi-dimensional into 1 dimension and return a copy of the result:
x.flatten()
    # Get the transpose of an array with ndarray.T:
x.T
    # Flip an array vertically or horizontally with np.flipud() and np.fliplr() respectively:
np.flipud(x)  # ud: up down
np.fliplr(x)  # lr: left right
    # Rotate an array 90 degrees counter-clockwise with np.rot90():
np.rot90(x,
         k=1)             # Number of 90 degree rotations
    # Shift elements in an array along a given dimension with np.roll():
np.roll(a= x,
        shift = 2,        # Shift elements 2 positions
        axis = 1)         # In each row
    # Leave the axis argument empty to shift on a flattened version of the array (shift across all dimensions):
np.roll(a= x,
        shift = 2)
    # Join arrays along an axis with np.concatenate():
array_to_join = np.array([[10,20,30],[40,50,60],[70,80,90]])

np.concatenate( (x,array_to_join),  # Arrays to join
               axis=1)                        # Axis to join upon
# 1.2.1 Numpy Arrays and Memory
    # same array extension
x = np.ones((3,3))  # [[1. 1. 1.]
                     # [1. 1. 1.]
                     # [1. 1. 1.]]
print(x[:,[0,1,2,2]])  # notice duplicated last dimension
"""[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]"""
    # np.zeros() to create an array filled with zeros:
np.zeros(shape= [4,6])
    # todo View vs Copy (id of np is useless, we use .base(), if view, return original numpy; if copy, return None).
    # View
y = x[:2,:2]
x[0,0] =999
print(y)
"""[[999.   1.]
 [  1.   1.]]"""
    # Copy
y = x[[0,1]]
x[0,0] =999
print(y)
"""[[1. 1. 1.]
 [1. 1. 1.]]"""
    # or make a copy of original np
y = x.copy()
    # create overlapping blocks that do not consume additional memory
from numpy.lib.stride_tricks import as_strided
x = np.arange(16,dtype=np.int64)  # [0,1,...,15]
y = as_strided(x,(7,4),(16,8))  # overlaps the entries to create a 7*4 Numpy array. The final argument in the
                                # as_strided function are the strides, which are the steps in bytes to move in the
    # row and column dimensions, respectively. Because the integer elements in the Numpy array are eight bytes (int64/8 = 8),
    # this is equivalent to moving by one element in the column dimension and by two elements in the row dimension.
print(y)
"""[[ 0  1  2  3]
 [ 2  3  4  5]
 [ 4  5  6  7]
 [ 6  7  8  9]
 [ 8  9 10 11]
 [10 11 12 13]
 [12 13 14 15]]"""
    # reassigning elements in the original x array
x[::2] = 99
print(x)  # [99  1 99  3 99  5 99  7 99  9 99 11 99 13 99 15]
print(y)
"""[[99  1 99  3]
 [99  3 99  5]
 [99  5 99  7]
 [99  7 99  9]
 [99  9 99 11]
 [99 11 99 13]
 [99 13 99 15]]"""

# 1.2.2 Numpy Matrices
"""Matrices in Numpy are similar to Numpy arrays but they can only have two dimensions. They implement row–column 
matrix multiplication as opposed to elementwise multiplication. Matrix objects are a subclass of ndarray, 
so they inherit all the attributes and methods of ndarrays. """
import numpy as np
    # Matrix
A=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
x=np.matrix([[1],[0],[0]])
A*x
"""matrix([[1],
[4],
[7]])"""
    # Array
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
x=np.array([[1],[0],[0]])
A.dot(x)
A @ x  # same result as above under python 3.x
"""array([[1],
[4],
[7]])"""

"""It is unnecessary to cast all multiplicands to matrices for multiplication. In the
next example, everything until last line is a Numpy array and thereafter we cast the
array as a matrix with np.matrix which then uses row–column multiplication. Note
that it is unnecessary to cast the x variable as a matrix because the left-to-right order
of the evaluation takes care of that automatically."""
A=np.ones((3,3))
type(A) # array not matrix: <class 'numpy.ndarray'>
x=np.ones((3,1)) # array not matrix
A*x
"""array([[1., 1., 1.],
[1., 1., 1.],
[1., 1., 1.]])"""
np.matrix(A)*x # row-column multiplication
"""matrix([[3.],
[3.],
[3.]])"""

# 1.2.3 Numpy Broadcasting
    # meshgrid
# Sample code for generation of first example
x = np.linspace(-4, 4, 9)

# numpy.linspace creates an array of
# 9 linearly placed elements between
# -4 and 4, both inclusive
y = np.linspace(-5, 5, 11)

# The meshgrid function returns
# two 2-dimensional arrays
x_1, y_1 = np.meshgrid(x, y)

print("x_1 = ")
print(x_1)
print("y_1 = ")
print(y_1)
"""x_1 = 
[[-4. -3. -2. -1.  0.  1.  2.  3.  4.]
 [-4. -3. -2. -1.  0.  1.  2.  3.  4.]
 [-4. -3. -2. -1.  0.  1.  2.  3.  4.]
 [-4. -3. -2. -1.  0.  1.  2.  3.  4.]
 [-4. -3. -2. -1.  0.  1.  2.  3.  4.]
 [-4. -3. -2. -1.  0.  1.  2.  3.  4.]
 [-4. -3. -2. -1.  0.  1.  2.  3.  4.]
 [-4. -3. -2. -1.  0.  1.  2.  3.  4.]
 [-4. -3. -2. -1.  0.  1.  2.  3.  4.]
 [-4. -3. -2. -1.  0.  1.  2.  3.  4.]
 [-4. -3. -2. -1.  0.  1.  2.  3.  4.]]
y_1 = 
[[-5. -5. -5. -5. -5. -5. -5. -5. -5.]
 [-4. -4. -4. -4. -4. -4. -4. -4. -4.]
 [-3. -3. -3. -3. -3. -3. -3. -3. -3.]
 [-2. -2. -2. -2. -2. -2. -2. -2. -2.]
 [-1. -1. -1. -1. -1. -1. -1. -1. -1.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 1.  1.  1.  1.  1.  1.  1.  1.  1.]
 [ 2.  2.  2.  2.  2.  2.  2.  2.  2.]
 [ 3.  3.  3.  3.  3.  3.  3.  3.  3.]
 [ 4.  4.  4.  4.  4.  4.  4.  4.  4.]
 [ 5.  5.  5.  5.  5.  5.  5.  5.  5.]]"""
    # add broadcast dimension
x = np.array([0,1])
y = np.array([0,1])
x  #  array([0, 1])
y  # array([0, 1])
x + y[:,None]  # the None Python singleton tells Numpy to make copies of y
"""array([[0, 1],
[1, 2]])"""
    # Scalar and One-Dimensional Array
a = np.array([1, 2, 3])
print(a)  # [1 2 3]
b = 2
print(b)  # 2
c = a + b
print(c)  # [3 4 5]
    # Scalar and Two-Dimensional Array
A = np.array([[1, 2, 3], [1, 2, 3]])
print(A)  # [[1 2 3] [1 2 3]]
b = 2
print(b)  # 2
C = A + b
print(C)  # [[3 4 5] [3 4 5]]
    # One-Dimensional and Two-Dimensional Arrays
A = np.array([[1, 2, 3], [1, 2, 3]])
print(A)
b = np.array([1, 2, 3])
print(b)
C = A + b
print(C)

# 1.2.4 Numpy Masked Arrays
"""This is particularly useful in plotting categorical data, where you may only want those values that correspond to 
a given category for part of the plot. Another common use is for image processing, wherein parts of the image may 
need to be excluded from subsequent processing """
from numpy import ma # import masked arrays
x = np.arange(10)
y = ma.masked_array(x, x<5)
print(y)  # [-- -- -- -- -- 5 6 7 8 9]
print (y.shape)  # (10,)
# changing an element in x does change the corresponding element in y, even though y is a masked array
x[-1] = 99 # change this
print(x)  # [ 0 1 2 3 4 5 6 7 8 99]
print(y)  # masked array changed! [-- -- -- -- -- 5 6 7 8 99]

# 1.2.5 floating-point Numbers
"""To sum up, when using floating point, you must check for approximate equality using something like Numpy allclose 
instead of the usual Python equality (i.e., ==) sign."""

# 1.2.6 Numpy Optimizations and Prospectus
""". Several important extensions to Numpy are under active development. First,
Numba is a compiler that generates optimized machine code from pure-Python code
using the LLVM compiler infrastructure.
The Dask project contains dask.array extensions for manipulating very large
datasets that are too big to fit in a single computer’s RAM (i.e., out of core) using
Numpy semantics. Furthermore, dask includes extensions for Pandas dataframes
(see Sect. 1.7).
"""

# 1.2.7 Array Math Operations
np.mean(x)  # # Get the mean of all the elements in an array with np.mean()
np.mean(x,
        axis = 1)     # Get means of each row
np.std(x,
        axis = 0)     # Get stdev for each column
np.log(x)
np.sqrt(x)
    # Take the vector dot product of row 0 and row 1
np.dot(x[0,0:],  # Slice row 0
       x[1,0:])  # Slice row 1

# 1.3 Matplotlib
"""Matplotlib is the primary visualization tool for scientific graphics in Python. Like all
great open-source projects, it originated to satisfy a personal need. """
    # example
import matplotlib.pyplot as plt
plt.plot(range(10))
plt.show()

# 1.3.1 Alternatives to Matplotlib
"""If you require real-time data display and tools for volumetric data rendering and
complicated 3D meshes with isosurfaces, then PyQtGraph is an option."""
"""An alternative that comes from the R community is ggplot which is a Python
port of the ggplot2 package that is fundamental to statistical graphics in R."""

# 1.3.2 Extensions to Matplotlib
"""For statistical plots, the first place to look is the seaborn module that includes a vast array of beautifully 
formatted plots including violin plots, kernel density plots, and bivariate histograms. The seaborn gallery includes 
samples of available plots and the corresponding code that generates them. Note that importing seaborn hijacks the 
default settings for all plots, so you have to coordinate this if you only want to use seaborn for some (not all) of 
your visualizations in a given session. """

# 1.4 IPython
"""IPython [3] originated as a way to enhance Python’s basic interpreter for smooth
interactive scientific development."""

# 1.5 Jupyter Notebook
"""The genius of the IPython development team
was to leverage these technologies for scientific computing by embedding IPython
in modern web browsers. In fact, this strategy has been so successful that IPython
has moved into other languages beyond Python such as Julia and R as the Jupyter
project. """

# 1.6 Scipy
"""Scipy was the first consolidated module for a wide range of compiled libraries, all based on Numpy arrays. Scipy 
includes numerous special functions (e.g., Airy, Bessel, elliptical) as well as powerful numerical quadrature 
routines via the QUADPACK Fortran library (see scipy.integrate), where you will also find other quadrature methods. """

# 1.7 Pandas
"""Pandas [4] is a powerful module that is optimized on top of Numpy and provides
a set of data structures particularly suited to time series and spreadsheet-style data
analysis (think of pivot tables in Excel). If you are familiar with the R statistical
package, then you can think of Pandas as providing a Numpy-powered dataframe for
Python."""

# 1.7.1 Series
"""There are two primary data structures in Pandas. The first is the Series object which
combines an index and corresponding data values."""
import pandas as pd # recommended convention
x=pd.Series(index = range(5),data=[1,3,9,11,12])
x
"""0 1
1 3
2 9
3 11
4 12
dtype: int64"""
    # In the general case, the index must be a sort-able array-like entity.
x=pd.Series(index = ['a','b','d','z','z'],data=[1,3,9,11,12])
x
"""a 1
b 3
d 9
z 11
z 12
dtype: int64"""  # Note the duplicated z entries in the index. We can get at the entries in the Seriesin a number of
                # ways. First, we can used the dot notation to select as in the following:
x.a  # 1
x.z
"""z 11
z 12
dtype: int64"""
    # indexed position of the entries with iloc
x.iloc[:3]
"""a 1
b 3
d 9
dtype: int64"""
    # slice across the index, even if it is not numeric with loc
x.loc['a':'d']
"""a 1
b 3
d 9
dtype: int64"""
x = pd.Series(range(5),[1,2,11,9,10])
grp=x.groupby(lambda i:i%2)  # odd or even
grp.get_group(0)  # even group
grp.get_group(1)  # odd group
grp.max() # max in each group

# 1.7.2 Dataframe
"""The Pandas DataFrame is an encapsulation of the Series that extends to two dimensions."""
df = pd.DataFrame({'col1': [1,3,11,2], 'col2': [9,23,0,2]})
df.iloc[:2,:2] # get section
df['col1'] # indexing
df.col1 # use dot notation
df.sum() # Subsequent operations
    # Grouping and aggregating
df = pd.DataFrame({'col1': [1,1,0,0], 'col2': [1,2,3,4]})
grp=df.groupby('col1')
grp.get_group(0)
grp.get_group(1)
grp.sum()
"""col2
col1
0 7
1 3"""
    # compute new columns
df['sum_col']=df.eval('col1+col2')
"""col1 col2 sum_col
0 1 1 2
1 1 2 3
2 0 3 3
3 0 4 4"""

# 1.8 Sympy
"""SymPy is a Python library for symbolic mathematics. It aims to become a full-featured computer algebra system (
CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible. SymPy is 
written entirely in Python. """

# 1.9
# Chapter 1.5 Descriptive Statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mtcars = pd.read_csv("../input/mtcars/mtcars.csv")
mtcars =  mtcars.rename(columns={'Unnamed: 0': 'model'})
mtcars.index = mtcars.model
del mtcars["model"]
    # descriptive statistics
mtcars.mean()  # mean
mtcars.mean(axis=1)  # means of each row
mtcars.median()   # Get the median of each column
mtcars.mode()  # appears most frequently
"""The columns with multiple modes (multiple values with the same count) return multiple values as the mode. Columns 
with no mode (no value that appears more than once) return NaN. """
mtcars["mpg"].var()
mtcars["mpg"].std()
mtcars["mpg"].skew()  # Check skewness
mtcars["mpg"].kurt()  # Check kurtosis
    # In a symmetric distribution, the mean and median will be the same. Let's investigate with a density plot:
norm_data = pd.DataFrame(np.random.normal(size=100000))
norm_data.plot(kind="density",
              figsize=(10,10))
plt.vlines(norm_data.mean(),     # Plot black line at mean
           ymin=0,
           ymax=0.4,
           linewidth=5.0)
plt.vlines(norm_data.median(),   # Plot red line at median
           ymin=0,
           ymax=0.4,
           linewidth=2.0,
           color="red")
    # In skewed distributions, the mean tends to get pulled in the direction of the skew, while the median tends to
    # resist the effects of skew:
skewed_data = pd.DataFrame(np.random.exponential(size=100000))
skewed_data.plot(kind="density",
              figsize=(10,10),
              xlim=(-1,5))
plt.vlines(skewed_data.mean(),     # Plot black line at mean
           ymin=0,
           ymax=0.8,
           linewidth=5.0)
plt.vlines(skewed_data.median(),   # Plot red line at median
           ymin=0,
           ymax=0.8,
           linewidth=2.0,
           color="red")
    # The mean is also influenced heavily by outliers, while the median resists the influence of outliers:
norm_data = np.random.normal(size=50)
outliers = np.random.normal(15, size=3)
combined_data = pd.DataFrame(np.concatenate((norm_data, outliers), axis=0))
combined_data.plot(kind="density",
              figsize=(10,10),
              xlim=(-5,20))
plt.vlines(combined_data.mean(),     # Plot black line at mean
           ymin=0,
           ymax=0.2,
           linewidth=5.0)
plt.vlines(combined_data.median(),   # Plot red line at median
           ymin=0,
           ymax=0.2,
           linewidth=2.0,
           color="red")
    # Measures of Spread
        # One of the simplest measures of spread is the range. Range is the distance between the maximum and minimum
        # observations:
max(mtcars["mpg"]) - min(mtcars["mpg"])
        # We can extract the minimum value (0th percentile), first quartile (25th percentile), median,
        # third quartile(75th percentile) and maximum value (100th percentile) using the quantile() function:
five_num = [mtcars["mpg"].quantile(0),
            mtcars["mpg"].quantile(0.25),
            mtcars["mpg"].quantile(0.50),
            mtcars["mpg"].quantile(0.75),
            mtcars["mpg"].quantile(1)]
        # use describe to see all of these measues
mtcars["mpg"].describe()
        # Interquartile (IQR) range is another common measure of spread. IQR is the distance between the 3rd quartile
        # and the 1st quartile:
mtcars["mpg"].quantile(0.75) - mtcars["mpg"].quantile(0.25)
        # The boxplots we learned to create in the lesson on plotting are just visual representations of the five number
        # summary and IQR:
mtcars.boxplot(column="mpg",
               return_type='axes',
               figsize=(8,8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)
    # To explore skew and kurt further, let's create some dummy data and inspect it:
norm_data = np.random.normal(size=100000)
skewed_data = np.concatenate((np.random.normal(size=35000)+2,
                             np.random.exponential(size=65000)),
                             axis=0)
uniform_data = np.random.uniform(0,2, size=100000)
peaked_data = np.concatenate((np.random.exponential(size=50000),
                             np.random.exponential(size=50000)*(-1)),
                             axis=0)

data_df = pd.DataFrame({"norm":norm_data,
                       "skewed":skewed_data,
                       "uniform":uniform_data,
                       "peaked":peaked_data})
data_df.skew()
data_df.kurt()

# 1.10 Data Exploration and Cleaning
    # Exploring The Variables
"""It is important to get a sense of how many variables and cases there are, the data types of the variables and the 
range of values they take on. """
titanic_train = pd.read_csv("../input/train.csv")      # Read the data
        # start off by checking the dimensions and the variable data types of df.dtypes.
titanic_train.shape      # Check dimensions
titanic_train.dtypes       # Warning raised when reading different dtypes in a column from a file.
        # After getting a sense of the data's structure, it is a good idea to look at a statistical summary of the
        # variables with df.describe():
titanic_train.describe()
"""Notice that non-numeric columns are dropped from the statistical summary provided by df.describe().
We can get a summary of the categorical variables by passing only those columns to describe():"""
        # describe only for categorial variables
categorical = titanic_train.dtypes[titanic_train.dtypes == "object"].index
print(categorical)
titanic_train[categorical].describe()

"""After looking at the data for the first time, you should ask yourself a few questions:

Do I need all of the variables?
Should I transform any variables?
Are there NA values, outliers or other strange values?
Should I create new variables?"""

    # Do I need all of the variables?
"""Getting rid of unnecessary variables is a good first step when dealing with any data set, since dropping variables 
reduces complexity and can make computation on the data faster. """
del titanic_train["PassengerId"]     # Remove PassengerId
    # Should I Transform Any Variables?
"""When you first load a data set, some of the variables may be encoded as data types that don't fit well with what 
the data really is or what it means. """
new_survived = pd.Categorical(titanic_train["Survived"])
new_survived = new_survived.rename_categories(["Died","Survived"])
new_survived.describe()
"""Pclass is an integer that indicates a passenger's class, with 1 being first class, 2 being second class and 3 
being third class. Passenger class is a category, so it doesn't make a lot of sense to encode it as a numeric 
variable. What's more 1st class would be considered "above" or "higher" than second class, but when encoded as an 
integer, 1 comes before 2. We can fix this by transforming Pclass into an ordered categorical variable: """
new_Pclass = pd.Categorical(titanic_train["Pclass"],
                           ordered=True)
new_Pclass = new_Pclass.rename_categories(["Class1","Class2","Class3"])
new_Pclass.describe()
titanic_train["Pclass"] = new_Pclass
"""If we grouped cabin just by this letter, we could reduce the number of levels while potentially extracting some 
useful information. """
char_cabin = titanic_train["Cabin"].astype(str) # Convert data to str
new_Cabin = np.array([cabin[0] for cabin in char_cabin]) # Take first letter
new_Cabin = pd.Categorical(new_Cabin)
new_Cabin.describe()
titanic_train["Cabin"] = new_Cabin
    # Are there NA Values, Outliers or Other Strange Values?
        # detect missing values with the pd.isnull() function:
dummy_vector = pd.Series([1,None,3,None,7,8])
dummy_vector.isnull()
"""Detecting missing values is the easy part: it is far more difficult to decide how to handle them. In cases where 
you have a lot of data and only a few missing values, it might make sense to simply delete records with missing 
values present. On the other hand, if you have more than a handful of missing values, removing records with missing 
values could cause you to get rid of a lot of data. Missing values in categorical data are not particularly troubling 
because you can simply treat NA as an additional category. Missing values in numeric variables are more troublesome, 
since you can't just treat a missing value as number. As it happens, the Titanic dataset has some NA's in the Age 
variable: """
titanic_train["Age"].describe()  # the count of age(712) is less than the total row count of hte data set(889). This
                    # indicates missing data. We can get the row indexes of the missing values with np.where():
missing = np.where(titanic_train["Age"].isnull() == True)
missing
"""Here are a few ways we could deal with them:
Replace the null values with 0s
Replace the null values with some central value like the mean or median
Impute some other value
Split the data set into two parts: one set with where records have an Age value and another set where age is null."""
titanic_train.hist(column='Age',    # Column to plot
                   figsize=(9,6),   # Plot size
                   bins=20)         # Number of histogram bins
new_age_var = np.where(titanic_train["Age"].isnull(), # Logical check
                       28,                       # Value if check is true
                       titanic_train["Age"])     # Value if check is false
titanic_train["Age"] = new_age_var
titanic_train["Age"].describe()
"""Similar to NA values, there's no single cure for outliers. You can keep them, delete them or transform them in 
some way to try to reduce their impact. Even if you decide to keep outliers unchanged it is still worth identifying 
them since they can have disproportionately large influence on your results. Let's keep the three high rollers 
unchanged. 

Data sets can have other strange values beyond missing values and outliers that you may need to address. Sometimes 
data is mislabeled or simply erroneous; bad data can corrupt any sort of analysis so it is important to address these 
sorts of issues before doing too much work. """
    # Should I Create New Variables?¶
"""The variables present when you load a data set aren't always the most useful variables for analysis. Creating new 
variables that are derivations or combinations existing ones is a common step to take before jumping into an analysis 
or modeling task. """
titanic_train["Family"] = titanic_train["SibSp"] + titanic_train["Parch"]
most_family = np.where(titanic_train["Family"] == max(titanic_train["Family"]))
titanic_train.loc[most_family]

# 1.11 Preparing Numeric Data
    # Centering and Scaling
"""The simplest way to center data is to subtract the mean value from each data point. Subtracting the mean centers 
the data around zero and sets the new mean to zero. Let's try zero-centering the mtcars dataset, a small set of 
car-related data. """
colmeans = mtcars.sum()/mtcars.shape[0]  # # Get column means
centered = mtcars-colmeans
centered.describe()
"""Now that the data is centered, we'd like to put it all on a common scale. One way to put data on a common scale is 
to divide by the standard deviation. """
column_deviations = mtcars.std(axis=0)  # Get column standard deviations
centered_and_scaled = centered/column_deviations
centered_and_scaled.describe()
"""Manually centering and scaling as we've done is a good exercise, but it is often possible to perform common data 
preprocessing automatically using functions built into Python libraries """
from sklearn import preprocessing
scaled_data = preprocessing.scale(mtcars)  # Scale the data*
    # Dealing With Skewed Data
"""Data with a long tail that goes off to the right is called positively skewed or right skewed. When you have a 
skewed distribution like the one above, the extreme values in the long tail can have a disproportionately large 
influence on whatever test you perform or models you build. Reducing skew may improve your results. Taking the square 
root of each data point or taking the natural logarithm of each data point are two simple transformations that can 
reduce skew. Let's see their effects on the skewed data: """
skewed = np.random.exponential(scale=2,      # Generate skewed data
                               size= 10000)
skewed = pd.DataFrame(skewed)                # Convert to DF
sqrt_transformed = skewed.apply(np.sqrt) # Get the square root of data points*
sqrt_transformed.hist(figsize=(8,8),     # Plot histogram
                 bins=50)
log_transformed = (skewed+1).apply(np.log)   # Get the log of the data
log_transformed.hist(figsize = (8,8),          # Plot histogram
                 bins=50)
    # Highly Correlated Variables
        # check the pairwise correlations between numeric variables using the df.corr() function
mtcars.iloc[:,0:6].corr()   # Check the pairwise correlations of 6 variables
        # A scatter plot matrix can be a helpful visual aide for inspecting collinearity.
from pandas.tools.plotting import scatter_matrix
scatter_matrix(mtcars.iloc[:,0:6], # Make a scatter matrix of 6 columns
               figsize=(10, 10),   # Set plot size
               diagonal='kde');    # Show distribution estimates on diagonal
"""If you find highly correlated variables, there are a few things you can do including:

Leave them be
Remove one or more variables
Combine them in some way
"""
    # Imputing with Sklearn
"""Imputation describes filling in missing data with estimates based on the rest of the data set. """
from sklearn.preprocessing import Imputer
        # The following line sets a few mpg values to None
mtcars["mpg"] = np.where(mtcars["mpg"]>22, None, mtcars["mpg"])
mtcars["mpg"]       # Confirm that missing values were added
        # Imputer fill in missing values based on the mean
imp = Imputer(missing_values='NaN',  # Create imputation model
              strategy='mean',       # Use mean imputation
              axis=0)                # Impute by column
imputed_cars = imp.fit_transform(mtcars)   # Use imputation model to get values
imputed_cars = pd.DataFrame(imputed_cars,  # Remake DataFrame with new values
                           index=mtcars.index,
                           columns = mtcars.columns)

# 1.12 Frequency Table
    # One-Way Tables
my_tab = pd.crosstab(index=titanic_train["Survived"],  # Make a crosstab
                     columns="count")                  # Name the count column
        # You can also use the value_counts() function to on a pandas series (a single column) to check its counts:
titanic_train.Sex.value_counts()
cabin_tab = pd.crosstab(index=titanic_train["Cabin"],  # Make a crosstab
                        columns="count")               # Name the count column
        # extract the proportion of the data that belongs to each category.
cabin_tab/cabin_tab.sum()
    # Two-Way Tables
"""Two-way frequency tables, also called contingency tables, are tables of counts with two dimensions where each 
dimension is a different variable. Two-way tables can give you insight into the relationship between two variables. """
survived_sex = pd.crosstab(index=titanic_train["Survived"],
                           columns=titanic_train["Sex"])
survived_sex.index= ["died","survived"]
        # Table of survival vs passenger class
survived_class = pd.crosstab(index=titanic_train["Survived"],
                            columns=titanic_train["Pclass"])

survived_class.columns = ["class1","class2","class3"]
survived_class.index= ["died","survived"]
        # Table of survival vs passenger class
survived_class = pd.crosstab(index=titanic_train["Survived"],
                            columns=titanic_train["Pclass"],
                             margins=True)   # Include row and column totals

survived_class.columns = ["class1","class2","class3","rowtotal"]
survived_class.index= ["died","survived","coltotal"]
            # get the total proportion of counts in each cell, divide the table by the grand total:
survived_class/survived_class.loc["coltotal","rowtotal"]
            # get the proportion of counts along each column:
survived_class/survived_class.loc["coltotal"]
            # get the proportion of counts along each row
survived_class.div(survived_class["rowtotal"],
                   axis=0)
            # transpose the table with df.T to swap rows and columns
survived_class.T/survived_class["rowtotal"]
    # Higher Dimensional Tables
surv_sex_class = pd.crosstab(index=titanic_train["Survived"],
                             columns=[titanic_train["Pclass"],
                                      titanic_train["Sex"]],
                             margins=True)   # Include row and column totals
        # The outermost index (Pclass) returns sections of the table instead of individual columns:
surv_sex_class[2]        # Get the subtable under Pclass 2
        # The secondary column index, Sex, can't be used as a top level index, but it can be used within a given Pclass:
surv_sex_class[2]["female"]   # Get female column within Pclass 2
        # Due to the convenient hierarchical structure of the table, we still use one division to get the proportion of survival across each column:
surv_sex_class/surv_sex_class.loc["All"]    # Divide by column totals

# 1.13  Plotting With Pandas
diamonds = pd.read_csv("../input/diamonds/diamonds.csv")
diamonds = diamonds.drop("Unnamed: 0", axis=1)
    # Histograms
diamonds.hist(column="carat",        # Column to plot
              figsize=(8,8),         # Plot size
              color="blue",          # Plot color
              bins=50,               # Use 50 bins
              range= (0,3.5));       # Limit x-axis range
diamonds[diamonds["carat"] > 3.5]  # pandas filter
    # Boxplots
diamonds.boxplot(column="price",        # Column to plot
                 by= "clarity",         # Column to split upon
                 figsize= (8,8));       # Figure size
    # Density Plots
diamonds["carat"].plot(kind="density",  # Create density plot
                      figsize=(8,8),    # Set figure size
                      xlim= (0,5));     # Limit x axis values
    # Barplots
carat_table = pd.crosstab(index=diamonds["clarity"], columns="count")
carat_table.plot(kind="bar",
                 figsize=(8,8),
                 stacked=False)  # grouped barplot; if True, horizontal barplot.
    # Scatterplots
diamonds.plot(kind="scatter",     # Create a scatterplot
              x="carat",          # Put carat on the x axis
              y="price",          # Put price on the y axis
              figsize=(10,10),
              ylim=(0,20000));    # y range
    # Line Plots
        # Create some data
years = [y for y in range(1950,2016)]
readings = [(y+np.random.uniform(0,20)-1900) for y in years]
time_df = pd.DataFrame({"year":years,
                        "readings":readings})
        # Plot the data
time_df.plot(x="year",
             y="readings",
             figsize=(9,9))
    # Saving Plots
my_plot = time_df.plot(x="year",     # Create the plot and save to a variable
             y="readings",
             figsize=(9,9))
my_fig = my_plot.get_figure()            # Get the figure
my_fig.savefig("line_plot_example.png")  # Save to file


# Chapter 2 Probability 2.1 introduction discrete variable probabilities what is the
# probability that the sum of the dice equals seven?
d={(i,j):i+j for i in range(1,7) for j in range(1,7)}  # for each set of (i and j), map to their sum.
        # inverse mapping
from collections import defaultdict
dinv = defaultdict(list)  # have to use defaultdict to use dic[key].append
for i,j in d.items():
    dinv[j].append(i)
print(dinv[7])  # [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]
        # compute the probability measured for each of these items
X={i:len(j)/36. for i,j in dinv.items()}
print(X)
"""{2: 0.027777777777777776, 3: 0.05555555555555555, 4: 0.08333333333333333, 5: 0.1111111111111111, 
6: 0.1388888888888889, 7: 0.16666666666666666, 8: 0.1388888888888889, 9: 0.1111111111111111, 10: 0.08333333333333333, 
11: 0.05555555555555555, 12: 0.027777777777777776} """

    # what is the probability that half the product (*) of three dice will exceed the their sum?
d={(i,j,k):((i*j*k)/2>i+j+k) for i in range(1,7) for j in range(1,7) for k in range(1,7)}  # The keys of this
# dictionary are the triples and the values are the logical values of whether or not half the product of three dice
# exceeds their sum.
        # inverse mapping
dinv = defaultdict(list)
for i,j in d.items():
    dinv[j].append(i)
X={i:len(j)/6.0**3 for i,j in dinv.items()}
print(X)  # {False: 0.37037037037037035, True: 0.6296296296296297}
    # two dice where we want the probability of a seven, but this time one of the dice is no longer fair. (Pandas)
"""The distribution for the unfair die is the following:
P({1}) = P({2}) = P({3}) = 1/9
P({4}) = P({5}) = P({6}) = 2/9
"""
from pandas import DataFrame
        # pandas index can be tuple.
d=DataFrame(index=[(i,j) for i in range(1,7) for j in range(1,7)], columns=['sm','d1','d2','pd1','pd2','p'])
        # the outcome of the first die is the d1 column and the outcome of the second die is d2
d.d1=[i[0] for i in d.index]
d.d2=[i[1] for i in d.index]
        #  the sum of the dices in the sm column
d.sm=list(map(sum,d.index))
        # fill out the probabilities for each face of the unfair die (d1) and the fair die (d2).
d.loc[d.d1 <= 3,'pd1'] = 1/9.  # pandas.loc can be used as filter
d.loc[d.d1 > 3,'pd1'] = 2/9.
d.pd2 = 1/6.
        # compute the joint probabilities for the sum of the shown faces
d.p = d.pd1 * d.pd2
        # compute the density of all the dice outcomes by using groupby
print(d.groupby('sm')['p'].sum())
"""sm
2     0.018519
3     0.037037
4     0.055556
5     0.092593
6      0.12963
7     0.166667
8     0.148148
9      0.12963
10    0.111111
11    0.074074
12    0.037037
Name: p, dtype: object"""

# 2.2 Projection
"""Figure 2.2 uses the matplotlib.patches module. This module contains
primitive shapes like circles, ellipses, and rectangles that can be assembled into
complex graphics. After importing a particular shape, you can apply that shape
to an existing axis using the add_patch method. The patches themselves can
by styled using the usual formatting keywords like color and alpha."""

# 2.3 conditional expectation
"""verify E(X − E(X|Y ))2 = E(X)2 − E(E(X|Y ))2"""
from sympy.abc import y,x
from sympy import integrate, simplify
fxy = x + y  # joint density
fy = integrate(fxy, (x,0,1))  # marginal density
fx = integrate(fxy, (y,0,1))  # marginal density
    # conditional expectation
EXY = integrate(x*(fxy/fy), (x,0,1))  # E(X|Y)
    # compute left side
LHS = integrate((x-EXY)**2*fxy, (x,0,1),(y,0,1))
    # compute the right side
RHS = integrate((x)**2*fx,(x,0,1))-integrate((EXY)**2*fy,(y,0,1))
integrate((x)**2*fx,(x,0,1))
integrate((x)**2,(x,0,1))
print(simplify(LHS-RHS)==0)

# 2.4 Conditional Expectation and Mean Squared Error
"""s. Suppose we have two fair six-sided dice (X and Y ) and
we want to measure the sum of the two variables as Z = X +Y . Further, let’s suppose
that given Z, we want the best estimate of X in the mean-squared-sense. """
import sympy as S
from sympy.stats import density, E, Die
x=Die('D1',6) # 1st six sided die
y=Die('D2',6) # 2nd six sides die
a=S.symbols('a')  # we use symbol for later simplify the equation.
z = x+y # sum of 1st and 2nd die
J = E((x-a*(x+y))**2) # expectation
print(S.simplify(J))  # 329*a**2/6 - 329*a/6 + 91/6
# With all that setup we can now use basic calculus to minimize the objective function J,
sol,=S.solve(S.diff(J,a),a) # using calculus to minimize
print(sol) # solution is 1/2
"""Sympy has a stats module that can do some basic work with expressions
involving probability densities and expectations. The above code uses its E
function to compute the expectation."""

import numpy as np
from sympy import stats
    # Eq constrains Z
samples_z7 = lambda : stats.sample(x, S.Eq(z,7))  # it generates random samples of x die, given that the sum of the
                                                    # outcomes of that die and the y die add up to z==7.
    #using 6 as an estimate
mn= np.mean([(6-samples_z7())**2 for i in range(100)])  # MSE calculation
    #7/2 is the MSE estimate
mn0= np.mean([(7/2.-samples_z7())**2 for i in range(100)])  # MSE calculation
print('MSE=%3.2f using 6 vs MSE=%3.2f using 7/2 ' % (mn,mn0))  # MSE=9.20 using 6 vs MSE=2.99 using 7/2
x=stats.FiniteRV('D3',{1:1/15., 2:1/15., 3:1/15., 4:1/15., 5:1/15., 6:2/3.})  # Create a Finite Random Variable given
                                                                                # a dict representing the density
E(x, S.Eq(z,7)) # conditional expectation E(x|z=7)

"""Three coins, 10, 20 and 50p are tossed. The values of the coins that land heads up are totaled. What is the expected 
total given that two coins have landed heads up? """
import sympy as S
X10,X20,X50 = S.symbols('X10,X20,X50', real=True)
xi = 10*X10+20*X20+50*X50
eta = X10*X20*(1-X50)+X10*(1-X20)*(X50)+(1-X10)*X20*(X50)
num=S.summation(xi*eta,(X10,0,1),(X20,0,1),(X50,0,1))  # Compute the summation of f with respect to symbols.
den=S.summation(eta*eta,(X10,0,1),(X20,0,1),(X50,0,1))
alpha=num/den
print(alpha) # alpha=160/3
    # quick simulation using pandas
import pandas as pd
d = pd.DataFrame(columns=['X10','X20','X50'])
d.X10 = np.random.randint(0,2,1000)  # randint(low, high=None, size=None, dtype=int)
d.X10 = np.random.randint(0,2,1000)
d.X20 = np.random.randint(0,2,1000)
d.X50 = np.random.randint(0,2,1000)
grp=d.groupby(d.eval('X10+X20+X50'))  # eval: Evaluate a string describing operations on DataFrame columns.
grp.get_group(2).eval('10*X10+20*X20+50*X50').mean()  # 52.60162601626016
    #  The following code shows that we can accomplish the same simulation using pure Numpy.
import numpy as np
from numpy import array
x=np.random.randint(0,2,(3,1000))
print(np.dot(x[:,x.sum(axis=0)==2].T,array([10,20,50])).mean())  # 52.860759493670884

"""Given X uniformly distributed on
[0, 1], find E(ξ|η) where
ξ(x) = 2x2
η(x) =
⎧
⎪⎨
⎪⎩
1 if x ∈ [0, 1/3]
2 if x ∈ (1/3, 2/3)
0 if x ∈ (2/3, 1]"""
x,c,b,a=S.symbols('x,c,b,a')
xi = 2*x**2
eta=S.Piecewise((1,S.And(S.Gt(x,0),
S.Lt(x,S.Rational(1,3)))), # 0 < x < 1/3
(2,S.And(S.Gt(x,S.Rational(1,3)),
S.Lt(x,S.Rational(2,3)))), # 1/3 < x < 2/3,
(0,S.And(S.Gt(x,S.Rational(2,3)),
S.Lt(x,1)))) # 1/3 < x < 2/3
h = a + b*eta + c*eta**2
J=S.integrate((xi-h)**2,(x,0,1))
sol=S.solve([S.diff(J,a),
S.diff(J,b),
S.diff(J,c),
],
(a,b,c))
print(sol)  # {a: 38/27, b: -20/9, c: 8/9}
print(S.piecewise_fold(h.subs(sol)))
"""Piecewise((2/27, (x > 0) & (x < 1/3)),
(14/27, (x > 1/3) & (x < 2/3)),
(38/27, (x > 2/3) & (x < 1)))"""
    # To reinforce our result, let’s do a quick simulation using Pandas.
d = pd.DataFrame(columns=['x','eta','xi'])
d.x = np.random.rand(1000)  # 1000 is the shape
d.xi = 2*d.x**2
pd.cut(d.x,[0, 1/3, 2/3, 1]).head()  # n use the pd.cut function to group the x values
d.groupby(pd.cut(d.x,[0,1/3,2/3,1])).mean()['xi']   # we know how to use pd.cut, we can just compute the mean on each group
"""x
(0.0, 0.333] 0.073048
(0.333, 0.667] 0.524023
(0.667, 1.0] 1.397096
Name: xi, dtype: float64"""

from pandas import DataFrame
import numpy as np
d = DataFrame(columns=['xi','eta','x','h','h1','h2'])
# 100 random samples
d.x = np.random.rand(100)
d.xi = d.eval('2*x**2')
d.eta =1-abs(2*d.x-1)
d.h1=d[(d.x<0.5)].eval('eta**2/2')
d.h2=d[(d.x>=0.5)].eval('(2-eta)**2/2')
d.fillna(0,inplace=True)
d.h = d.h1+d.h2
d.head()
from matplotlib.pyplot import subplots
fig,ax=subplots()
ax.plot(d.xi,d.eta,'.',alpha=.3,label='$\eta$')
ax.plot(d.xi,d.h,'k.',label='$h(\eta)$')
ax.legend(loc=0,fontsize=18)
ax.set_xlabel('$2 xˆ2$',fontsize=18)
ax.set_ylabel('$h(\eta)$',fontsize=18)

# 2.6 useful distributions
# 2.6.0 The Uniform Distribution
import pandas as pd
import scipy.stats as stats
uniform_data = stats.uniform.rvs(size=100000,  # Generate 100000 numbers
                                 loc = 0,      # From 0
                                 scale=10)     # To 10
pd.DataFrame(uniform_data).plot(kind="density",  # Plot the distribution
                               figsize=(9,9),
                               xlim=(-1,11))
stats.uniform.cdf(x=2.5,         # Cutoff value (quantile) to check
                  loc=0,         # Distribution start
                  scale=10)      # Distribution end = 0.25
stats.uniform.ppf(q=0.4,         # Probability cutoff
                  loc=0,         # Distribution start
                  scale=10)      # Distribution end = 4.0
    # Generating Random Numbers and Setting The Seed
import random
random.randint(0,10)     # Get a random integer in the specified range
random.choice([2,4,6,9]) # Get a random element from a sequence
random.random()          # Get a real number between 0 and 1
random.uniform(0,10)     # Get a real in the specified range
random.seed(12)  # Set the seed to an arbitrary value
print([random.uniform(0,10) for x in range(4)])
random.seed(12)  # Set the seed to the same value
print([random.uniform(0,10) for x in range(4)])  # same as line 975

# 2.6.1 normal distribution
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
    # create an array of random numbers taken from a normal distribution
np.random.seed(0)
x_rand = np.random.normal(loc=0, scale=1.0, size=1000)  # loc is mean, scale is std
    # histogram
sns.distplot(x_rand, kde=False)  # kde=False means no line just bar
    # histogram with different number of bins
sns.distplot(x_rand, bins=100, kde=False)  # bins control number of bars
    # histogram + kernel density estimate (default)
sns.distplot(x_rand)  # default kde=True
    # histogram + fitted normal distribution
sns.distplot(x_rand, fit=stats.norm, kde=False)  # also fits a line but not based on data but based on description of fit
    # fit a normal distribution
loc, scale = stats.norm.fit(x_rand)  # fit: return estimates of shape (if applicable), location, and scale parameters from data.
print('loc = {0}\tscale = {1}'.format(loc, scale))
    # Probability density function (PDF)
        # linearly spaced values of X
x = np.linspace(start=-5, stop=5, num=100)
        # PDF (probability density function)
pdf = stats.norm.pdf(x, loc=loc, scale=scale)
        # line plot of the PDF
plt.plot(x, pdf, color='black')
plt.xlabel('X')
plt.ylabel('PDF')
    # Cumulative distribution function (CDF)
        # CDF (cumulative distribution function)
cdf = stats.norm.cdf(x, loc=loc, scale=scale)
        # line plot of the CDF
plt.plot(x, cdf, color='black')
plt.xlabel('X')
plt.ylabel('CDF = P(x<=X)')
    # Percent point function (PPF)
        # linearly spaced values CDF
cdf_ = np.linspace(start=0, stop=1, num=10000)
        # x using 'ppf'
x_ = stats.norm.ppf(cdf_, loc=loc, scale=scale)
        # line plot of the CDF
plt.plot(x_, cdf_, color='black')
plt.xlabel('X')
plt.ylabel('CDF = P(x<=X)')
    # Use of the CDF
        # probability that the variable 𝑋 takes a value lower than 𝑥=1
cdf_1 = stats.norm.cdf(1, loc=loc, scale=scale)  # 0.8551974783788131
        # plot the variable 𝑋 takes a value lower than 𝑥=1
plt.plot(x, cdf, color='black')
plt.vlines(1, 0, cdf_1, linestyle=':')
plt.hlines(cdf_1, -5, 1, linestyle=':')
plt.xlabel('X')
plt.ylabel('CDF = P(x <= X)')
        # value 𝑥 that is not exceeded 99% of the time
x_99 = stats.norm.ppf(0.99, loc=loc, scale=scale)
plt.plot(x, cdf, color='black')
plt.hlines(.99, -5, x_99, linestyle=':')
plt.vlines(x_99, 0, .99, linestyle=':')
plt.xlabel('X')
plt.ylabel('CDF = P(x <= X)')

# 2.6.2 multinomial distribution (extension of binomial distribution)
    # The Binomial Distribution
"""For example, we could model flipping a fair coin 10 times with a binomial distribution where the number of trials 
is set to 10 and the probability of success is set to 0.5. In this case the distribution would tell us how likely it 
is to get zero heads, 1 head, 2 heads and so on. """
fair_coin_flips = stats.binom.rvs(n=10,        # Number of flips per trial
                                  p=0.5,       # Success probability
                                  size=10000)  # Number of trials
print( pd.crosstab(index="counts", columns= fair_coin_flips))
pd.DataFrame(fair_coin_flips).hist(range=(-0.5,10.5), bins=11)
stats.binom.cdf(k=5,        # Probability of k = 5 successes or less
                n=10,       # With 10 flips
                p=0.8)      # And success probability 0.8
1 - stats.binom.cdf(k=8,        # Probability of k = 9 successes or more
                    n=10,       # With 10 flips
                    p=0.8)      # And success probability 0.8
stats.binom.pmf(k=5,        # Probability of k = 5 successes
                n=10,       # With 10 flips
                p=0.5)      # And success probability 0.5

from scipy.stats import multinomial, binom
rv = multinomial(n=10,pvals=[1/3]*3)  # 10 is number of balls, 3 means categorized into three categories.
print(rv.rvs(4))  # print 4 possible outcomes.
rv.pmf([2,4,4])  # 0.05334552659655548 calculate the pobability of this [2,4,4]
multinomial.pmf([3, 4], n=7, p=[0.4, 0.6])  # 0.29030399999999973
binom.pmf(3, 7, 0.4)  # 0.29030400000000012  same as above
    # The functions pmf, logpmf, entropy, and cov support broadcasting
multinomial.pmf([[3, 4], [3, 5]], n=[7, 8], p=[.3, .7])  # array([0.2268945 , 0.25412184])
    # Compute the covariance matrix of the multinomial distribution
multinomial.cov([4, 5], [[.3, .7], [.4, .6]])
"""array([[[ 0.84, -0.84],
        [-0.84,  0.84]],
       [[ 1.2 , -1.2 ],
        [-1.2 ,  1.2 ]]])"""
# 2.6.3 Chi-square Distribution
# 2.6.3.1 Chi-Squared Goodness-Of-Fit Test
"""it tests whether the distribution of sample categorical data matches an expected distribution. For example, 
you could use a chi-squared goodness-of-fit test to check whether the race demographics of members at your church or 
school match that of the entire U.S. population or whether the computer browser preferences of your friends match 
those of Internet uses as a whole. """
import numpy as np
import pandas as pd
import scipy.stats as stats
    # create dataframes that only have one column with the sum of all these observations.
national = pd.DataFrame(["white"] * 100000 + ["hispanic"] * 60000 + \
                        ["black"] * 50000 + ["asian"] * 15000 + ["other"] * 35000)

minnesota = pd.DataFrame(["white"] * 600 + ["hispanic"] * 300 + \
                         ["black"] * 250 + ["asian"] * 75 + ["other"] * 150)

national_table = pd.crosstab(index=national[0], columns="count")  # crosstab() Computes a simple cross tabulation of two (or more) factors.
minnesota_table = pd.crosstab(index=minnesota[0], columns="count")

print("National")
print(national_table)
print(" ")
print("Minnesota")
print(minnesota_table)
    # calculate the chi-squared statistic for our data to illustrate:
observed = minnesota_table

national_ratios = national_table/len(national)  # Get population ratios for each categories

expected = national_ratios * len(minnesota)   # Get expected counts for each categories

chi_squared_stat = (((observed-expected)**2)/expected).sum()

print(chi_squared_stat)  # 18.194805
    # see if 18.194805 is in 95% confident interval
crit = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 4)   # Df = number of variable categories - 1

print("Critical value")
print(crit)  # 9.487729036781154

p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,  # Find the p-value
                             df=4)
print("P value")
print(p_value)  # 0.00113047
"""Since our chi-squared statistic exceeds the critical value, we'd reject the null hypothesis that the two 
distributions are the same. """
    # You can carry out a chi-squared goodness-of-fit test automatically using the scipy function scipy.stats.chisquare():
stats.chisquare(f_obs= observed,   # Array of observed counts
                f_exp= expected)   # Array of expected counts
"""Power_divergenceResult(statistic=array([18.19480519]), pvalue=array([0.00113047]))"""

# 2.6.3.2 Chi-Squared Test of Independence
"""The chi-squared test of independence tests whether two categorical variables are independent."""
    # Let's generate some fake voter polling data and perform a test of independence:
np.random.seed(10)
"""With the seed reset (every time), the same set of numbers will appear every time.

If the random seed is not reset, different numbers appear with every invocation
10 is just a number that when you use same number later, it gives you same random results"""
        # Sample data randomly at fixed probabilities
voter_race = np.random.choice(a= ["asian","black","hispanic","other","white"],
                              p = [0.05, 0.15 ,0.25, 0.05, 0.5],
                              size=1000)  # one row 1000 columns.

        # Sample data randomly at fixed probabilities
voter_party = np.random.choice(a= ["democrat","independent","republican"],
                              p = [0.4, 0.2, 0.4],
                              size=1000)

voters = pd.DataFrame({"race":voter_race,
                       "party":voter_party})  # 1000 rows 2 columns

voter_tab = pd.crosstab(voters.race, voters.party, margins = True)  # count based on each category

voter_tab.columns = ["democrat","independent","republican","row_totals"]

voter_tab.index = ["asian","black","hispanic","other","white","col_totals"]

observed = voter_tab.iloc[0:5,0:3]   # Get table without totals for later use
expected = np.outer(voter_tab["row_totals"][0:5],
                     voter_tab.loc["col_totals"][0:3]) / 1000

expected = pd.DataFrame(expected)

expected.columns = ["democrat","independent","republican"]
expected.index = ["asian","black","hispanic","other","white"]
chi_squared_stat = (((observed-expected)**2)/expected).sum().sum()
crit = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 8)   # *

print("Critical value")
print(crit)

p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,  # Find the p-value
                             df=8)
print("P value")
print(p_value)
stats.chi2_contingency(observed= observed)

# 2.6.4 Poisson and Exponential Distribution
    # Geometric Distribution
"""The geometric distribution is discrete and models the number of trials it takes to achieve a success in repeated 
experiments with a given probability of success. """
random.seed(12)
flips_till_heads = stats.geom.rvs(size=10000,  # Generate geometric data
                                  p=0.5)       # With success prob 0.5
        # Print table of counts
print( pd.crosstab(index="counts", columns= flips_till_heads))
        # Plot histogram
pd.DataFrame(flips_till_heads).hist(range=(-0.5,max(flips_till_heads)+0.5)
                                    , bins=max(flips_till_heads)+1)
stats.geom.cdf(k=5,   # Prob of success in first 5 flips
                           p=0.5)
stats.geom.pmf(k=2,   # Prob of needing exactly 2 flips to get first success
              p=0.5)
    # Expomential Distribution
"""The exponential distribution is a continuous analog of the geometric distribution and models the amount of time 
you have to wait before an event occurs given a certain occurrence rate. """
            # Get the probability of waiting more than 1 time unit before a success
prob_1 = stats.expon.cdf(x=1,
                         scale=1)  # Arrival rate
1 - prob_1  # Note: The average arrival time for the exponential distribution is equal to 1/arrival_rate
            # Let's plot this exponential distribution to get an idea of its shape
plt.fill_between(x=np.arange(0,1,0.01),
                 y1= stats.expon.pdf(np.arange(0,1,0.01)) ,
                 facecolor='blue',
                 alpha=0.35)
plt.fill_between(x=np.arange(1,7,0.01),
                 y1= stats.expon.pdf(np.arange(1,7,0.01)) ,
                 facecolor='red',
                 alpha=0.35)
plt.text(x=0.3, y=0.2, s= round(prob_1,3))
plt.text(x=1.5, y=0.08, s= round(1 - prob_1,3))
    # Poisson
"""The Poisson distribution models the probability of seeing a certain number of successes within a time interval, 
where the time it takes for the next success is modeled by an exponential distribution. """
random.seed(12)
arrival_rate_1 = stats.poisson.rvs(size=10000,  # Generate Poisson data
                                   mu=1 )       # Average arrival time 1
        # Print table of counts
print( pd.crosstab(index="counts", columns= arrival_rate_1))

        # Plot histogram
pd.DataFrame(arrival_rate_1).hist(range=(-0.5,max(arrival_rate_1)+0.5)
                                    , bins=max(arrival_rate_1)+1)
stats.poisson.cdf(k=5,     # Check the probability of 5 arrivals or less
                  mu=10)   # With arrival rate 10
stats.poisson.pmf(k=10,     # Check the prob f exactly 10 arrivals
                  mu=10)    # With arrival rate 10
# 2.6.5 Gamma Distribution
    #1 : Creating gamma continuous random variable
from scipy.stats import gamma
numargs = gamma.numargs
[a] = [0.7, ] * numargs
rv = gamma(a)
    #2 : generalized gamma random variates.
import numpy as np
quantile = np.arange(0.01, 1, 0.1)
        # Random Variates
R = gamma.rvs(a, scale=2, size=10)
print("Random Variates : \n", R)
        # PDF
R = gamma.pdf(a, quantile, loc=0, scale=1)
print("\nProbability Distribution : \n", R)
    #3 : Graphical Representation.
distribution = np.linspace(0, np.minimum(rv.dist.b, 3))
print("Distribution : \n", distribution)
plot = plt.plot(distribution, rv.pdf(distribution))
    #4 : Varying Positional Arguments
x = np.linspace(0, 5, 100)
        # Varying positional arguments
y1 = gamma.pdf(x, a, 1, 3)
y2 = gamma.pdf(x, a, 1, 4)
plt.plot(x, y1, "*", x, y2, "r--")
# 2.6.6 Beta Distribution
from scipy.stats import beta
numargs = beta.numargs
[a, b] = [0.6, ] * numargs
quantile = np.arange (0.01, 1, 0.1)
random.seed(11)
arrival_rate_1 = stats.beta.rvs(a, b, scale = 2,  size = 10  # Generate Poisson data
                                   )
        # Print table of counts
print( pd.crosstab(index="counts", columns= arrival_rate_1))

        # Plot histogram
pd.DataFrame(arrival_rate_1).hist(range=(-0.5,max(arrival_rate_1)+0.5)
                                    , bins=max(arrival_rate_1)+1)
stats.beta.cdf(k=5,     # Check the probability of 5 arrivals or less
                  mu=10)   # With arrival rate 10
stats.beta.pmf(k=10,     # Check the prob f exactly 10 arrivals
                  mu=10)    # With arrival rate 10

# 2.6.7 Dirichlet-Multinomial Distribution
from scipy.stats import dirichlet
d = dirichlet([ 1,1,1 ])
d.rvs(3) # get samples from distribution

# 2.6.8 Confidence intervals
    # Sampling Distributions and The Central Limit Theorem
np.random.seed(10)
population_ages1 = stats.poisson.rvs(loc=18, mu=35, size=150000)
population_ages2 = stats.poisson.rvs(loc=18, mu=10, size=100000)
population_ages = np.concatenate((population_ages1, population_ages2))
pd.DataFrame(population_ages).hist(bins=58,
                                  range=(17.5,75.5),
                                  figsize=(9,9))
print( stats.skew(population_ages) )  # The distribution has low skewness
np.random.seed(10)
point_estimates = []  # Make empty list to hold point estimates
for x in range(200):  # Generate 200 samples
    sample = np.random.choice(a=population_ages, size=500)
    point_estimates.append(sample.mean())
pd.DataFrame(point_estimates).plot(kind="density",  # Plot sample mean density
                                   figsize=(9, 9),
                                   xlim=(41, 45))  # the result is quite similar to normal distribution
    # Confidence Intervals
np.random.seed(10)
sample_size = 1000
sample = np.random.choice(a= population_ages, size = sample_size)
sample_mean = sample.mean()
z_critical = stats.norm.ppf(q = 0.975)  # Get the z-critical value*
print("z-critical value:")              # Check the z-critical value
print(z_critical)  # 1.959963984540054
pop_stdev = population_ages.std()  # Get the population standard deviation
margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)
print("Confidence interval:")
print(confidence_interval)  # (41.70306406882683, 43.34293593117317)
        # create several confidence intervals and plot them to get a better sense of what it means to "capture" the true mean
np.random.seed(12)
sample_size = 1000
intervals = []
sample_means = []
for sample in range(25):
    sample = np.random.choice(a=population_ages, size=sample_size)
    sample_mean = sample.mean()
    sample_means.append(sample_mean)
    z_critical = stats.norm.ppf(q=0.975)  # Get the z-critical value*
    pop_stdev = population_ages.std()  # Get the population standard deviation
    stats.norm.ppf(q=0.025)
    margin_of_error = z_critical * (pop_stdev / math.sqrt(sample_size))
    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)
    intervals.append(confidence_interval)
plt.figure(figsize=(9,9))
plt.errorbar(x=np.arange(0.1, 25, 1),
             y=sample_means,
             yerr=[(top-bot)/2 for top,bot in intervals],
             fmt='o')
plt.hlines(xmin=0, xmax=25,
           y=43.0023,
           linewidth=2.0,
           color="red")
        # If you don't know the standard deviation of the population, you have to use the standard deviation of your sample as a stand in when creating confidence intervals
np.random.seed(10)
sample_size = 25
sample = np.random.choice(a= population_ages, size = sample_size)
sample_mean = sample.mean()
t_critical = stats.t.ppf(q = 0.975, df=24)  # Get the t-critical value*
print("t-critical value:")                  # Check the t-critical value
print(t_critical)
sample_stdev = sample.std(ddof=1)    # Get the sample standard deviation
sigma = sample_stdev/math.sqrt(sample_size)  # Standard deviation estimate
margin_of_error = t_critical * sigma
confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)
print("Confidence interval:")
print(confidence_interval)
        # Instead of calculating a confidence interval for a mean point estimate by hand, you can calculate it using the Python function stats.t.interval()
stats.t.interval(alpha = 0.95,              # Confidence level
                 df= 24,                    # Degrees of freedom
                 loc = sample_mean,         # Sample mean
                 scale = sigma)             # Standard deviation estimate

# 2.7 Information Entropy

# 2.8 Moment Generating Functions
import sympy as S
from sympy import stats
p,t = S.symbols('p t',positive=True)
x=stats.Binomial('x',10,p)
mgf = stats.E(S.exp(t*x))
print(S.simplify(stats.E(x)))  # 10*p
print(S.simplify(S.diff(mgf,t).subs(t,0)))  # 10*p
print(S.simplify(stats.moment(x,1)))  # 10*p
print(S.simplify(stats.moment(x,2)))  # 10*p*(9*p + 1)
S.var('x:2',real=True)  # (x0, x1)
S.var('mu:2',real=True)  # (mu0, mu1)
S.var('sigma:2',positive=True)  # (sigma0, sigma1)
S.var('t',positive=True)  # t
x0=stats.Normal(x0,mu0,sigma0)
x1=stats.Normal(x1,mu1,sigma1)
# 2.9 Monte Carlo Sampling Methods

# 2.10 Sampling Importance Resampling

# 2.11 Useful Inequalities
# 2.11.1 Markov inequalities
"""Markov's inequality gives an upper bound for the probability that a non-negative function of a random variable is 
greater than or equal to some positive constant. """
# 2.11.2 Chebyshev inequalities
"""Chebyshev's inequality uses the variance to bound the probability that a random variable deviates far from the 
mean. """
import sympy
import sympy.stats as ss
t = sympy.symbols('t', real=True)
x = ss.ChiSquared('x',1)
r = ss.P((x-1) > t, x > 1) + ss.P(-(x-1) > t, x < 1)
w = (1-ss.cdf(x)(t+1)) + ss.cdf(x)(1-t)
fw = sympy.lambdify(t, w)
[fw(i) for i in [0,1,2,3,4,5]]
# 2.11.3 Hoeffding’s Inequality



# 3. Statistics
# 3.3 types of convergence
# 3.3.1 almost sure convergence
# 3.3.2 Convergence in Probability
# 3.3.3 Convergence in Distribution
# 3.3.4 Limit Theorems
# 3.4 Estimation Using Maximum Likelihood
# 3.4.1 Setting Up the Coin-Flipping Experiment
from scipy.stats import bernoulli
p_true = 1/2.0  # estimate this
fp = bernoulli(p_true)  # create bernoulli random variables
xs = fp.rvs(100)  # generate some samples
print(xs[:30])
    # Now, we can write out the likelihood function using Sympy.
import sympy
x, p, z = sympy.symbols('x p z', positive=True)  # positive=True eases Sympy’s internal simplification algorithms.
phi = p**x*(1-p)**(1-x)  # distribution function
L = np.prod([phi.subs(x,i) for i in xs])  # likelihood function of sample xs happens.
print(L)  # p**60*(1 - p)**40
logL = sympy.expand_log(sympy.log(L))  # 60*log(p) + 40*log(1 - p)
sol, = sympy.solve(sympy.diff(logL,p),p)  # diff: calculate differentiate of logL on p. solve: calculate p that makes first argument 0.
    # likelihood plot
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x = np.linspace(0,1,100)
ax.plot(x,list(map(sympy.lambdify(p,logL,'numpy'),x)),'k-',lw=3)
ax.plot(sol,logL.subs(p,sol),'o',color='gray',ms=15,label='Estimated')
ax.plot(p_true,logL.subs(p,p_true),'s',color='k',ms=15,label='Actual')
ax.set_xlabel('$p$',fontsize=18)
ax.set_ylabel('Likelihood',fontsize=18)
ax.set_title('Estimate not equal to true value',fontsize=18)
ax.legend(loc=0)

# 3.4.2 Delta Method
    # simulate variance of odds p/(1-p)
from scipy import stats
d = stats.bernoulli(0.1).rvs((10,5000)).mean(0)  # compute MLE estimates
d = d[np.logical_not(np.isclose(d,1))]  # avoid divide-by-zero: isclose identifies ones and logical_not removes ones.
odds = d/(1-d)  # computes odds ratio
print('odds ratio=',np.mean(odds),'var=',np.var(odds))

# 3.5 Hypothesis Testing and P-Values
# 3.5.1 Back to the Coin-Flipping Example
"""For example, let’s have a new test where we declare   H1  when   k=60  out of the 100 trials turns out to be 
heads. What is the   β  function in this case? """
import sympy as S
from sympy.stats import P, Binomial
theta = S.symbols('theta', real=True)
X = Binomial('x', 100, theta)
beta_function = P(X>60)
print(beta_function.subs(theta, 0.5))  # theta = 0.5 to beta_function  0.0176001001088524
print(beta_function.subs(theta, 0.7))  # theta = 0.7 to beta_function  0.979011423996075
# 3.5.2 Receiver Operating Characteristic
# 3.5.3 P-Values
# 3.5.4 Test Statistics
"""Suppose we have a receiver and we want to distinguish whether just noise (  H0 ) or signal pulse noise (  H1 ) is 
received. For the noise-only case, we have   x∼N(0,1)  and for the signal pulse noise case we have   x∼N(1,1) . """
    # Neyman–Pearson Test
"""The Neyman-Pearson Lemma is a way to find out if the hypothesis test you are using is the one with the greatest 
statistical power. """
from sympy import stats
s = stats.Normal('s',1,1)  # signal + noise
n = stats.Normal('n',0,1)  # noise
x = S.symbols('x',real=True)
L = stats.density(s)(x)/stats.density(n)(x)  # Neyman-Pearson Test function
g = S.symbols('g',positive=True)  # define gamma
v = S.integrate(stats.density(n)(x), (x, S.Rational(1,2) + S.log(g), S.oo))
print(S.nsolve(v-0.01,3.0))
    # Generalized Likelihood Ratio Test.
"""The null hypothesis is that all three coins have the same probability of heads,   H0:p=p1=p2=p3 ."""
    # Permutation Test
"""The Permutation Test is good way to test whether or not samples come from the same distribution. """
    # Wald Test (Z-test)
"""The Wald Test is an asymptotic test. Suppose we have   H0:θ=θ0  and otherwise   H1:θ≠θ0. a way to find out if 
explanatory variables in a model are significant. """
# 3.5.5 Testing Multiple Hypotheses
"""test the null hypothesis against a sequence of n competing hypotheses   Hk . We obtain p-values for each 
hypothesis so now we have multiple p-values to consider   {pk}.  To boil this sequence down to a single criterion, 
we can make the following argument. Given n independent hypotheses that are all untrue, the probability of getting at 
least one false alarm is the following: 
PFA=1−(1−p0)n"""
# 3.5.6 Fisher Exact Test
"""Fisher's exact test is a statistical test used to determine if there are nonrandom associations between two 
categorical variables """
# 3.5.7 T test
    # One-Sample T-Test¶
"""A one-sample t-test checks whether a sample mean differs from the population mean."""
population_ages1 = stats.poisson.rvs(loc=18, mu=35, size=150000)
population_ages2 = stats.poisson.rvs(loc=18, mu=10, size=100000)
population_ages = np.concatenate((population_ages1, population_ages2))
minnesota_ages1 = stats.poisson.rvs(loc=18, mu=30, size=30)
minnesota_ages2 = stats.poisson.rvs(loc=18, mu=10, size=20)
minnesota_ages = np.concatenate((minnesota_ages1, minnesota_ages2))
stats.ttest_1samp(a = minnesota_ages,               # Sample data
                 popmean = population_ages.mean())  # Pop mean
        # check the quantiles
stats.t.ppf(q=0.025,  # Quantile to check
            df=49)  # Degrees of freedom
stats.t.ppf(q=0.975,  # Quantile to check
            df=49)  # Degrees of freedom
        #  calculate the chances of seeing a result
stats.t.cdf(x= -2.5742,      # T-test statistic
               df= 49) * 2   # Multiply by two for two tailed test *
        #  construct a 95% confidence interval
sigma = minnesota_ages.std()/math.sqrt(50)  # Sample stdev/sample size
stats.t.interval(0.95,                        # Confidence level
                 df = 49,                     # Degrees of freedom
                 loc = minnesota_ages.mean(), # Sample mean
                 scale= sigma)                # Standard dev estimate
    # Two-Sample T-Test
"""A two-sample t-test investigates whether the means of two independent data samples differ from one another."""
wisconsin_ages1 = stats.poisson.rvs(loc=18, mu=33, size=30)
wisconsin_ages2 = stats.poisson.rvs(loc=18, mu=13, size=20)
wisconsin_ages = np.concatenate((wisconsin_ages1, wisconsin_ages2))
stats.ttest_ind(a= minnesota_ages,
                b= wisconsin_ages,
                equal_var=False)    # Assume samples have equal variance?
    # Paired T-Test
"""testing differences between samples of the same group at different points in time"""
np.random.seed(11)
before= stats.norm.rvs(scale=30, loc=250, size=100)
after = before + stats.norm.rvs(scale=5, loc=-1.25, size=100)
weight_df = pd.DataFrame({"weight_before":before,
                          "weight_after":after,
                          "weight_change":after-before})
weight_df.describe()             # Check a summary of the data
stats.ttest_rel(a = before,
                b = after)
# 3.5.8 Type I and Type II Error
plt.figure(figsize=(12,10))
plt.fill_between(x=np.arange(-4,-2,0.01),
                 y1= stats.norm.pdf(np.arange(-4,-2,0.01)) ,
                 facecolor='red',
                 alpha=0.35)
plt.fill_between(x=np.arange(-2,2,0.01),
                 y1= stats.norm.pdf(np.arange(-2,2,0.01)) ,
                 facecolor='grey',
                 alpha=0.35)
plt.fill_between(x=np.arange(2,4,0.01),
                 y1= stats.norm.pdf(np.arange(2,4,0.01)) ,
                 facecolor='red',
                 alpha=0.5)
plt.fill_between(x=np.arange(-4,-2,0.01),
                 y1= stats.norm.pdf(np.arange(-4,-2,0.01),loc=3, scale=2) ,
                 facecolor='grey',
                 alpha=0.35)
plt.fill_between(x=np.arange(-2,2,0.01),
                 y1= stats.norm.pdf(np.arange(-2,2,0.01),loc=3, scale=2) ,
                 facecolor='blue',
                 alpha=0.35)
plt.fill_between(x=np.arange(2,10,0.01),
                 y1= stats.norm.pdf(np.arange(2,10,0.01),loc=3, scale=2),
                 facecolor='grey',
                 alpha=0.35)
plt.text(x=-0.8, y=0.15, s= "Null Hypothesis")
plt.text(x=2.5, y=0.13, s= "Alternative")
plt.text(x=2.1, y=0.01, s= "Type 1 Error")
plt.text(x=-3.2, y=0.01, s= "Type 1 Error")
plt.text(x=0, y=0.02, s= "Type 2 Error")
    # calculate the type II error rate for the distributions
lower_quantile = stats.norm.ppf(0.025)  # Lower cutoff value
upper_quantile = stats.norm.ppf(0.975)  # Upper cutoff value
        # Area under alternative, to the left the lower cutoff value
low = stats.norm.cdf(lower_quantile,
                     loc=3,
                     scale=2)
        # Area under alternative, to the left the upper cutoff value
high = stats.norm.cdf(upper_quantile,
                      loc=3,
                      scale=2)
        # Area under the alternative, between the cutoffs (Type II error)
high-low
# 3.5.8 ANOVA
"""The t-test works well when dealing with two groups, but sometimes we want to compare more than two groups at the same
time. The analysis of variance or ANOVA is a statistical inference test that lets you compare multiple groups at the 
same time.
"""
    # One-Way ANOVA
"""The one-way ANOVA tests whether the mean of some numeric variable differs across the levels of one categorical 
variable. In the case of the ANOVA, you use the "f-distribution"."""
        # The scipy library has a function for carrying out one-way ANOVA tests called scipy.stats.f_oneway().
np.random.seed(12)
races = ["asian","black","hispanic","other","white"]
            # Generate random data
voter_race = np.random.choice(a= races,
                              p = [0.05, 0.15 ,0.25, 0.05, 0.5],
                              size=1000)
voter_age = stats.poisson.rvs(loc=18,
                              mu=30,
                              size=1000)
            # Group age data by race
voter_frame = pd.DataFrame({"race":voter_race,"age":voter_age})
groups = voter_frame.groupby("race").groups
            # Etract individual groups
asian = voter_age[groups["asian"]]
black = voter_age[groups["black"]]
hispanic = voter_age[groups["hispanic"]]
other = voter_age[groups["other"]]
white = voter_age[groups["white"]]
            # Perform the ANOVA
stats.f_oneway(asian, black, hispanic, other, white)  # F_onewayResult(statistic=1.7744689357329695, pvalue=0.13173183201930463)
"""indicating that there is no significant difference between the means of each group."""
        # Another way to carry out an ANOVA test is to use the statsmodels library
import statsmodels.api as sm
from statsmodels.formula.api import ols
model = ols('age ~ race',  # Model formula
            data=voter_frame).fit()
anova_result = sm.stats.anova_lm(model, typ=2)
print(anova_result)
        # To check which groups differ after getting a positive ANOVA result, you can perform a follow up test or "post-hoc test".
            # Get all race pairs
race_pairs = []
for race1 in range(4):
    for race2 in range(race1+1,5):
        race_pairs.append((races[race1], races[race2]))
            # Conduct t-test on each pair
for race1, race2 in race_pairs:
    print(race1, race2)
    print(stats.ttest_ind(voter_age[groups[race1]],
                          voter_age[groups[race2]]))
"""The p-values for each pairwise t-test suggest mean of white voters is likely different from the other groups, 
since the p-values for each t-test involving the white group is below 0.05. """
        # Another common post hoc-test is Tukey's test. You can carry out Tukey's test using the pairwise_tukeyhsd()
            # function in the statsmodels.stats.multicomp library:
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=voter_age,     # Data
                          groups=voter_race,   # Groups
                          alpha=0.05)          # Significance level
tukey.plot_simultaneous()    # Plot group confidence intervals
plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")
tukey.summary()              # See test summary

# 3.6 Confidence Intervals
# 3.7 Linear Regression
    # import libraries
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
    # load data
matplotlib.style.use('ggplot')
mtcars = pd.read_csv("../input/mtcars/mtcars.csv")
    # plot data
mtcars.plot(kind="scatter",
           x="wt",
           y="mpg",
           figsize=(9,9),
           color="black")
    # regression model
from sklearn import linear_model
        # Initialize model
regression_model = linear_model.LinearRegression()
        # Train the model using the mtcars data
regression_model.fit(X = pd.DataFrame(mtcars["wt"]),
                     y = mtcars["mpg"])
    # Check trained model y-intercept
print(regression_model.intercept_)
    # Check trained model coefficients
print(regression_model.coef_)
    # variance in the response variable is explained
regression_model.score(X = pd.DataFrame(mtcars["wt"]),
                       y = mtcars["mpg"])
    # residuals
train_prediction = regression_model.predict(X = pd.DataFrame(mtcars["wt"]))
            # Actual - prediction = residuals
residuals = mtcars["mpg"] - train_prediction
residuals.describe()
    # calculate R-squared
SSResiduals = (residuals**2).sum()
SSTotal = ((mtcars["mpg"] - mtcars["mpg"].mean())**2).sum()
        # R-squared
1 - (SSResiduals/SSTotal)
    # plot the line it fits on our scatterplot
mtcars.plot(kind="scatter",
           x="wt",
           y="mpg",
           figsize=(9,9),
           color="black",
           xlim = (0,7))
        # Plot regression line
plt.plot(mtcars["wt"],      # Explanitory variable
         train_prediction,  # Predicted values
         color="blue")
    # add an outlier--a super heavy fuel efficient car--and plot a new regression model:
mtcars_subset = mtcars[["mpg","wt"]]
super_car = pd.DataFrame({"mpg":50,"wt":10}, index=["super"])
new_cars = mtcars_subset.append(super_car)
        # Initialize model
regression_model = linear_model.LinearRegression()
        # Train the model using the new_cars data
regression_model.fit(X = pd.DataFrame(new_cars["wt"]),
                     y = new_cars["mpg"])
train_prediction2 = regression_model.predict(X = pd.DataFrame(new_cars["wt"]))
        # Plot the new model
new_cars.plot(kind="scatter",
           x="wt",
           y="mpg",
           figsize=(9,9),
           color="black", xlim=(1,11), ylim=(10,52))
        # Plot regression line
plt.plot(new_cars["wt"],     # Explanatory variable
         train_prediction2,  # Predicted values
         color="blue")
        # We can investigate the normality of residuals with a Q-Q (quantile-quantile) plot. Make a qqplot by passing
# the residuals to the stats.probplot() function in the scipy.stats library:
plt.figure(figsize=(9,9))
stats.probplot(residuals, dist="norm", plot=plt)
    # using stats package to generate nice table
slope, intercept, r_value, p_value, stderr = stats.linregress(pd.DataFrame(new_cars["wt"]), new_cars["mpg"])
import statsmodels.formula.api as smf
results = smf.ols('mpg ~ wt', data=new_cars).fit()
print(results.summary2())
    # Polynomial Regression
        # Initialize model
poly_model = linear_model.LinearRegression()
        # Make a DataFrame of predictor variables
predictors = pd.DataFrame([mtcars["wt"],           # Include weight
                           mtcars["wt"]**2]).T     # Include weight squared
        # Train the model using the new_cars data
poly_model.fit(X = predictors,
               y = mtcars["mpg"])
        # Check trained model y-intercept
print("Model intercept")
print(poly_model.intercept_)
        # Check trained model coefficients (scaling factor given to "wt")
print("Model Coefficients")
print(poly_model.coef_)
        # Check R-squared
print("Model Accuracy:")
print(poly_model.score(X = predictors,
                 y = mtcars["mpg"]))
        # Plot the curve from 1.5 to 5.5
poly_line_range = np.arange(1.5, 5.5, 0.1)
        # Get first and second order predictors from range
poly_predictors = pd.DataFrame([poly_line_range,
                               poly_line_range**2]).T
        # Get corresponding y values from the model
y_values = poly_model.predict(X = poly_predictors)
mtcars.plot(kind="scatter",
           x="wt",
           y="mpg",
           figsize=(9,9),
           color="black",
           xlim = (0,7))
        # Plot curve line
plt.plot(poly_line_range,   # X-axis range
         y_values,          # Predicted values
         color="blue")
    # Multiple Linear Regression
        # Initialize model
multi_reg_model = linear_model.LinearRegression()
        # Train the model using the mtcars data
multi_reg_model.fit(X = mtcars.loc[:,["wt","hp"]],
                     y = mtcars["mpg"])
        # Check trained model y-intercept
print(multi_reg_model.intercept_)
        # Check trained model coefficients (scaling factor given to "wt")
print(multi_reg_model.coef_)
        # Check R-squared
multi_reg_model.score(X = mtcars.loc[:,["wt","hp"]],
                      y = mtcars["mpg"])
# 3.8 Maximum A-Posteriori
"""In Bayesian statistics, a maximum a posteriori probability (MAP) estimate is an estimate of an unknown quantity, 
that equals the mode of the posterior distribution. The MAP can be used to obtain a point estimate of an unobserved 
quantity on the basis of empirical data """
# 3.9 Robust Statistics
"""More concretely, suppose you have a model that works great except for a few outliers. The temptation is to just 
ignore the outliers and proceed. Robust estimation methods provide a disciplined way to handle outliers without 
cherry-picking data that works for your favored model. """
# 3.10 Bootstrapping
import numpy as np
from scipy import stats
rv = stats.beta(3,2)  # beta distribution
xsample = rv.rvs(50)  # get 50 random observation from this beta distribution
yboot = np.random.choice(xsample,(100,50))
yboot_mn = yboot.mean()
np.std(yboot.mean(axis=1))
# 3.10.1 Parametric Bootstrap
# 3.11 Gauss–Markov

