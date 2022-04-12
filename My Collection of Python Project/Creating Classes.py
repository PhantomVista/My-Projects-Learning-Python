# classes are used to define new types (ie 'Booleans, Strings, Numbers, list, Dictionary)
# When creating a class, capitalize the first letter of variable. This is called "pascal naming convention"
# Example: class Jump, or class JumpStart


class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x * point1.y)
point1.draw()

point2 = Point()
point2.x = 1


# There's a better way to get x & y coordinates
# using the

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(10, 20)
print(point.x)


