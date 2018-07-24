# Problem 527: Random Binary Search

The problem statement can be found [here](https://projecteuler.net/problem=527). 

The Python Jupyter Notebook `p527_py.ipynb` has a full writeup of the solution.

The python script `p527.py` computes the answer. [Cython](http://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html) is used to boost performance. First
do

```
    python setup.py build_ext --inplace
```

to [build the cython extension module](https://code.tutsplus.com/tutorials/speeding-python-with-cython--cms-29557) before running `p527.py`. If you need to install cython do

```
    pip install cython
```

