import math
test_h = int(input("Hieght of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(h,w,c):
    numberOfcans = (h*w)/c
    print(f"No of cans required to paint the wall is : {math.ceil(numberOfcans)} cans")

paint_calc(h=test_h,w=test_w,c=coverage)