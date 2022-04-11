# from ssl import OPENSSL_VERSION_INFO


# def sum_of_divisiors(n):
#     sum = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             sum += i
#             i+=1

#     return sum

# print(sum_of_divisiors(10)) # Should be 23
# print(sum_of_divisiors(11)) # Should be 28
# print(sum_of_divisiors(12)) # Should be 33
# print(sum_of_divisiors(13)) # Should be 40
# print(sum_of_divisiors(36)) # Should be 47


# #sum of the divisors of a number
# def sum_of_divisors(n):
#     sum = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             sum += i
#             i+=1

#     return sum

def sum_of_divisors(n):
    sum = 0
    
    for i in range(1, n):
        if n % i == 0 :
         sum = sum + i
         i = i + 1
    return sum

print(sum_of_divisors(36))

