## 0x05. Python - Exceptions

## MY Learning Notes

In python there are two distinguishable kinds of errors and exceptions.

1. Syntax Errors: Which is also called parsing errors are errors that points the mistakes in using python langauage.

2. Exceptions: Exception is thrown when and error occur during an execution or where you what and exception to occur.

\*\* Handling Exceptions
To handle exception, use the `try` and `except` keywords. During excecution, The code within `try` block is executed and if and exception occurs that matches the exception name the code in the `except` block is executed otherwise it is skipped.

A try statement can have more than one except clause to specify handlers for different exceptions

Here is and example

```py
try:
    list = [0,2,4]
    print(list[4])
except IndexError:
    print("The index doesn't exist")
except:
    print("An unknown error occured")
```

The `try`...`except` statement has an optional `else` clause, which when present must follow all except clauses. It is useful for code that must be executed if the try clause does not raise exception.

There is also if a `final` clause that is use to execute code that will always will be executed wehter an exception occured or not.

```py
try:
    list = [0,2,4]
    print(list[2])
except IndexError:
    print("The index doesn't exist")
else:
    print("It worked")
finally:
    print("It doesn't matter what happened out there I am here")
```

## 8.4. Raising Exceptions

The `raise` statement allows the programmer to force a specified exception to occur. For example:
`raise NameError('HiThere')`

## Static Method

A static method allows you to use the method with initializeing the class object

To create a staticmethod use the `@staticmethod`

## Example

```py
Class Sum:
    @staticmethod
    def getSum(*arg):
        sum = 0
        for i in arg:
            sum += i
        return sum

def main():
    print("Sum: ", Sum.getSum(1,2,3,4,5))

main()
```

> > > Sum: 15

```py
Class Dog:
    num_of_dogs = 0

    def _init_(self, name="Unknown"):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():
    spot = Dog("spot")
    billy = Dog("Billy")
    spot.getNumOfDogs()
    billy.getNumOfDogs()
```

> > > There are currently 2 dogs
> > > There are currently 2 dogs
