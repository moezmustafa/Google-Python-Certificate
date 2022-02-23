
def factorial(n):
    if n<=1 : 
        return 1 
    else :
        return n * factorial(n-1)


print(factorial(3)) # Should be 6\
print(factorial(5)) # Should be 15\
print(factorial(10)) # Should be 55\