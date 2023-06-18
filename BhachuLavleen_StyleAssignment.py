'''
Lavleen Bhachu
WRI310 - Style Assignment 
June 19, 2023
=============================
Use this github link to view the code and the output of the program: 
=============================
Running Instructions (with the Python built-in IDE): 
- open the file (it will open automatically with the built-in IDE).
- press F5 to run the module.
- the output will show in another window.
- there is no need for the end-user to input anything; just run the module and enjoy :)
=============================

Python Print Statements.
'''

import datetime
from typing import List

###  A class in python is a block of code that defines types of data.

class Person:
    '''
    A person. 

    === Attributes === 
    appearance: a list of strings describing elements of a persons physical appearance.
    '''
    appearance: List[str]

    def __init__(self, traits: List[str]) -> None:
        '''
        Initializes a new Person Object.
        '''
        self.appearance = traits

    def __str__(self) -> str:
        '''
        A string representation for a Person Object.
        '''
        pass

class Autobus: 
    '''
    An object representing a French Bus. 

    === Attributes ===
    line: the route the bus will take. 
    station: the current station the bus is waiting at. 
    passengers: a list of Person objects currently aboard the bus. 
    '''
    line: str
    station: str
    passengers: List[Person]

    def __init__(self, line: str, station: str, passengers: List[Person]) -> None:
        '''
        Initializes a new Bus Object.
        '''
        self.line = line
        self.station = station
        self.passengers = passengers

    def change_station(self, new_station: str) -> None:
        '''
        Changes the current station for the bus.
        '''
        self.station = new_station
    
    def board_bus(self, passenger: Person) -> None: 
        '''
        Called when a passenger boards the bus.
        '''
        pass
    
    def exit_bus(self, passenger: Person) -> None: 
        '''
        Called when a passenger exits the bus.
        '''
        pass

class JostlingError(Exception): 
    '''
    Exception raised when jostling occurs.
    '''

    def __str__(self) -> str:
        return super().__str__()



""" today = datetime.time(12, 00)
print("the time is %d", (today))

S_bus = {"seat1": "", "seat2": "another man", "seat3": "", "pole1" : "long neck man"}
report = "S bus contains: \n"
for passenger in S_bus: 
    report += S_bus[passenger]
    report += "\n"
print(report)

S_bus["seat1"] = "narrator"
report = "S bus contains: \n"
for passenger in S_bus: 
    report += S_bus[passenger]
    report += "\n"
print(report)

S_bus["seat2"] = ""
for passenger in S_bus: 
    report += S_bus[passenger]
    report += "\n"
try:
    print(x)
except: 
    print("JoustingException: Long neck man is accusing another passenger of jousting him.")
print(report)

print("==================================================")
print("==================================================")
print("S_") """