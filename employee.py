"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from abc import abstractmethod


class Employee:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class Salaried(Employee):
    def __init__(self, name, salary = None):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.salary}."
    # Billie works on a monthly salary of 4000.  Their total pay is 4000.
class Sal_Commission(Salaried):
    def __init__(self, name, salary = None, contracts = None, contract_rate = None):
        super().__init__(name, salary)
        self.contracts = contracts
        self.contract_rate = contract_rate
    def get_pay(self):
        return self.salary + (self.contracts * self.contract_rate)
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.contract_rate}/contract.  Their total pay is {self.get_pay()}."

class Sal_Bonus(Salaried):
    def __init__(self, name, salary = None, bonus = None):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_pay(self):
        return self.salary + self.bonus
    
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}."


class Hourly(Employee):
    def __init__(self, name, hour_rate = None, hours = None):
        super().__init__(name)
        self.hour_rate = hour_rate
        self.hours = hours

    def get_pay(self):
        return self.hour_rate * self.hours

    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.hour_rate}/hour.  Their total pay is {self.get_pay()}.'

class Hr_Bonus(Hourly):
    def __init__(self, name, hour_rate = None, hours = None, bonus = None):
        super().__init__(name, hour_rate, hours)
        self.bonus = bonus

    def get_pay(self):
        return (self.hour_rate * self.hours) + self.bonus
    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.hour_rate}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}.'


class Hr_Commission(Hourly):
    def __init__(self, name, hour_rate = None, hours = None, contracts = None, contract_rate = None):
        super().__init__(name, hour_rate, hours)
        self.contracts = contracts
        self.contract_rate = contract_rate
        self.commission = contracts * contract_rate

    def get_pay(self):
        return (self.hour_rate * self.hours) + self.commission

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.hour_rate}/hour and receives a commission for {self.contracts} contract(s) at {self.contract_rate}/contract.  Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salaried('Billie', salary = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly('Charlie', hour_rate = 25, hours = 100)
print(str(charlie))
# print(charlie.get_pay())
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Sal_Commission('Renee', salary = 3000, contract_rate=200, contracts=4)
print(str(renee))
# print(renee.get_pay())
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hr_Commission('Jan', hours = 150, hour_rate = 25, contracts = 3, contract_rate= 220)
print(str(jan))
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Sal_Bonus('Robbie', salary = 2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hr_Bonus('Ariel', hour_rate=30, hours = 120, bonus = 600)

