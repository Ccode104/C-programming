#!/bin/python3

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

#Tail Recursion
#BigInt data type used by Python internally

def extraLongFactorials(n, res):
    # Write your code here
    if (n == 0) or (n == 1):
        print(res)
    else:
        extraLongFactorials(n-1, res * n)
       

if __name__ == '__main__':
    n = int(input().strip())
    res=1
    
    extraLongFactorials(n, 1)