from random import randint, choice


# Classes
class Laptop:
    '''a simple simulation of a laptop'''

    def __init__(self, manufacturer, model): # add a parameter named display
        '''the basic attributes'''
        self.manufacturer = manufacturer
        self.model = model
        self.power = 'Off'

    def power(self):
        '''check the power status of the laptop'''
        if self.power == 'Off':
            self.power = 'On'
            print(f"Turned the laptop {self.power}")
        else:
            self.power = 'Off'
            print(f"Turned the laptop {self.power}")


    def __init__(self, display,):
        '''the basic attributes'''
        self.display = display
        self.status = 'Off'

        def status(self):
            if self.status == 'Off':
                    self.status = 'On'
                    print(f"Turned the laptop {self.status}")
            else:
                    self.status = 'Off'
                    print(f"Turned the laptop {self.status}")

class Human:
    ''' a simple attempt to simulate human behaviour'''
    def __init__(self, name, age):
        '''initialize the attributes'''
        self.name = name
        self.age = age
    def talk(self):
        '''simulate talking'''
        print(f"{self.name.title()} is talking.")
    def ageOf(self):
        '''find the age of the person'''
        print(f"{self.name.title()} is {self.age} years old!")

class User:
    '''saves user info'''
    def __init__(self,fName,lName,username,password):
        self.fName = fName
        self.lName = lName
        self.username = username
        self.password = password
        self.account_number =randint(00000000000, 99999999999)
        self.team = choice(['red', 'blue','green'])
    def describe_user(self):
        '''describes the user'''
        print(f"User Profile: \n\tFirst Name:\t{self.fName.title()}\n\tLast Name:\t{self.lName.title()}\n\tUsername:\t{self.username}\n\tPassword:\t{self.password}\n\team:\t{self.team.title()}")
    def greet_user(self):
        '''send message'''
        print(f"Welcome {self.username}!")

class Car:
    def __init__(self, manufacture, model,enginetype):
        self.manufacture = manufacture
        self.model = model
        self.engine_type = enginetype

    def driver(self):
        if self.engine_type == 'ICE' or self.engine_type == 'Hybrid':
            print('Buying Fuel')
        elif self.engine_type == 'Electric':
            print('EV does not use fuel, charging instead')
        else:
            print('Error')