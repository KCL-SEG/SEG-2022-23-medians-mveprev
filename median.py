"""Median calculator."""

def median(list):
    temp = sorted(list)
    mid = len(temp) // 2
    return (temp[mid] + temp[-mid-1]) / 2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        print(f"The median of this list is {median(numbers)}")
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
