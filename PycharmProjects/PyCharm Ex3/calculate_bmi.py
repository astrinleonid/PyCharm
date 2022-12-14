"""
Try to spot the bugs!

Author: Omer Rosenbaum
"""


def calculate_bmi(weight, height):
    """calculates a person's BMI given the persons weight and height"""
    return weight / (height ** 2)


if __name__ == '__main__':
    patients = [(75, 1.81), (82, 1.76), (95, 1.72)]

    for patient in patients:
        weight, height = patient #corrected: reference to the first element of the list instead of iteration
        bmi = calculate_bmi(weight, height) #corrected: wrong order of arguments
        print("Patient's BMI is: %f" % bmi)