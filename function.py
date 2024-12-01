# Define the function
def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False

# Assign values to variables
a = 10
b = 6

# Call the function and store the result
result = greaterThan(a, b)

# Print the result
print("The statement", str(a), "is greater than", str(b), "is", str(result))
