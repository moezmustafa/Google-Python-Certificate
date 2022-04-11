
def multiple_genereator(number):
    multiple = []
    for i in range(1 , 11):
     multiple.append(i * number)

    return multiple


print(multiple_genereator(3))
print(multiple_genereator(5))