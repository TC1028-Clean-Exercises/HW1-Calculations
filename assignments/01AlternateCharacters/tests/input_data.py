# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
        #Inputs
        ["0"],
        # Ouputs
        ["Enter number of characters: "],
        # Message in case of failure
        ["No characters should be printed."]
    ),
    # Test case 2
    (
        #Inputs
        ["2"],
        # Ouputs
        ["Enter number of characters: ", "#", "%"],
        # Message in case of failure
        ["Only two characters printed."]
    ),
    # Test case 3
    (
        #Inputs
        ["8"],
        # Ouputs
        ["Enter number of characters: ", "#", "%", "#", "%", "#", "%", "#", "%"],
        # Message in case of failure
        ["Eight characters printed."]
    ),
]
