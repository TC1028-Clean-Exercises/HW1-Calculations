# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
        #Inputs
        ["5000", "0.05", "10", "12"],
        # Ouputs
        ["Enter initial principal balance: ",
         "Enter interest rate (decimal): ",
         "Enter number of periods: ",
         "Enter number of times interest is compounded in each period: ",
         "Total amount saved: 8235.0474884514"],
        # Message in case of failure
        ["The result should be over 8000."]
    ),
    # Test case 2
    (
        #Inputs
        ["100", "0.1", "20", "1"],
        # Ouputs
        ["Enter initial principal balance: ",
         "Enter interest rate (decimal): ",
         "Enter number of periods: ",
         "Enter number of times interest is compounded in each period: ",
         "Total amount saved: 672.7499949325611"],
        # Message in case of failure
        ["The result should be over 600."]
    ),
    # Test case 3
    (
        #Inputs
        ["24500", "0.02", "24", "2"],
        # Ouputs
        ["Enter initial principal balance: ",
         "Enter interest rate (decimal): ",
         "Enter number of periods: ",
         "Enter number of times interest is compounded in each period: ",
         "Total amount saved: 39499.5389032204"],
        # Message in case of failure
        ["The result should be nearly 40000."]
    ),
    # Test case 4
    (
        #Inputs
        ["4567890", "0.03", "5", "12"],
        # Ouputs
        ["Enter initial principal balance: ",
         "Enter interest rate (decimal): ",
         "Enter number of periods: ",
         "Enter number of times interest is compounded in each period: ",
         "Total amount saved: 5306137.680298504"],
        # Message in case of failure
        ["The result should be over 5300000."]
    ),
]
