# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["4", "8"],
        ["Enter lower limit: ", "Enter lower limit: ", "Even numbers in the range: 3"],
        "The result should be 3: (4, 6 and 8 are the even numbers) \n"
    ),
    (
        ["3", "12"],
        ["Enter lower limit: ", "Enter lower limit: ", "Even numbers in the range: 5"],
        "The result should be 5: (4, 6, 8, 10 and 12 are the even numbers) \n"
    ),
    (
        ["7", "2"],
        ["Enter lower limit: ", "Enter lower limit: ", "Even numbers in the range: 0"],
        "There is no range that can go from 7 to 2 with incrementing numbers\n"
    ),
    (
        ["0", "7"],
        ["Enter lower limit: ", "Enter lower limit: ", "Even numbers in the range: 4"],
        "The result should be 3: (0, 2, 4 and 6 are the even numbers) \n"
    )
]
