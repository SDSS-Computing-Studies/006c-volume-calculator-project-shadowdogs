#!python3
# Volume Calculator
# Feel free to rename your variables
import math


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Jhune Francis
    # Modified:
    print("""
    ==========Welcome To ShadowDogsUnleashed Calculator==========
    Cube
    Sphere
    Cone
    Cylinder
    Pyramid
    =============================================================
    """)


def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Jhune Francis
    # Modified:
    print("""
    ==========Instructions==========
    Choose a shape 
    Enter the value of the shape that you chose
    type "exit" to close the program
    ================================
    """)


def getShape():
    shape = input("Enter your shape: ")
    return shape


def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    # Author: David
    # Modified:
    if shape == "Cube" or "cube":
        # volume = sidelength**3
        paramList = ["Enter a side length: "]

    elif shape == "Sphere" or "sphere":
        # volume = (4 / 3) * math.pi * (radius**3)
        paramList = ["Enter radius: "]

    elif shape == "Cone" or "cone":
        # volume = math.pi * (radius**2) * (height / 3)
        paramList = ["Enter radius: ", "Enter height: "]

    elif shape == "Pyramid" or "pyramid":
        # volume = (length * width * height) / 3
        paramList = ["Enter base length: ",
                     "Enter base width: ", "Enter height: "]

    elif shape == "Cylinder" or "pyramid":
        # volume = math.pi * (radius**2) * height
        paramList = ["Enter radius: ", "Enter height: "]

    return paramList


def getInputs(paramList):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    # Author: Sam
    # Modified:
    measurements = []
    for i in paramList:
        measurements.append(input(i))

    return measurements


def calculate(shape, inputList):
    if shape == "Cube" or "cube":
        # volume = sidelength**3
        x = int(inputList[0])
        answer = x ** 3

    elif shape == "Sphere" or "sphere":
        # volume = (4 / 3) * math.pi * (radius**3)
        x = int(inputList[0])
        answer = (4 / 3) * math.pi * (x ** 3)

    elif shape == "Cone" or "cone":
        # volume = math.pi * (radius**2) * (height / 3)
        x = int(inputList[0])
        y = int(inputList[1])
        answer = math.pi * (x ** 2) * (y / 3)

    elif shape == "Pyramid" or "pyramid":
        # volume = (length * width * height) / 3)
        x = int(inputList[0])
        y = int(inputList[1])
        z = int(inputList[2])
        answer = (x * y * z) / 3

    elif shape == "Cylinder" or "cylinder":
        # volume = math.pi * (radius**2) * height
        x = int(inputList[0])
        y = int(inputList[1])
        answer = math.pi * (x ** 2) * y

    return answer


def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    # Author:
    # Modified:
    x = ""
    title()
    instructions()
    while x != "exit":
        nshape = getShape()
        nlist = getParams(nshape)
        ninputs = getInputs(nlist)
        answer = calculate(nshape, ninputs)
        print("The volume of the " + nshape + " is " + str(answer))

        x = input("Type 'exit' to stop program ")


main()
