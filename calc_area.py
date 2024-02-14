### Step 1

def calc_area_square(side_length):
    return  side_length ** 2

# input_number = 2
# output_number = calc_area_square(input_number)

# print(f'calc_area_square = {calc_area_square(2)}')




# Step 2

import math
#input_numbers = [0, 1, 4, 100]

def calc_area_circle(radius):
    if not isinstance(radius, (float,int)): # checking input type
        raise TypeError(f'radius is {radius} but should be a number')
    if radius < 0:
        raise ValueError(f'radius is {radius} but must be positive')
    return math.pi * radius ** 2

# for i in input_numbers:
#     print(calc_area_circle(i))

# conditionals within the functio       

def calc_area_rectangle(side1,side2):
    if side1 == side2:
        return side1**2
    else:
        return side1 * side2
    