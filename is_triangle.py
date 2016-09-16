# define if statement

def is_triangle(x, y, z):
    if (x + y < z):
        print("No")
    elif (x + z < y):
        print("No")
    elif (z + y < x):
        print("No")
    else:
        print("Yes")


is_triangle(5, 2, 4)
