#count the digits in the number 

# def digits(n):
#     if n == 0:
#         return 0
#     else:
#         return 1 + digits(n/10)


# def digits_4(n):
# 	count = 0

# 	while (n!=0):
# 		count += 1
# 		n = n / 10
# 	return count



# def digits(n) :
#     count = 0
#     while n != 0 :
#         count += 1
#         n = n / 10
#     return count


	
# print(digits(25))   # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000)) # Should print 4
# print(digits(0))    # Should print 1





def digits(n):
 count = 0
 m = 1
    if n == 0:
	  return 0
      m =0 
        while (m!=0):
		count += 1
		n = n // 10             #use the floor divison to get the eact answer 
        
    return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

