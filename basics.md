# Python for Java Programmers

I'm just going to put some of the major syntactical differences
between the two languages. I will also include a section showing off the 
things you can do in python which would not be easy in Java. 

__Important__ You will need to download Python 3.4 if you don't already
 have it. 

Python broke backwards compatibility going from 2 to 3, so an older version
 will not work.

## Hello World

Way shorter in Python. Also note, Python is an interpreted language, so
you just need to say "python file.py" instead of the separate compile (javac),
and execute (java).

#### Python
```python
print ('Hello, World!')
```
#### Java
```java
public class Hello
{
    public static void main(String[] args)
    {
	System.out.println("Hello, World!");
    }
}
```

##Variables

When declaring a new variable in Python, you do not have to specify
a type. It will have a type underneath it all but you
generally don't have to worry about it, since the obvious
casts will be done for you.

Python is dynamically-typed so you don't really have to declare
a variable. If there is a statement such as ``` x = 5 ``` 
Python will look up the variable. If it can't find it, it assumes
you want to new declare a new one. This is good to keep in mind
when you are debugging.

#### Python
```python
x = 5 # its an int here
x /= 2 # now a float
```

#### Java
```java
double x = 5; //would need a cast if declared as an int
x /= 2;
```

## Looping/Indentation

Python uses indentation to mark off blocks of code. While normally indentation
is used for human readability, in Python the interpreter actually reads the
indentation and determines blocks of code based on this. Basically, an indent
functions as a curly brace in Java. Also, notice the colon marking
the end of the conditional expression.

#### Python
```python
for x in range(1, 6):
    print(x)

# Of course you can always do a while loop
# By the way, hash-tag is how you comment in Python

x = 1
while x<6:
    print(x)
    x += 1
```
#### Java
```java
for(int x=1; x<6; x++)
    System.out.println(x);

//Same while loop in Java:
int x=1;
while(x<6)
	System.out.println(x++);
```

This example also uses Python's range function. It creates a list
of numbers from the first argument (inclusive) to the second 
(exclusive). Python's for loop always uses a list or similar 
structure, an iterable to be exact, like Javas for(a : a[]) thingy


## Classes 

A basic class in Python is similar enough to one in Java. The
major differences are:
* Fields must always be referred to as self.field.
* All methods take self as their first argument.
* The constructor's name is __init__(self, arg0, arg1)
* __init__ and other special methods have 2 underscores on each side of their name.
* Because of dynamic typing, you don't have a section declaring
fields, unless you want that variable to have an initial value
before the constructor.

#### Python
```python
class Adder:
    """This is an optional documentation string."""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

adder = Adder(2, 6)
print(adder.add())

```

#### Java
```java
public class Adder
{
    public int a;
    public int b;

    public Adder(int a, int b)
    {
	this.a = a;
	this.b = b;
    }

    public int add()
    {
	return a+b;
    }
}
```

#### Java
```java
public class Test
{
    public static void main(String[] args)
    {
	Adder adder = new Adder(2, 6);
	System.out.println(adder.add());
    }
}
```

### Inheritance and Static Variables
* Just put the parent class in parenthesis.
* Multiple inheritance is allowed.
* You can declare a static variable simply by
leaving off the self. prefix and using it outside of any methods.
* Note that there's both a static and instance variable named count.
* __str__ is another special method in Python. It is equivalent to the 
toString in Java.

```python
class Pet:

    count = 0  # static

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Pet.count += 1 
        self.count = Pet.count

    def __str__(self):
        return "%s is a %s, and is the %d pet created" % (self.name, self.species, self.count)

class Dog(Pet):
    def __init__(self, name):
        Pet.__init__(self, name, "dog")

fido = Dog("Fido")
ed = Pet("Ed", "horse")

print(fido)
print(ed)
```
```java
public class Pet
{
    static int count = 0;

    public String name;
    public String species;
    public int id;

    public Pet(String name, String species)
    {
	this.name = name;
	this.species = species;
	id = count += 1;
    }

    public String toString()
    {
	return name + " is a " + species + ", and is the " +
	    id + " pet created";
    }
}
```
```java
public class Dog extends Pet
{
    public Dog(String name)
    {
	super(name, "dog");
    }
}
```
```java
public class Test
{
    public static void main(String[] args)
    {
	Dog fido = new Dog("Fido");
	Pet ed = new Pet("Ed", "horse");
	System.out.println(fido);	
	System.out.println(ed);	
    }
}
```




### Import
###Chained comparisons

Checck if argument # is between yadda and dadda

```python
import sys
pgm_name = sys.argv[0]
p = int(sys.argv[1])
```

Tuples - multiple return values

### Functions as variables, lambdas

```python
def forEach(lzt, fn):
    new_lzt = [] # empty list
    for item in lzt:
        new_lzt.append(fn(item))
    return new_lzt

def increment(x):
    return x+1

print(forEach(range(5), increment))
print(forEach(range(5), lambda x: x**2))
```