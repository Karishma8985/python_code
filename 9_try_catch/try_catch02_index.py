try:
    
    even_numbers = [2,4,6,8,12,14,16]
    print(even_numbers[16])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError as i:
    print("Index Out of Bound.",i)

# Output: Index Out of Bound