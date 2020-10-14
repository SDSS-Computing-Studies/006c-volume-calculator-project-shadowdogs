#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Jhune Francis
    # Modified:
    print("""
    ----------Welcome To ShadowDogsUnleashed Calculator----------
    Cube
    Sphere
    Cone
    Cylinder
    Pyramid 
    -------------------------------------------------------------
    """)
    return None


def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("""
    ----------Instructions----------
    Choose a shape listed above
    Enter value of the shape that you chose

    """)

    return None


def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    # Author:
    # Modified:
    if shape == "Cube":
        # volume = sidelength**3
        paramList = ["Enter a side length: "]

    elif shape == "Sphere":
        # volume = (4 / 3) * math.pi * (radius**3)
        paramList = ["Enter radius: "]

    elif shape == "Cone":
        # volume = math.pi * (radius**2) * (height / 3)
        paramList = ["Enter radius: ", "Enter height: "]

    elif shape == "Pyramid":
        # volume = (length * width * height) / 3
        paramList = ["Enter base length: ",
                     "Enter base width: ", "Enter height: "]

    elif shape == "Cylinder":
        # volume = math.pi * (radius**2) * height
        paramList = ["Enter radius: ", "Enter height: "]

    return paramList


def getInputs(paramList):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    # Author:
    # Modified:
    measurements = []
    for i in paramList:
        measurements.append(input(i))

    return measurements


def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    # Author:
    # Modified:
    title()

getParams()
getInputs()
