class Base(): # Defining class
    def __init__(self, x, y) -> None: # Class Contructor
        self.x = x # Creating and setting fields
        self.y = y

    def printInfo(self) -> None: # Class method
        print(f"x: {self.x}, y: {self.y}") # Calling class fields using self


obj = Base(1, 2) # Creating class Base object
obj.x = 4 # Setting property of the object
print(obj.x) # Getting property of the object
obj.printInfo() # Calling method of the object
