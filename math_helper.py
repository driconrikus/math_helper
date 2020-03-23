import math

def mathematics():
    user_selection = str(input('Which calculation do you want to make?: '))
    if user_selection == 'Hypotenuse' or user_selection == 'hypotenuse': #Calculates the length of the hypotenuse using Pythagorea's theorem.

        from math import sqrt
        print("Input lengths of shorter triangle sides: ")
        a = float(input('a: '))
        b = float(input('b: '))
        c = sqrt(a**2 + b**2)

        print('The length of the hypotenuse is: %.3f' %c)

    elif user_selection == 'Area' or user_selection == 'area': #Calculates the area with Pi * r^2
        r = float(input('Enter the radius of the circle: '))
        area = math.pi * r**2

        print('The area of the circle is: %.2f' %area)

    elif user_selection == 'Perimeter' or user_selection == 'perimeter': #Calculates the perimeter with the diameter
        d = float(input('Enter the diameter of the circle: '))
        perimeter = math.pi * d
    
        print('The perimeter of the circle is: %.2f' %perimeter)

    elif user_selection == 'Diameter' or user_selection == 'perimeter': #Calculates the diameter with perimeter
        p = float(input('Enter the perimeter of the circle: '))
        d = p / math.pi

        print('The diameter of the circle is %.2f' %d)
    
    elif user_selection == 'Sectorarea' or user_selection == 'sectorarea': #Calculates area of a sector
        r = float(input('Enter the radius of the circle: '))
        a = float(input('Enter the delta of the sector: '))
        sectorarea = a / 360 * math.pi * r**2

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
            print('Finished.')
            break
        else:
            print('Invalid option. Finishing...')
            break
    
loop_function()
