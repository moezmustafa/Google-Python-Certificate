#count the number of digits in the number
def digits(n):
    count = 0

    if n == 0:
        return 0



    while n != 0:
        print("value of number is " ,n)
        print("value of count is " ,count)
        count += 1
        
        n = n // 10
    return count

print(digits(25))   # Should print 2
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1





# def digits(n):
# 	count = 0
# 	if n==0:
# 		count = 1
# 		return count 
# 	while (n>0):
# 		count += 1
# 		n = n // 10
# 	return count
	
# print(digits(25))   # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000)) # Should print 4
# print(digits(0))    # Should print 1

