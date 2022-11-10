
areas = [0]

def rectangle_area(x,y):
    a = x * y
    return a

def rectangle_area_enumerate(rectangle_count):
    count = 1
    while count <= rectangle_count:
        length = int(input("What is the length of the rectangle? "))
        width = int(input("What is the width of the rectangle? "))
        areas.append(rectangle_area(length, width))
        count += 1
    return areas

def rectangle_area_add(rectangle_count, *areas):
    count = 1
    area = 0
    while count <= rectangle_count:
        area += areas[count]
        count += 1
    return area

def main():
    rectangle_count = int(input("How many rectangles do you have? "))
    areas = rectangle_area_enumerate(rectangle_count)
    area = rectangle_area_add(rectangle_count, *areas)
    print(f"This is your final area: {area}")
    pass

main()