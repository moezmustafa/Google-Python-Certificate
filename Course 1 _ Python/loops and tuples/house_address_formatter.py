# def format_address(address_string):
#   # Declare variables

#   # Separate the address string into parts

#   # Traverse through the address parts
#   for __:
#     # Determine if the address part is the
#     # house number or part of the street name

#   # Does anything else need to be done 
#   # before returning the result?
  
#   # Return the formatted string  
#   return "house number {} on street named {}".format(__)

# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"

# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"

# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"


string = "55 North Center Drive"
street_part = ""
# Separate the string into parts
address_parts = string.split()
print(address_parts)

for index in address_parts:
    if index.isdigit():
        number_part = index
    elif index.isalpha():
       street_part = street_part + " " + index

print("house number {} on street named {}".format(number_part, street_part))



#FINAL CODE BELOW 
#FINAL CODE BELOW 
#FINAL CODE BELOW 
#FINAL CODE BELOW 
#FINAL CODE BELOW 
#FINAL CODE BELOW 
#FINAL CODE BELOW 
#FINAL CODE BELOW 
#FINAL CODE BELOW 

print("\n")
print("\n")
print("\n")
print("\n")



def format_address(address_string):
  # Declare variables
    new_string = ""
    number_part = ""
    street_part = ""
  # Separate the address string into parts
    new_string = address_string.split()
  # Traverse through the address parts
    for words in new_string:
        if words.isdigit():
            number_part = words
        elif words.isalpha():
            street_part = street_part + " " + words
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
    return "house number {} on street named {}".format(number_part, street_part)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
