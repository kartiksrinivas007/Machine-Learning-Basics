def countdown(num):
    print('Start')
    while num > 0:
        yield num # returns the number and then stops the function
        num -=1

cd  = countdown(5) # it contains everything
value = next(cd) # it basically keeps track of the state of the function, they are liek static variables, can also use cuntcalls decorator instead for a static object
print(value) # the next is basically iterating over the iterator object that has been created
print("Second time = ",next(cd))
print("Third time = ", next(cd))

"""
Generators are useful in generating series type data usually.
They are also sueful in memory management
"""

def fibonacci(num):
    a, b = 0,1
    count = 0
    while count < num:
        yield a # returns a
        a, b = b, a + b
        count +=1
    return

container =  fibonacci(10)

for  i in container:
    print(i , end = " ")
