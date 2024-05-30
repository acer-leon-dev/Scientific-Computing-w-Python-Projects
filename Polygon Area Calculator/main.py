# Create a rectangle
class Rectangle:
    # Set width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    # Gets the width of the line from one corner to the opposite corner
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    # Returns a literal representation of the shape in asterisks 
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return '\n'.join('*' * self.width for _ in range(self.height)) + '\n'

    # Return the amount of times a given shape can fit into the rectangle
    def get_amount_inside(self, shape):
        width_fits = 0
        height_fits = 0
        while True:
            if shape.width * (width_fits+1) <= self.width:
                width_fits += 1
            else:
                break
        while True:
            if shape.height * (height_fits+1) <= self.height:
                height_fits += 1
            else:
                break
        
        return width_fits * height_fits

# Create a square
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __str__(self):
        return f"Square(side={self.width})"

    # Change the length of the sides
    def set_side(self, side_length):
        self.width, self.height = side_length, side_length
    # The same as {set_side}
    def set_width(self, side_length):
        self.width, self.height = side_length, side_length
    # The same as {set_side}
    def set_height(self, side_length):
        self.width, self.height = side_length, side_length

# Testing
if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
