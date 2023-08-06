# InfiniteList

InfiniteList is a data type which can support any number
of elements. This can be done by using class attributes
storing a low number of elements.

# Installation

pip install InfiniteList

# Usage

To use this library, install it using the command 
shown in "Installation" section. Then, read the 
instructions below regarding how to use operations 
with InfiniteList.

## count()

InfiniteList class has 'count()' method accepting an element
as the parameter to get the number
of occurrences of an element in the list.

For example:
a: InfiniteList = InfiniteList([2, 3, 4, 3])
a.count(3) -> returns 2

## copy()

InfiniteList has 'copy()' method to return a copy of itself.

## index()

InfiniteList class has 'count()' method accepting an element
as the parameter to get the index of the first
occurrence of that element in the list.

For example:
a: InfiniteList = InfiniteList([2, 3, 4, 3])
a.index(3) -> returns 1

## reverse()

'reverse()' method in InfiniteList class reverses the 
order of elements in the list.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
c.reverse()
print(c) -> prints [6, 5, 3, 4]

## sort()

'sort()' method in InfiniteList class sorts all its
elements in ascending order.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
c.sort()
print(c) -> prints [3, 4, 5, 6]

## min()

'min()' method in InfiniteList returns the minimum element 
in the list.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
print(c.min()) -> prints 3

## max()

'max()' method in InfiniteList returns the maximum element 
in the list.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
print(c.max()) -> prints 6

## sum()

'sum()' method in InfiniteList returns the sum of
elements in the list.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
print(c.sum()) -> prints 18

## extend()

InfiniteList class has 'extend()' method which 
adds all elements from a list or iterable to the
InfiniteList. The elements are added to the end of the
InfiniteList.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
c.extend([7, 8])
print(c) -> prints [4, 3, 5, 6, 7, 8]

## insert()

'insert()' method in InfiniteList inserts an 
element at a particular index in the list.

For example:
c: InfiniteList = InfiniteList([1, 2, 3])
c.insert(1, 4)
print(c) -> prints [1, 4, 2, 3]

## append()

'append()' method in InfiniteList adds an element 
to the end of the list.

For example:
c: InfiniteList = InfiniteList([1, 2, 3])
c.append(5)
print(c) -> prints [1, 2, 3, 5]

## delete()

'delete()' method in InfiniteList removes an element 
at a particular index in the list.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
c.delete(1)
print(c) -> prints [4, 5, 6]

## remove()

'remove()' method in InfiniteList removes an elements
in the list if it exists.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
c.remove(5)
print(c) -> prints [4, 3, 6]

## clear()

'clear()' method in InfiniteList removes all elements 
from the list.

## length

To get the number of elements in an InfiniteList, 
you can write a code in the format 'len(infinite_list)'.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
print(len(c)) -> prints 4

## get an item

To get an item from an InfiniteList, you can write
a code in the format 'infinite_list[index]'.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
print(c[2]) -> prints 5

## edit an item in the list

To edit the value of an item in the list, you need to 
specify the index of the item you want to edit and the 
new value of the item.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
c[2] = 7
print(c) -> prints [4, 3, 7, 6]

## str

Using Python's built-in 'print' function followed with 
an InfiniteList will print out all the elements in the 
InfiniteList.

For example:
c: InfiniteList = InfiniteList([4, 3, 5, 6])
print(c) -> prints [4, 3, 5, 6]

# Running Tests

The script "BigNumber_versus_mpf.py" 
(https://github.com/GlobalCreativeCommunityFounder/InfiniteList/blob/main/InfiniteList/InfiniteList_versus_list.py) 
is used to run tests of the performance of InfiniteList library against 
Python's built-in list class.

## Sample Test Results

Examples of test results for InfiniteList versus list are in the 
following files:

1. https://github.com/GlobalCreativeCommunityFounder/InfiniteList/blob/main/InfiniteList/InfiniteList_versus_list_append.txt (testing for performance of adding items to lists)
2. https://github.com/GlobalCreativeCommunityFounder/InfiniteList/blob/main/InfiniteList/InfiniteList_versus_list_sort.txt (testing for performance of sorting items in lists)