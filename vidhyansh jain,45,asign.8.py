import math
def calculate_area(shape,*args):
    if shape=="circle":
        return math.pi*args[0]**2
    elif shape =="rectangle":
        return args[0]*args[1]
    elif shape =="triangle":
        return 0.5*args[0]*args[1]
    else:
        return "Invalid shape"
print("Area of Circle:",calculate_area("circle",5))
print("Area of Recangle:",calculate_area("rectangle",4,6))
print("Area of Triangle:",calculate_area("triangle",4,5))