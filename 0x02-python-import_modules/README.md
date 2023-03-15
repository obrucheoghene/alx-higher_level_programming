## 0x02. Python - import & modules

### Definition of Modules

In Python, a module is a file containing Python definitions and statements. A module can define functions, classes, and variables. It can also include runnable code.

Modules are used to organize and manage code in a structured way, making it easier to maintain and reuse. You can import modules in other Python scripts to use their functions and classes, which saves time and effort in writing code from scratch.

1. Within a module, the module’s name (as a string) is available as the value of the global variable **name**.

For example a python file `cal.py` with the following content

```py
def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)
```

There are variant to import modules in python
Here are some examples

```py
import cal

cal.add(3, 5)
cal.sub(6, 3)

```

```py
from cal import add, sub
add(3, 5)
sub(6, 3)
```

Use as

```py
import cal as calculate

calculate.add(3, 5)
calculate.sub(6, 3)

```

```py
from cal import add as sum, sub as rem
sum(3, 5)
rem(6, 3)
```

**Note**
_For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter – or, if it’s just one module you want to test interactively, use importlib.reload(), e.g. import importlib; importlib.reload(modulename)._

### Executing modules as scripts

When you run a python script

```sh
python cal.py <arguments>
```

the code in the module will be executed, just as if you imported it, but with the **name** set to "**main**". That means that by adding this code at the end of your module:
That is when you import a python module, the global variable name **name** == name of the file without the `py` extension
that is **name** == "cal" but if you run the script **name** == "**main**"

lets update our `cal.py` script

```py
def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

if __name__ == "__main__":
    import sys
    add(int(sys.argv[1]), int(sys.argv[2]))
```

Running the `cal.py` will execute the script

```sh
python cal.py 20 50
```

Result: `70`

But if `cal.py` is imported, the code will not be executed

```sh
import cal.py
```

No result.

_This is often used either to provide a convenient user interface to a module, or for testing purposes (running the module as a script executes a test suite)._

### The Module Search Path

When a module named spam is imported, the interpreter first searches for a built-in module with that name. These module names are listed in `sys.builtin_module_names`. If not found, it then searches for a file named spam.py in a list of directories given by the variable `sys.path`. `sys.path` is initialized from these locations:

- The directory containing the input script (or the current directory when no file is specified).

- `PYTHONPATH` (a list of directory names, with the same syntax as the shell variable `PATH`).

- The installation-dependent default (by convention including a site-packages directory, handled by the site module).

The variable `sys.path` is a list of strings that determines the interpreter’s search path for modules. It is initialized to a default path taken from the environment variable PYTHONPATH, or from a built-in default if PYTHONPATH is not set. You can modify it using standard list operations:

### “Compiled” Python files

To speed up loading modules, Python caches the compiled version of each module in the **pycache** directory under the name module.version.pyc, where the version encodes the format of the compiled file; it generally contains the Python version number. For example, in CPython release 3.3 the compiled version of spam.py would be cached as **pycache**/spam.cpython-33.pyc. This naming convention allows compiled modules from different releases and different versions of Python to coexist.

A program doesn’t run any faster when it is read from a `.pyc` file than when it is read from a `.py` file; the only thing that’s faster about .pyc files is the speed with which they are loaded.

### The dir() Function

The built-in function `dir()` is used to find out which names a module defines. It returns a sorted list of strings:

_Without arguments, dir() lists the names you have defined currently_
