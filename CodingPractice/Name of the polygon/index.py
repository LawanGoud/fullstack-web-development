sides = int(input())

if sides < 3:
    print("Not Polygon")
elif sides == 3:
    print("Triangle")
elif sides == 4:
    print("Quadrilateral")
elif sides == 5:
    print("Pentagon")
else:
    print("Big Polygon")