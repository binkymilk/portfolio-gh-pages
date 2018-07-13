
# Day 3: File Input and Output, Linear Algebra, RNG

Since these topics are relatively short, I'll be including them in my daily learning as well.

## Storing Arrays on Disk in Binary Format

The two most important functions are np.save and np.load.


```python
import numpy as np
```


```python
arr = np.arange(10)
```


```python
np.save('some_array', arr)
```


```python
np.load('some_array.npy')
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
np.savez('array_archive.npz', a=arr, b=arr)
```


```python
arch = np.load('array_archive.npz')
```


```python
arch['b']
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])



## Linear Algebra

Very useful and matrix operations.


```python
x = np.array([[1., 2., 3.], [4., 5., 6.]])
```


```python
y = np.array([[6., 23.], [-1, 7], [8, 9]])
```


```python
x
```




    array([[ 1.,  2.,  3.],
           [ 4.,  5.,  6.]])




```python
y
```




    array([[  6.,  23.],
           [ -1.,   7.],
           [  8.,   9.]])




```python
x.dot(y) #equivalently np.dot(x, y)
```




    array([[  28.,   64.],
           [  67.,  181.]])




```python
np.dot(x, np.ones(3))
```




    array([  6.,  15.])



np.linalg has a standard set of functions such as matrix decompositions, inverse, determinants, etc. 


```python
from numpy.linalg import inv, qr
```


```python
X = np.random.randn(5, 5)
```


```python
mat = X.T.dot(X)
```


```python
inv(mat)
```




    array([[ 24.69810068,   8.72435349,   8.45012323,  -5.50410329,
             -4.17346112],
           [  8.72435349,   4.50099024,   3.20687359,  -3.1220978 ,
             -1.81528028],
           [  8.45012323,   3.20687359,   3.35821413,  -2.27025213,
             -1.35459909],
           [ -5.50410329,  -3.1220978 ,  -2.27025213,   2.46201951,
              1.22278913],
           [ -4.17346112,  -1.81528028,  -1.35459909,   1.22278913,
              1.13579713]])




```python
mat.dot(inv(mat))
```




    array([[  1.00000000e+00,   1.40766178e-15,  -5.01753407e-16,
             -1.09963922e-15,   3.26898871e-16],
           [ -1.07183641e-15,   1.00000000e+00,   7.09681348e-16,
              2.83288000e-16,  -1.04360361e-15],
           [  3.18044612e-15,  -2.64379801e-15,   1.00000000e+00,
              4.78610079e-16,  -5.40300268e-16],
           [ -2.94788431e-15,  -6.59589593e-15,  -1.54638239e-15,
              1.00000000e+00,  -5.10377624e-16],
           [ -4.03739382e-15,  -9.17197141e-16,  -2.11980521e-15,
              1.37193816e-15,   1.00000000e+00]])




```python
q, r = qr(mat)
```


```python
r
```




    array([[-2.88705916,  5.81624204,  6.48415881,  8.76784203, -3.29448026],
           [ 0.        , -3.3870252 ,  0.57779696, -2.93115224, -2.00961391],
           [ 0.        ,  0.        , -0.83453199, -0.12142824, -1.47240532],
           [ 0.        ,  0.        ,  0.        , -0.88638395,  1.26356864],
           [ 0.        ,  0.        ,  0.        ,  0.        ,  0.19868035]])



Other commonly-used numpy.linalg functions are diag, trace, det, eig, inv, pinv, svd, solve, and lstsq.

## Random Number Generation


```python
samples = np.random.normal(size=(4,4))
samples
```




    array([[-0.65155537,  0.11415376,  1.09876926,  1.09211659],
           [ 0.07490524,  1.59488315,  3.15605069, -0.45545527],
           [ 0.33151533,  0.0442087 ,  0.12154232,  1.38948241],
           [ 0.16423881,  1.27282279, -0.31237781, -0.37142525]])



The difference with NumPy's random number generator and the built-int Python function is that the latter only produces one value at a time.


```python
from random import normalvariate
```


```python
N = 1000000
```


```python
%timeit samples = [normalvariate(0, 1) for _ in range(N)]
```

    1 loop, best of 3: 1.11 s per loop
    


```python
%timeit np.random.normal(size=N)
```

    10 loops, best of 3: 39.5 ms per loop
    

These other functions are available under numpy.random: seed, permutation, shuffle, rand, randint, randn, binomial, normal, beta, chisquare, gamma, and uniform.

## Example: Random Walks


```python
# Pure Python way to implement a single random walk in 1000 steps using the built-int random module
import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
```

### Simple Many Random Walks at Once


```python
nwalks = 5000
```


```python
nsteps = 1000
```


```python
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
```


```python
steps = np.where(draws > 0, 1, -1)
```


```python
walks = steps.cumsum(1)
```


```python
walks
```




    array([[  1,   0,  -1, ..., -70, -69, -68],
           [ -1,   0,   1, ...,  -4,  -5,  -6],
           [  1,   2,   1, ...,   6,   5,   6],
           ..., 
           [ -1,   0,   1, ...,  -2,  -3,  -4],
           [  1,   2,   1, ...,  18,  17,  18],
           [  1,   0,   1, ..., -16, -15, -16]], dtype=int32)




```python
walks.max()
```




    123




```python
walks.min()
```




    -119



That's it for learning the basics of NumPy. The next lesson would be Pandas, something really common for data analysis.
