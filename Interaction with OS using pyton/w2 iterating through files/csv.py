import csv 

with open ("csv_file.txt" , "w") as file : 
    csv_f = csv.reader(file)

for row in csv_f : 
        name, phone ,role = row
        print("Name:{} , Phone: {} , Role:{}".format(name,phone,role))
