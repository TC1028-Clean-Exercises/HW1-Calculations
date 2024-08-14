![Tec de Monterrey](../../images/logotecmty.png)
# Even numbers range

Modify the file `src/exercise.py` so that the program performs as described below:

```python
def main():
  # Substitute this comment and the pass expression with your code
  pass

if __name__ == '__main__':
    main()
```

## Description

Write a function **count_evens** that takes as arguments the integer values a
and b and returns the count of even numbers from a to b, using a for loop.
Suppose a < b. If a and/or b are even, they must be included. 0 is considered
even.

#### Inputs
Two integer numbers, for the lower and upper limits of the number range to analyze.

#### Outputs
An integer number for the amount of even numbers between the two limits, inclusive.
That is, if any of the limits is even, it must also be counted.

#### IMPORTANT NOTE:
The output of your program must be exactly identical to the examples shown below:

When calling only the function:
```
count_evens(3, 12)
5


count_evens(7, 2)
0
```

When running the whole program:
```
Enter lower limit: 3
Enter upper limit: 12
Even numbers in the range: 5

Enter lower limit: 7
Enter lower limit: 2
Even numbers in the range: 0

Enter lower limit: 100
Enter lower limit: 250
Even numbers in the range: 76
```
