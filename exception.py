#Exception #Raise #Asserions

"""
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value

A try statement can have multiple different except blocks to handle different exceptions.
Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them."""

a=int(input())
eve=a%2
assert eve==0,"eneter even number only"
b=int(input())
c=0
try:
    c=float(a)/b
except (ZeroDivisionError,ValueError,TypeError):
    print("Please input correct var as per thr type")
finally:
    print(c)


    