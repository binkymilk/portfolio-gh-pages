
# Day 3: Data Processing Using Arrays

For today's 'Girl Meets #DataViz' entry, I'll be learning data processing using arrays. Now, I know this is a very important step in wrangling and analyzing data. I hope the past concepts in arrays and maybe the same syntax will show up as well.


```python
import numpy as np
```


```python
points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
```


```python
xs, ys = np.meshgrid(points, points)
```


```python
ys
```




    array([[-5.  , -5.  , -5.  , ..., -5.  , -5.  , -5.  ],
           [-4.99, -4.99, -4.99, ..., -4.99, -4.99, -4.99],
           [-4.98, -4.98, -4.98, ..., -4.98, -4.98, -4.98],
           ..., 
           [ 4.97,  4.97,  4.97, ...,  4.97,  4.97,  4.97],
           [ 4.98,  4.98,  4.98, ...,  4.98,  4.98,  4.98],
           [ 4.99,  4.99,  4.99, ...,  4.99,  4.99,  4.99]])




```python
import matplotlib.pyplot as plt
```


```python
z = np.sqrt(xs ** 2 + ys ** 2)
z
```




    array([[ 7.07106781,  7.06400028,  7.05693985, ...,  7.04988652,
             7.05693985,  7.06400028],
           [ 7.06400028,  7.05692568,  7.04985815, ...,  7.04279774,
             7.04985815,  7.05692568],
           [ 7.05693985,  7.04985815,  7.04278354, ...,  7.03571603,
             7.04278354,  7.04985815],
           ..., 
           [ 7.04988652,  7.04279774,  7.03571603, ...,  7.0286414 ,
             7.03571603,  7.04279774],
           [ 7.05693985,  7.04985815,  7.04278354, ...,  7.03571603,
             7.04278354,  7.04985815],
           [ 7.06400028,  7.05692568,  7.04985815, ...,  7.04279774,
             7.04985815,  7.05692568]])




```python
plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()
```




    <matplotlib.colorbar.Colorbar at 0x1930b38ff60>




```python
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
```




    <matplotlib.text.Text at 0x1930ab47ac8>




```python
plt.show()
```


![png](Day3_files/Day3_10_0.png)


## Expressing Conditional Logic as Array Operations

Another function is the numpy.where which is another counterpart for the 'x if condition else y' expression.


```python
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
```


```python
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
```


```python
cond = np.array([True, False, True, True, False])
```

Now, we want to take out values from xarr if the corresponding element in cond is True and get values from yarr if False.


```python
result = [(x if c else y)
          for x, y, c in zip(xarr, yarr, cond)]
```


```python
result
```




    [1.1000000000000001, 2.2000000000000002, 1.3, 1.3999999999999999, 2.5]




```python
result = np.where(cond, xarr, yarr)
result
```




    array([ 1.1,  2.2,  1.3,  1.4,  2.5])




```python
arr = np.random.randn(4, 4)
arr
```




    array([[-0.41398097, -1.06186291, -0.12717428, -0.55227707],
           [ 0.09025902, -0.52136327,  0.44686089,  1.83608475],
           [ 2.22659232,  1.05829726, -0.37598718, -0.34948822],
           [ 0.15390363, -1.36662903,  0.43586674, -0.18852091]])




```python
np.where(arr > 0, 2, -2)
```




    array([[-2, -2, -2, -2],
           [ 2, -2,  2,  2],
           [ 2,  2, -2, -2],
           [ 2, -2,  2, -2]])




```python
np.where(arr > 0, 2, arr) # set only positive values to 2
```




    array([[-0.41398097, -1.06186291, -0.12717428, -0.55227707],
           [ 2.        , -0.52136327,  2.        ,  2.        ],
           [ 2.        ,  2.        , -0.37598718, -0.34948822],
           [ 2.        , -1.36662903,  2.        , -0.18852091]])



## Mathematical and Statistical Methods

These mathematical functions are commonly used in aggregations and to compute statistics.


```python
arr = np.random.randn(5, 4) # normally-distributed data
```


```python
arr.mean()
```




    0.097761700649068667




```python
np.mean(arr)
```




    0.097761700649068667




```python
arr.sum()
```




    1.9552340129813732




```python
arr.mean(axis=1)
```




    array([-0.2125116 , -0.04842038, -0.23089352,  0.48288069,  0.49775331])




```python
arr.sum(0)
```




    array([ 0.85783315, -2.22579029,  4.20083787, -0.87764672])




```python
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
```


```python
arr.cumsum(0)
```




    array([[ 0,  1,  2],
           [ 3,  5,  7],
           [ 9, 12, 15]], dtype=int32)




```python
arr.cumprod(1)
```




    array([[  0,   0,   0],
           [  3,  12,  60],
           [  6,  42, 336]], dtype=int32)



There are other functions for this such as std, var, min, max, argmin, and argmax.

## Methods for Boolean Arrays


```python
arr = np.random.randn(100)
```


```python
(arr > 0).sum() # Number of positive values
```




    51




```python
bools = np.array([False, False, True, False])
```


```python
bools.any() # Checks whether one or more values in an array is True
```




    True




```python
bools.all() # Checks whether every value is True
```




    False



## Sorting


```python
arr = np.random.randn(8)
```


```python
arr
```




    array([ 0.98233339, -0.8337867 ,  1.64382401, -1.07890647,  0.70105196,
            2.50638798,  0.51067766, -0.98978948])




```python
arr.sort()
```


```python
arr
```




    array([-1.07890647, -0.98978948, -0.8337867 ,  0.51067766,  0.70105196,
            0.98233339,  1.64382401,  2.50638798])




```python
arr = np.random.randn(5, 3)
```


```python
arr
```




    array([[-0.80731548,  0.52131162, -0.94010644],
           [ 0.08874958,  0.46704757,  0.80205328],
           [ 0.81714004, -0.17706826,  0.58001287],
           [-1.722179  ,  1.53712588, -1.33403036],
           [ 0.59708898, -0.68939265, -0.58872216]])




```python
arr.sort(1)
```


```python
arr
```




    array([[-0.94010644, -0.80731548,  0.52131162],
           [ 0.08874958,  0.46704757,  0.80205328],
           [-0.17706826,  0.58001287,  0.81714004],
           [-1.722179  , -1.33403036,  1.53712588],
           [-0.68939265, -0.58872216,  0.59708898]])




```python
large_arr = np.random.randn(1000)
```


```python
large_arr.sort()
```


```python
large_arr[int(0.05 * len(large_arr))] # 5% quantile
```




    -1.6097976179740394




```python
np.sort(arr)
```




    array([[-0.94010644, -0.80731548,  0.52131162],
           [ 0.08874958,  0.46704757,  0.80205328],
           [-0.17706826,  0.58001287,  0.81714004],
           [-1.722179  , -1.33403036,  1.53712588],
           [-0.68939265, -0.58872216,  0.59708898]])



## Unique and Other Set Logic

The next methods are some basic set operations for one-dimensional arrays.


```python
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
```

The method np.unique() returns the sorted unique values in an array


```python
np.unique(names)
```




    array(['Bob', 'Joe', 'Will'], 
          dtype='<U4')




```python
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
```


```python
np.unique(ints)
```




    array([1, 2, 3, 4])




```python
sorted(set(names))
```




    ['Bob', 'Joe', 'Will']



Another method is the np.in1d which tests membership of the values in one array in another.


```python
values = np.array([6, 0, 0, 3, 2, 5, 6])
```


```python
np.in1d(values, [2, 3, 6])
```




    array([ True, False, False,  True,  True, False,  True], dtype=bool)



Other methods include: intersect1d(x, y), union1d(x, y), in1d(x, y), setdiff1d(x, y), setxor1d(x, y)

That's it for today!


```python

```
