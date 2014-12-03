# Python for Java Programmers

I'm just going to put some of the major syntactical differences
between the two languages. I will also include a section showing off the 
things you can do in python which would not be easy in Java. 

** Important ** You will need to download Python 3.4 if you don't already
 have it. 

Python broke backwards compatibility going from 2 to 3, so an older version
 will not work.

## Hello World

Way shorter in Python. Also note, Python is an interpreted language, so
you just need to say "python file.py" instead of the seperate compile (javac),
and execute (java).

The Python code is first, and the equivalent Java code follows. This will be 
the pattern for each example.

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

## Looping/Indentation

Python uses indentation to mark off blocks of code. While normally indentaion
is used for human readability, in Python the interpretter actually reads the
indentation and determines blocks of code based on this. Basically, an indent
functions as a curly brace in Java.

#### Python
```python
for x in range(1, 6):
    print(x)

# Of course you can always do a while loop
# By the way, hashtag is how you comment in Python

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


#### Python
```python

```

#### Java
```java

```