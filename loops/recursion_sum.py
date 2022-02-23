def sum_positive_numbers(n) :
    if n == 1:
        return 1
    else:
        return n + sum_positive_numbers(n-1)


print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
print(sum_positive_numbers(10)) # Should be 55
print(sum_positive_numbers(20)) # Should be 210
print(sum_positive_numbers(50)) # Should be 123450
print(sum_positive_numbers(100)) # Should be 5050

