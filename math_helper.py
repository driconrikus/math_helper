import math

def mathematics():
    user_selection = str(input('Which calculation do you want to make?: '))
    if user_selection == 'Hypotenuse': #Calculates the length of the hypotenuse using Pythagorea's theorem.

        from math import sqrt
        print("Input lengths of shorter triangle sides: ")
        a = float(input('a: '))
        b = float(input('b: '))
        c = sqrt(a**2 + b**2)

        print('The length of the hypotenuse is: %.3f' %c)

    elif user_selection == 'Area': #Calculates the area with Pi * r^2
        Pi = 3.14
        r = float(input('Enter the radius of the circle: '))
        area = Pi * r * r

        print('The area of the circle is: %.2f' %area)

    elif user_selection == 'Perimeter': #Calculates the perimeter with the diameter
        Pi = 3.14
        d = float(input('Enter the diameter of the circle: '))
        perimeter = Pi * d
    
        print('The perimeter of the circle is: %.2f' %perimeter)

    elif user_selection == 'Diameter': #Calculates the diameter with perimeter
        Pi = 3.14
        p = float(input('Enter the perimeter of the circle: '))
        d = p / Pi

        print('The diameter of the circle is %.2f' %d)
    
    elif user_selection == 'Sectorarea': #Calculates area of a sector
        Pi = 3.14
        r = float(input('Enter the radius of the circle: '))
        a = float(input('Enter the delta of the sector: '))
        sectorarea = a / 360 * Pi * r**2

        print('The area of a sector is %.2f' %sectorarea)
    
    else:
        print('Please type in: Hypotenuse, Area, Perimeter, Sectorarea or Diameter')

def loop_function():
    i = 1
    while i < 10:
        mathematics()
        user_selection = str(input('Do you want to continue? (Y/N) '))
        if user_selection == 'Y' or user_selection == 'y':
            i +=1
        elif user_selection == 'N' or user_selection == 'n':
            break
        else:
            print('Invalid option. Finishing...')
            break
    
loop_function()
