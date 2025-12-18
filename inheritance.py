class Base():
    def __init__(self, x) -> None:
        print("Init")
        self._x = x
    
    def _sayHello(self) -> None:
        print(f"Hello from Base. X: {self._x}")
    
    def info(self) -> None: # Polymorphism
        print(f"X: {self._x}")

class Derived(Base): # Adding Parent`s classes
    def __init__(self, x, y) -> None:
        super().__init__(x) # Init Parent`s class 
        # OR
        # Base.__init__(self, x)
        self.__y = y

    def sayHello(self):
        self._x = 5

        super()._sayHello() # Calling parents method
        # OR
        # self._sayHello()

        print(f"Hello from Derived. Y: {self.__y}")

    def info(self) -> None: # Polymorphism
        print(f"X: {self._x}, Y: {self.__y}")

obj1 = Base(5)
obj = Derived(1, 2)
obj.sayHello()

