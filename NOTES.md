# Python Notes
.idea is for pycharm ide
To run code with python3, enter `python3 path/to/python-file.py`
# Brython library
Brython - lets you run python in the browser -> scrimba
Python code converted to JS

## Python Datatypes
- can use `type()` method to get the datatype of
  - `print(type('hello'))` --> `<class 'str'>`
string ("ten")
integers (whole number 10)
float (decimal point number 10.3)
boolean (True or False)

## Type casting
- String to Integer `int("1")` will be `1`
- Integer to String `str(1)` will be `"1"`
- Integer to Float `float(1)` will be `1.0`
- Float to Integer `int(4.3)` will be `4`
- Note: `int("3.4")` will _error out_.
  - Need to _first_ cast to float, _then_ to integer
  - `int(float("3.4"))` will be `3`

## Escaping
backslash \

```py
a = 'it\'s'

# switch to double quotes 
b = "it's"
```
## Naming Conventions
variable names: snakecase --> favorite_drink

# Arithmetic Operations
- Addition: a + b
- Subtraction: a - b
- Multiplication: a * b
- Division (float): a / b
- Division (floor): a // b
- Modulus: a % b
- Exponent: a ** b

## Functions
- functions are defined and use the word `def` before and end with a `:` after the parenthesis. The code block uses indentation to show what belongs with the function. 

```py
def my_new_function(param1, param2):
  print(f'Printing param1 {param1} and param2 {param2} using an fstring -- string literal')

my_new_function('hello1', 'hello2')
  
```
