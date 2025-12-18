class Base():
    def __init__(self, x: int, y: int, z: int, t: int) -> None:
        self.__x = x # Creating private fields
        self.__y = y
    
        self._t = t # Creating protected fields

        self.z = z # Creating public fields
    
    def setX(self, x: int) -> None: # Setter
        self.__x = x

    def getY(self) -> int: # Getter
        return self.__y

    def _printHello(self) -> None: # Protected method
        print("Hello")

    def __printInfo(self) -> str: # Private method
        return f"x: {self.__x}, y: {self.__y}"

    def getInfo(self) -> None: # Public method
        print(self.__printInfo())


obj = Base(1, 2, 3, 4)
obj.setX(4)
print(obj.getY())
print(obj.z)
obj.getInfo() # Calling public method

obj._printHello() # Calling protected method (not recommended)
