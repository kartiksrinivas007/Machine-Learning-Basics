import logging
import os

os.system("echo "" > args-kwargs.log")
FORMAT = '%(name)s : %(asctime)s : %(levelname)s : %(module)s : %(message)s'
logger = logging.getLogger(__name__) # convention to use the name as __name__ for the module logger
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('args-kwargs.log') 
logger.addHandler(file_handler)
formatter = logging.Formatter(FORMAT)
file_handler.setFormatter(formatter)

#logging.basicConfig(filename = 'args-kwargs.log' , level = logging.DEBUG, format = '%(asctime)s : %(levelname)s : %(module)s : %(message)s ')

def argskwargs(*args, **kwargs):
    for arg in args:
        print(arg)
        logger.debug(f"the argument is = {arg}")
    for key, value in kwargs.items():
        print(key, value)
    for key in kwargs.keys():
        print(key, kwargs[key])
        

#args is  a tuple while kwargs is a dict
#then the * and ** unpacks the tuple and dict
argskwargs(1,2,3,4,5,6,7,8,9,10, name = "John", age = 20)



a  = (1, 2, 3, 4, 5)
b = {"name": "John", "age": 20}

argskwargs(*a, **b)
