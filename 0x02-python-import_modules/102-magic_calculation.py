def magic_calculation_102(a, b):
    add = __import__('magic_calculation_102', fromlist=['add']).add
    sub = __import__('magic_calculation_102', fromlist=['sub']).sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

# Test the function
result = magic_calculation_102(3, 5)
print(result)
