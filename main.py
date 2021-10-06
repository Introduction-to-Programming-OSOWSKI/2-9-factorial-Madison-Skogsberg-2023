#WRITE YOUR CODE IN THIS FILE
#define function
#add parameter
def factorial(x):
    y = 1
    for i in range (1, x + 1):
        y = i * y
    return y
#run functions
print(factorial(10))