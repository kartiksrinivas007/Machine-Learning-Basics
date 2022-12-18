# Decorators are just functions using the outputs of another function, the rapper inside can return the function object that you want
import functools
def repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
    

class Countcalls:
    
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs): # callable objects , remember that a function is also an object in python
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@Countcalls # only a single function object is created apparently
@repeat # it counts the number of times repeat is called not the original function
def print_name():
    print("Hello")
    return 5


print_name()
print_name()
print_name()