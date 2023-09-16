class Rectangle:
    # Construct a rectangle object 
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

def main():
    # Create a rectangle with user-defined width and height
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    r1 = Rectangle(width, height)
    
    print("The width of the rectangle is", r1.width)
    print("The height of the rectangle is", r1.height)
    print("The area of the rectangle is", r1.getArea())
    print("The perimeter of the rectangle is", r1.getPerimeter())

main()