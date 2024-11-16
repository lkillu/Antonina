class GeometricFigure:
    def area(self):
        raise NotImplementedError("Метод area() должен применяться для рассчета площади конкретной фигуры в соответствующем классе")
    
class Rectangle(GeometricFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14
        return pi* (self.radius ** 2)

class Rhombus(GeometricFigure):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2

if __name__ == "__main__":
    
    width = float(input("Ширина прямоугольника = "))
    height = float(input("Высота прямоугольника = "))
    rectangle = Rectangle(width, height)
    print("Площадь прямоугольника =", rectangle.area())
    
    radius = float(input("\nРадиус круга = "))
    circle = Circle(radius)
    print("Площадь круга =", circle.area())
    
    diagonal1 = float(input("\nДиагональ ромба 1 = "))
    diagonal2 = float(input("Диагональ ромба 2 = "))
    rhombus = Rhombus(diagonal1, diagonal2)
    print("Площадь ромба =", rhombus.area())
