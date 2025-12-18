class Vector():
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def __add__(self, otherVector): # Overloading a = a + b
        return Vector(self.x + otherVector.x, self.y + otherVector.y) # returns Class object!

    def __iadd__(self, otherVector): # Overloading a += b
        self.x += otherVector.x
        self.y += otherVector.y 
        return self

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

vec1 = Vector(1, 2)
vec2 = Vector(2, 1)
vec1 = vec1 + vec2
vec1 += vec2

print(vec1.x, vec1.y)
