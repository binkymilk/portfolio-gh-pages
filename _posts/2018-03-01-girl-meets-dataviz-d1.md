---
layout: post
title: "Girl Meets #DataViz: Day 1"
date: 2018-03-01
---

# Day 1: NumPy Basics

Since today is the first day, I'll go back to the basics of NumPy. I didn't have formal learning on Python and although it can have similar syntax with other languages, there were still alot of functions that I was not aware of.

Here's what I've learned so far:


```python
import numpy as np
```


```python
data1 = [6, 7.5, 8, 0, 1]
```

You can convert a Python array to a NumPy array by using the .array() function. You can get the dimension and the shape of the array as well using .ndim and .shape, respectively. To get the data type of an array, you can use .dtype.


```python
arr1 = np.array(data1)
```


```python
arr1
```




    array([ 6. ,  7.5,  8. ,  0. ,  1. ])




```python
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
```


```python
arr2 = np.array(data2)
```


```python
arr2
```




    array([[1, 2, 3, 4],
           [5, 6, 7, 8]])




```python
arr2.ndim
```




    2




```python
arr2.shape
```




    (2, 4)




```python
arr1.dtype
```




    dtype('float64')




```python
arr2.dtype
```




    dtype('int32')



This one's interesting because you can actually create an array full of zeroes or ones. Or you can create an array that isn't initialized.


```python
np.zeros(10)
```




    array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])




```python
np.zeros((3, 6))
```




    array([[ 0.,  0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.]])




```python
np.empty((2, 3, 2))
```




    array([[[ 0.,  0.],
            [ 0.,  0.],
            [ 0.,  0.]],
    
           [[ 0.,  0.],
            [ 0.,  0.],
            [ 0.,  0.]]])



Just like native Python, NumPy also has a function of creating an array of a range of numbers.


```python
np.arange(15)
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])



You can also explicitly state the data type of an array. The .astype(param) function copies the data type of the parameter to the calling array.


```python
arr1 = np.array([1, 2, 3], dtype=np.float64)
```


```python
np.array([1, 2, 3], dtype=np.int32)
```




    array([1, 2, 3])




```python
arr1.dtype
```




    dtype('float64')




```python
arr2.dtype
```




    dtype('int32')




```python
arr = np.array([1, 2, 3, 4, 5])
arr.dtype
```




    dtype('int32')




```python
float_arr = arr.astype(np.float64)
```


```python
float_arr.dtype
```




    dtype('float64')




```python
arr
```




    array([1, 2, 3, 4, 5])




```python
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr
```




    array([  3.7,  -1.2,  -2.6,   0.5,  12.9,  10.1])




```python
arr.astype(np.int32)
```




    array([ 3, -1, -2,  0, 12, 10])




```python
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)
```




    array([  1.25,  -9.6 ,  42.  ])




```python
int_array = np.arange(10)
```


```python
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
```


```python
int_array.astype(calibers.dtype)
```




    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])




```python
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr
```




    array([[ 1.,  2.,  3.],
           [ 4.,  5.,  6.]])



Operations on arrays can also be done easily using NumPy.


```python
arr * arr
```




    array([[  1.,   4.,   9.],
           [ 16.,  25.,  36.]])




```python
arr - arr
```




    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])



## Slicing and indexing

This is the part where I'm confused as hell (lmao).

There's a lot of ways to index and slice an array. You can access elements using 1 parameter, which returns one element. You can also access multiple elements using the [num1:num2]. The first number indicates the index of the first element to be accessed. The second number indicates how many elements (from the start of the array) are going to be accessed.


```python
arr = np.arange(10)
arr
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
arr[5]
```




    5




```python
arr[5:8]
```




    array([5, 6, 7])




```python
arr[5:8] = 12
arr
```




    array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])




```python
arr_slice = arr[5:8]
```


```python
arr_slice[1] = 12345
```


```python
arr
```




    array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,     9])




```python
arr_slice[:] = 64
```


```python
arr
```




    array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])




```python
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]
```




    array([7, 8, 9])




```python
arr2d[0][2]
```




    3




```python
arr2d[0,2]
```




    3




```python
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6]],
    
           [[ 7,  8,  9],
            [10, 11, 12]]])




```python
arr3d[0]
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
old_values = arr3d[0].copy()
```


```python
arr3d[0] = 42
arr3d
```




    array([[[42, 42, 42],
            [42, 42, 42]],
    
           [[ 7,  8,  9],
            [10, 11, 12]]])




```python
arr3d[0] = old_values
arr3d
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6]],
    
           [[ 7,  8,  9],
            [10, 11, 12]]])




```python
arr3d[1, 0]
```




    array([7, 8, 9])




```python
arr[1:6]
```




    array([ 1,  2,  3,  4, 64])




```python
arr2d
```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])




```python
arr2d[:2]
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
arr2d[:2, 1:]
```




    array([[2, 3],
           [5, 6]])




```python
arr2d[:, :1]
```




    array([[1],
           [4],
           [7]])



Okay, so things just got more interesting (and weirder) because you can now access elements on an array based on another array.


```python
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
names
```




    array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], 
          dtype='<U4')




```python
data
```




    array([[-0.3495857 ,  0.16252991,  0.14711447,  0.26868534],
           [ 0.38422365,  1.76713606,  1.06027233,  1.06529881],
           [-1.26115393,  0.85135587,  0.16902094, -0.48304254],
           [ 0.75302938,  0.2544839 , -0.14698368, -0.40647642],
           [-0.57687291,  0.4083022 , -1.07838816,  0.18733095],
           [-0.73245778, -0.30754811, -1.06954618,  0.36380007],
           [ 1.13925367, -0.09024229,  0.5732781 , -0.87999833]])




```python
names == 'Bob'
```




    array([ True, False, False,  True, False, False, False], dtype=bool)




```python
data[names == 'Bob']
```




    array([[-0.3495857 ,  0.16252991,  0.14711447,  0.26868534],
           [ 0.75302938,  0.2544839 , -0.14698368, -0.40647642]])




```python
data[names == 'Bob', 2:]
```




    array([[ 0.14711447,  0.26868534],
           [-0.14698368, -0.40647642]])




```python
names != 'Bob'
```




    array([False,  True,  True, False,  True,  True,  True], dtype=bool)




```python
data[~(names == 'Bob')]
```




    array([[ 0.38422365,  1.76713606,  1.06027233,  1.06529881],
           [-1.26115393,  0.85135587,  0.16902094, -0.48304254],
           [-0.57687291,  0.4083022 , -1.07838816,  0.18733095],
           [-0.73245778, -0.30754811, -1.06954618,  0.36380007],
           [ 1.13925367, -0.09024229,  0.5732781 , -0.87999833]])



NOTE: This is very important so don't forget!! The 'AND' operator is used as & and the 'OR' operator is used as |.


```python
mask = (names == 'Bob') | (names == 'Will')
mask
```




    array([ True, False,  True,  True,  True, False, False], dtype=bool)




```python
data[data < 0] = 0
```


```python
data
```




    array([[ 0.        ,  0.16252991,  0.14711447,  0.26868534],
           [ 0.38422365,  1.76713606,  1.06027233,  1.06529881],
           [ 0.        ,  0.85135587,  0.16902094,  0.        ],
           [ 0.75302938,  0.2544839 ,  0.        ,  0.        ],
           [ 0.        ,  0.4083022 ,  0.        ,  0.18733095],
           [ 0.        ,  0.        ,  0.        ,  0.36380007],
           [ 1.13925367,  0.        ,  0.5732781 ,  0.        ]])




```python
arr = np.empty((8, 4))
```


```python
for i in range(8):
    arr[i] = i
arr
```




    array([[ 0.,  0.,  0.,  0.],
           [ 1.,  1.,  1.,  1.],
           [ 2.,  2.,  2.,  2.],
           [ 3.,  3.,  3.,  3.],
           [ 4.,  4.,  4.,  4.],
           [ 5.,  5.,  5.,  5.],
           [ 6.,  6.,  6.,  6.],
           [ 7.,  7.,  7.,  7.]])




```python
arr[[4, 3, 0, 6]]
```




    array([[ 4.,  4.,  4.,  4.],
           [ 3.,  3.,  3.,  3.],
           [ 0.,  0.,  0.,  0.],
           [ 6.,  6.,  6.,  6.]])




```python
arr[[-3, -5, -7]]
```




    array([[ 5.,  5.,  5.,  5.],
           [ 3.,  3.,  3.,  3.],
           [ 1.,  1.,  1.,  1.]])



Reshaping is one of the helper functions to make it easier to create data. (You don't actually have to type in every dimension!)


```python
arr = np.arange(32).reshape((8, 4))
arr
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15],
           [16, 17, 18, 19],
           [20, 21, 22, 23],
           [24, 25, 26, 27],
           [28, 29, 30, 31]])



Now, this one's interesting. I got confused as to what happened next.


```python
arr[[1, 5, 7, 2] , [0, 3, 1, 2]]
```




    array([ 4, 23, 29, 10])



So, the first array indicates the row indices of the array being accessed. The second array indicates the column indices to be accessed. I can't believe this is possible (and easy, if you understand it). I wonder when these kind of things are used?


```python
arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]
```




    array([[ 4,  7,  5,  6],
           [20, 23, 21, 22],
           [28, 31, 29, 30],
           [ 8, 11,  9, 10]])




```python
arr = np.arange(15).reshape((3, 5))
arr
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])



One of the useful operations is transposition!


```python
arr.T
```




    array([[ 0,  5, 10],
           [ 1,  6, 11],
           [ 2,  7, 12],
           [ 3,  8, 13],
           [ 4,  9, 14]])




```python
arr = np.random.randn(6, 3)
np.dot(arr.T, arr)
```




    array([[ 2.31106866, -0.6529425 , -1.34886903],
           [-0.6529425 ,  1.40338322, -0.47591315],
           [-1.34886903, -0.47591315,  5.03525197]])




```python
arr = np.arange(16).reshape((2, 2, 4))
arr
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7]],
    
           [[ 8,  9, 10, 11],
            [12, 13, 14, 15]]])




```python
arr.transpose((1, 0, 2))
```




    array([[[ 0,  1,  2,  3],
            [ 8,  9, 10, 11]],
    
           [[ 4,  5,  6,  7],
            [12, 13, 14, 15]]])




```python
arr.swapaxes(1,2)
```




    array([[[ 0,  4],
            [ 1,  5],
            [ 2,  6],
            [ 3,  7]],
    
           [[ 8, 12],
            [ 9, 13],
            [10, 14],
            [11, 15]]])



So, that's the end of my day 1 learning for #dataviz. That was quite a lot, but still very basic. I'm looking forward for more learning.
