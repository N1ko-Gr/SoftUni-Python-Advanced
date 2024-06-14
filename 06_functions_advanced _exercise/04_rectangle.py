def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return f"Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2*(length+width)

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"



print(rectangle(2, 10))
print(rectangle('2', 10))
