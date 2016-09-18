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


side_1 = raw_input("Find out if three lengths can make a triangle. Enter first length.\n")

int(side_1)

side_2 = raw_input("Second length. \n")

int(side_2)

side_3 = raw_input("Third length. \n")

int(side_3)

is_triangle(side_1, side_2, side_3)
