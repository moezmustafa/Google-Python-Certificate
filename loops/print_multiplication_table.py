
#print the multiplication table 1 to 3

# def print_multiplication_table(low, high):
#     for i in range(low, high+1):
#         for j in range(1, i+1):
#             print(i, "x", j, "=", i*j, end="\t")
#         print()

# print_multiplication_table(1, 3)

def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(1 ,x+1):
			
			print(str(x*y) , end = " ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above