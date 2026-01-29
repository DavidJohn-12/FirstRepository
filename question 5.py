import math
def circle_area_coverage(radius_of_circle1, radius_of_circle2):
    if radius_of_circle1 and radius_of_circle2 > 0: #if valid, calculate each area
        area_of_circle1=math.pi*(radius_of_circle1**2)
        area_of_circle2=math.pi*(radius_of_circle2**2)

        if area_of_circle1 > area_of_circle2: #checks for larger one
            percentage_of_circle1_covered_by_circle_2= (area_of_circle2/area_of_circle1)*100 #calculates percentage
            return percentage_of_circle1_covered_by_circle_2

        if area_of_circle1 < area_of_circle2: #checks for larger one
            percentage_of_circle2_covered_by_circle_1=(area_of_circle1/area_of_circle2)*100 #calculates percentage
            return percentage_of_circle2_covered_by_circle_1

    else:
        return "One or both radii is an invalid value" #invalid statement

print(circle_area_coverage(7,13))