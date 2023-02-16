x = int(input("Enter total values: "))
y = int(input("Enter values to choose from: "))
def factorial(num):
    z = 1
    for i in range(1, num + 1):
        z = z * i
    return z
combinations = factorial(x)/(factorial(y) * factorial(x-y))
permutations = factorial(x)/factorial(x-y)

print("total combinations (order doesn't matter) are: " + str(combinations))
print("total permutations (order does matter) are: " + str(permutations))
