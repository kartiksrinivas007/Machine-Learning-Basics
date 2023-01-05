import datetime
import logging
import os
import args_kwargs

FORMAT = '%(name)s : %(asctime)s : %(levelname)s : %(module)s  == %(message)s'
logger = logging.getLogger(__name__) # convention to use the name as __name__ for the module logger
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('employee.log') 
logger.addHandler(file_handler)
formatter = logging.Formatter(FORMAT)
file_handler.setFormatter(formatter)
"""
you set a logger with its __name__ and its level , you add a filehandler to the logger, you add a Formatter and a level(if needed) to the file_handler and then you 
use the logger
"""
os.system('echo "" > employee.log') # empty the file 
#logging.basicConfig(filename = "employee.log", level = logging.INFO, format = FORMAT) # will not make a difference to the root logger defined in args_kwargs
class Employee:
    growth_rate = 4
    
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        logger.info(f"New employee created with name = {self.name}")

    def __str__(self):
        return f"Employee : {self.name} and pay {self.pay}"

    def apply_raise(self ):
        self.pay = self.pay * self.growth_rate

    @classmethod
    def set_rate(cls, rate):
        cls.growth_rate = rate

    """
    you can create alternative constructors using class methods, for different formatted inputs
    """
    @classmethod
    def from_string(cls, string):
        name, pay = string.split('-')
        return cls(name, pay) # calls the constructor

    @staticmethod
    def get_date():
        return datetime.datetime.now()

class Dev(Employee):
    growth_rate = 6.0

    def __init__(self, name , pay, prog_lang):
        #call the part that takes part of the first three arguments
        super().__init__(name, pay)#calls the parent constructor
        self.prog_lang = prog_lang # the rest


if __name__ == "__main__":
    e = Employee("Kartik", 30000)
    print(e)
    Employee.set_rate(20)
    e.apply_raise()
    print(e)
    print(Employee.get_date())
    d = Dev("Aayush", 40000, "C++")
    print(d.prog_lang)
    #help(d) #this is a fantastic description of the attributes that are carried by the class


    
