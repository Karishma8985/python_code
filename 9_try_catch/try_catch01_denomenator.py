# simple try except....
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print(ZeroDivisionError)

# Output: Error: Denominator cannot be 0. 