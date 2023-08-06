# mcalc
> ###### A simple not very precise calculator :exclamation::exclamation::exclamation:
Able to perform basic operations like:
* Add
* Subtract
* Multiply
* Divide
* Take ***n*** root

### Getting started:
#### Instalation:
To install the package run **`pip install mcalc`**
#### Usage examples
```
>>> from mcalc.calc import Calculator
>>> Calculator(0)
0.0
>>> Calculator(1)
1.0
>>> cal1 = Calculator(10)
>>> cal1.add(5)
15.0
>>> cal1.subtract(10)
5.0
>>> cal1.multiply(-5)
-25.0
>>> cal1.divide(-5)
5.0
>>> cal1.n_root(3)
1.7099759466766968
>>> cal1.reset(9)
9.0
>>> cal1.n_root(2)
3.0
>>> cal1.n_root(0.2)
243.0
```

#### Usage caveats
* You get basic [python floating point precision](https://docs.python.org/3/tutorial/floatingpoint.html)
* `n_root` method doesn't support taking roots of negative numbers, because this package doesn't support complex numbers (simple is in the name :sweat_smile:)

#### License
This code is protected under the MIT license



