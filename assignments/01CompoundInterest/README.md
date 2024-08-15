![Tec de Monterrey](../../images/logotecmty.png)
# Alternate characters

Modify the file `src/exercise.py` so that the program performs as described below:

```python
def main():
  # Substitute this comment and the pass expression with your code
  pass

if __name__ == '__main__':
    main()
```

## Description

Write a program that can compute compound interest for savings in an account.
Reference:
https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php

Use the formula:

$A = P \; \left( 1 + \dfrac{r}{n} \right)^{nt}$

Your program must ask the user for 4 values: principal investment amount ($P$),
interest rate ($r$), number of time periods ($t$), number of times within a period
when interest is compounded ($n$)
Your program must print the final amount ($A$) saved in the end

**Remember to add comments in your program. At the top of the file, you must have
a comment describing the program, and including your name**

#### Inputs
Your program must ask the user for 4 values:
- principal investment amount ($P$)
- interest rate ($r$)
- number of time periods ($t$)
- number of times within a period when interest is compounded ($n$)

#### Outputs
Your program must print the final amount ($A$) saved in the end

#### IMPORTANT NOTE:
The output of your program must be exactly identical to the examples shown below:

```
Enter initial principal balance: 5000
Enter interest rate (decimal): 0.05
Enter number of periods: 10
Enter number of times interest is compounded in each period: 12
Total amount saved: 8235.0474884514

Enter initial principal balance: 100
Enter interest rate (decimal): 0.1
Enter number of periods: 20
Enter number of times interest is compounded in each period: 1
Total amount saved: 672.7499949325611

Enter initial principal balance: 24500
Enter interest rate (decimal): 0.02
Enter number of periods: 24
Enter number of times interest is compounded in each period: 2
Total amount saved: 39499.5389032204
```
