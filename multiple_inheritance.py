class A():
    def __init__(self) -> None:
        print("init A")


class B(A):
    def __init__(self) -> None:
        print("init B")
        # A.__init__(self)
        # OR
        super().__init__() # Better

class C(A):
    def __init__(self) -> None:
        print("init C")

        # A.__init__(self)
        # OR
        super().__init__() # Better

class D(B, C):
    def __init__(self) -> None:
        print("init D")

        # B.__init__(self)
        # C.__init__(self)
        # OR
        super().__init__() # Better

d = D()
print(D.__mro__)
