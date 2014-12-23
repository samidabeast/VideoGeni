# Python for Java Programmers

I'm just going to put some of the major syntactical differences
between the two languages. Most examples will have equivalent code for 
Python and Java, but some Java examples are left off because
they are not nearly as easy to do in that language.

__Important__ You will need to download Python 3.4 if you don't already
 have it. 

__Also note__ Python is an interpreted language, so
you just need to say "python file.py" instead of the separate compile (javac),
and execute (java).

[Hello World](#Hello World)
[Variables](#Variables)
[Looping/Indentation](#Looping/Indentation)
[Classes ](#Classes )
[Inheritance and Static Variables](#Inheritance and Static Variables)
[Import](#Import)
[Chained comparisons](#Chained comparisons)
[Program Arguments](#Program Arguments)
[Tuples](#Tuples)
[Functions as variables](#Functions as variables)
[Lambdas](#Lambdas)


## Hello World <a name="Hello World"></a>
Way shorter in Python.

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

## Variables <a name="Variables"></a>

When declaring a new variable in Python, you do not have to specify
a type. It will have a type behind the scenes, but this type can change, so you
rarely have to cast variables, as it is done for you.

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

## Looping/Indentation <a name="Looping/Indentation"></a>

 While normally indentation is solely used for human readability,
 in Python the interpreter actually reads the
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
structure, an iterable to be exact, like Javas ``` for(i : array[]) ```loop.


## Classes  <a name="Classes "></a>

A basic class in Python is similar enough to one in Java. The
major differences are:
* Fields must always be referred to as self.field.
* All methods take self as their first argument.
* The constructor's name is __init__(self, arg0, arg1)
* __init__ and other special methods have 2 underscores on each side of their name.
* You don't have to have a section declaring
fields, unless you want that variable to have an initial value
__before__ the constructor.

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

## Inheritance and Static Variables <a name="Inheritance and Static Variables"></a>
* Just put the parent class in parenthesis.
* Multiple inheritance is allowed.
* You can declare a static variable simply by
leaving off the self. prefix and using it outside of any methods.
* Note that there's both a static and instance variable named count.
* __str__ is another special method in Python. It is equivalent to the 
toString in Java.

#### Python
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

class Dog(Pet):  # Dog inherits from Pet
    def __init__(self, name):
        Pet.__init__(self, name, "dog")

fido = Dog("Fido")
ed = Pet("Ed", "horse")

print(fido)
print(ed)
```
#### Java
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
#### Java
```java
public class Dog extends Pet
{
    public Dog(String name)
    {
	super(name, "dog");
    }
}
```
#### Java
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

## Import <a name="Import"></a>
## Chained comparisons <a name="Chained comparisons"></a>
## Program Arguments <a name="Program Arguments"></a>

#### Python
```python
import sys

if 1 < len(sys.argv) < 4:
    pass
else:
    print("ERROR: Invalid number of arguments.")
```
#### Java
```java
public class Test
{
    public static void main(String[] args)
    {

	if (args.length > 0 && args.length < 3)
	    ;
	else
	    System.out.println("ERROR: Invalid number of arguments.");
    }
}
```

## Tuples <a name="Tuples"></a>
A tuple is like a list, but you cannot modify its contents once created. It
is just to package some things together so you can move them around easier.
Tuples let you return multiple values from a function easily. You can also
unpack a tuple and give its contents to a function as parameters.

#### Python
```python
def funk():
    return(2,3)

def add(a,b):
    return a+b

x = funk() # x is a tuple

print(add(*x)) # prints 5
print(add(x[0],x[1])) # prints 5
```

## Functions as variables <a name="Functions as variables"></a>
## Lambdas <a name="Lambdas"></a>

Functions are just another type of variable in Python. This means that you
can pass them to other functions as arguments, and that you can also return
them. A lambda is an anonymous function, one without name. If you are
simply using the function as a parameter, using a lambda is easier than
defining a function the normal way.
#### Python
```python
def forEach(lzt, fn): 
#calls fn on each element in lzt, builds a new list of results
    new_lzt = [] # empty list
    for item in lzt:
        new_lzt.append(fn(item))
    return new_lzt

def increment(x):
    return x+1

print(forEach(range(5), increment)) # [1, 2, 3, 4, 5]
print(forEach(range(5), lambda x: x**2)) # [0, 1, 4, 9, 16]
```