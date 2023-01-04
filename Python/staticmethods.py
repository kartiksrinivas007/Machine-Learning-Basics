import datetime
class Employee:
    growth_rate = 4
    
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
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
    pass

if __name__ == "__main__":
	e = Employee("Kartik", 30000)
	print(e)
	Employee.set_rate(20)
	e.apply_raise()
	print(e)
	print(Employee.get_date())
