from pprint import pprint

pprint(vars(misc))

#print out the variables in an object/module

#vectorize fn for matrix use
fn = scipy.vectorize(lambda x: 255-x)

def fprint(fn, val):
    print(fn.__name__, end=' ')
    print("of "+str(val)+": "+str(fn(val)))
