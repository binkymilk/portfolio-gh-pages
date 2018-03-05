---
layout: post
title: "Girl Meets #DataViz"
date: 2018-03-03
---


# Day 2: Universal Functions

This is my second day of learning data analysis! Today's lesson is rather short, let's see what I can learn from it!

Many universal functions (ufuncs) are simple element-wise transformations. This means that given an array, it will perform the function in every element.


```python
import numpy as np
```


```python
arr = np.arange(10)
```


```python
np.sqrt(arr)
```




    array([ 0.        ,  1.        ,  1.41421356,  1.73205081,  2.        ,
            2.23606798,  2.44948974,  2.64575131,  2.82842712,  3.        ])




```python
np.exp(arr)
```




    array([  1.00000000e+00,   2.71828183e+00,   7.38905610e+00,
             2.00855369e+01,   5.45981500e+01,   1.48413159e+02,
             4.03428793e+02,   1.09663316e+03,   2.98095799e+03,
             8.10308393e+03])




```python
x = np.random.randn(8)
y = np.random.randn(8)
```


```python
x
```




    array([-1.40274301,  0.45403217, -0.4610062 , -1.44508332,  0.47436282,
           -1.45967956,  0.95617593,  0.44620104])




```python
y
```




    array([-1.60748525,  0.41349073, -1.50241078,  0.88536089, -1.51674347,
            0.03991642, -0.76024273, -1.36851858])



The function np.maximum compares every element of the two arrays and creates a new array consisting of the maximum values per index.


```python
np.maximum(x, y)
```




    array([-1.40274301,  0.45403217, -0.4610062 ,  0.88536089,  0.47436282,
            0.03991642,  0.95617593,  0.44620104])



Another function is the modf which returns the fractional part of a floating array.


```python
arr = np.random.randn(7) * 5
```


```python
np.modf(arr)
```




    (array([-0.61607718, -0.09127391,  0.02748275,  0.51365093,  0.32243359,
             0.05208878, -0.38210385]), array([-0., -0.,  5.,  3.,  3.,  5., -1.]))



There are a lot of other unary functions that can be used. Some examples are, abs, fabs, square, log, log10, sign, ceil, floor, rint, etc.

That's it for today!


```python

```
