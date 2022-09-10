# polynomial-division
Divide polynomials easily!

## Installation

From PyPI:

```zsh
$ pip install polynomial-division
```

## Command line

### Command

```zsh
$ divide 2,-1,7,4 2,1
```

### Parameters

* `dividend`: a list of coefficients. For example, for the polynomial \$2x^3 - x^2 + 7x + 4\$, this is `2,-1,7,4`
* `divisor`: a list of coefficients. For example, for the expression \$2x+1\$, this is `2,1`

### Output

```zsh
Result: 1.0x^2 + -1.0x^1 + 4.0
```

## Python

### Import module

```python
from polynomial_division import polynomial_divide as pd
```

### Call function

```python
print(pd((2,-1,7,4), (2,1)))
```

### Parameters

* `dividend`: a tuple of coefficients. For example, for the polynomial \$2x^3 - x^2 + 7x + 4\$, this is `(2,-1,7,4)`
* `divisor`: a tuple of coefficients. For example, for the expression \$2x+1\$, this is `(2,1)`

### Output

```python
(1.0, -1.0, 4.0)
```
