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
    name: a way to reference the person
    appearance: a list of strings describing elements of a persons physical appearance.
    '''
    name: str
    appearance: List[str]

    def __init__(self, name: str, traits: List[str]) -> None:
        '''
        Initializes a new Person Object.
        '''
        self.name = name
        self.appearance = traits

    def __str__(self) -> str:
        '''
        A string representation for a Person Object.
        '''
        lst = ""
        for trait in self.appearance: 
            lst += "-" + trait + "\n"
        return "name: " + self.name + "\nappearance: \n" + lst

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
        print("station: %s" % new_station)
    
    def board_bus(self, passenger: Person) -> None: 
        '''
        Called when a passenger boards the bus.
        '''
        self.passengers.append(passenger)
        print("%s boarded the bus" % passenger.name)
    
    def exit_bus(self, passenger: Person) -> None: 
        '''
        Called when a passenger exits the bus.
        '''
        self.passengers.remove(passenger)
        print("%s exited the bus" % passenger.name)

class JostlingError: 
    '''
    Exception raised when jostling occurs.
    '''
    def __init__(self) -> None:
        pass 
    def __str__(self) -> str:
        return "JostlingError: A passenger is accusing another of stepping on his new kicks!"


if __name__ == "__main__":

    ### the setting ###
    initial_station = "Parc Monceau district platform"
    time = datetime.time(12, 17)
    print("time: " + str(time))
    print("---")

    ### the characters ### 
    person1 = Person("long-neck dude", ["with an annoyingly long neck", "with a stupid hat", "rude youngster"])
    person2 = Person("narrator", ["observant", "confused", "annoyed"])
    person3 = Person("another passenger", ["unkonwn traits"])
    person4 = Person("a friend", ["fashionable", "giving much needed advice on a button."])

    S = Autobus("S", initial_station, [person1, person3])
    print("the %s line is boarding" % S.line)
    print("---")
    S.board_bus(person2)
    print("---")
    for passenger in S.passengers: 
        print(passenger)
    
    print("---")

    next_station = "next staton"
    S.change_station(next_station)
    print("the %s line has stopped at %s" % (S.line, next_station))
    S.exit_bus(person3)
    jostling = JostlingError()
    print(jostling)
    
    print("---")

    last_station = "gare Saint-Lazare"
    time2 = datetime.time(14, 17)
    diff = time2.hour - time.hour
    print("time: " + str(time2) + ", %d hour(s) have passed" % diff)
    print("---")

    S.change_station(last_station)
    print("---")
    print(person1.name + " is with " + person4.name)
    print(person4)