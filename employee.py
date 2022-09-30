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

class Sal_Commission(Salaried):
    def __init__(self, name, salary = None, contracts = None, contract_rate = None):
        super().__init__(name, salary)

    def get_pay(self):
        return self.salary + (self.contracts * self.contract_rate)
class Sal_Bonus(Salaried):
    def __init__(self, name, salary = None, bonus = None):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_pay(self):
        return self.salary + self.bonus

class Hourly(Employee):
    def __init__(self, name, hour_rate = None, hours = None):
        super().__init__(name)
        self._hour_rate = hour_rate
        self._hours = hours

    def get_pay(self):
        return self._hour_rate * self._hours

class Hr_Bonus(Hourly):
    def __init__(self, name, hour_rate = None, hours = None, bonus = None):
        super().__init__(name, hour_rate, hours)
        self.bonus = bonus

    def get_pay(self):
        return (self._hour_rate * self._hours) + self.bonus

class Hr_Commission(Hourly):
    def __init__(self, name, hour_rate = None, hours = None, contracts = None, contract_rate = None):
        super().__init__(name, hour_rate, hours)
        self.bonus = contracts * contract_rate

    def get_pay(self):
        return (self._hour_rate * self._hours) + self.bonus

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salaried('Billie', salary = 4000)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly('Charlie', hour_rate = 25, hours = 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Sal_Commission('Renee', salary = 3000, contract_rate=200, contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hr_Commission('Jan', hours = 150, hour_rate = 25, contracts = 3, contract_rate= 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Sal_Bonus('Robbie', salary = 2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hr_Bonus('Ariel', hour_rate=30, hours = 120, bonus = 600)
