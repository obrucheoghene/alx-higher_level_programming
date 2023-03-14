## 0x03. Python - Data Structures: Lists, Tuples

### List

### What you should know about List

A `list` in python is a list of comma-seperated values (items) between square brackets
Lists might contain items of different types, but usually the items all have the same type.

Here is an example

```py
numbers = [1, 4, 9, 16, 25]
```

Like `strings`, `list` can be indexed and sliced

```py
numbers[0]
```

All slice operations on a `list` return a new `list` which is a `shallow copy` of the orginal list

```py
new_numbers = numbers[:]
```

Lists support operations like concatenation:

```py
add_list = numbers + [3, 9, 9, 5, 6]
```

Unlike `strings` which are immutable, `list` are mutable type. Meaning it is possible to change its content

```py
numbers[0] = 40
```

You can add items to the end of a `list` using the `append()` method

```py
numbers.append(40)
```

Just as you assign a value to and index position, you can assign value(s) to a slice which can the size of the list or clear it entirely

```py
numbers[1:3] = [50,40,5,3]
```

Use the `len()` function to get the length of `lists`

```py
len(numbers)
```

It is possible to nest list, that is and a list to a list.

```py
alpha_number = [[['a', 'b', 'c'], [1, 2, 3]]]
```
