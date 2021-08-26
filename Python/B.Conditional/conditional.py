# conditional statements
# Beauty products
Menu="Beauty cream","Face wash","body lotion","Face cream","BB cream","skin cream"
print(Menu)
Customer=input("Select Your Product")


# if
Customer=input("Select Your Product")
if(Customer=="Beauty cream"):
    print("offer 1+1 (Beauty cream+face cream)")


# if-else
Customer=input("Select Your Product")
if(Customer=="Beauty cream"):
    print("offer 1+1 (Beauty cream+face cream)")
else:
    print("No offers avaiable")


# if-elif-else
Customer=input("Select Your Product")
if(Customer=="Beauty cream"):
    print("offer 1+1 (Beauty cream + face cream)")
elif(Customer=="Face cream"):
    print("offer 1+1 (Body lotion cream + BB cream)")
elif(Customer=="BB cream"):
    print("offer 1+1 (Beauty cream + skin cream)")
else:
    print("No offers avaiable")


# Nested if
Customer=input("Select Your Product")
if(Customer=="Beauty cream"):
    if(Customer=="BB cream"):
        print("2+2 offer (Beauty cream,BB cream + Face cream,face wash)")

# Nested if-else
Customer=input("Select Your Product")
if(Customer=="Beauty cream"):
    if(Customer=="BB cream"):
        print("2+2 offer (Beauty cream,BB cream + Face cream,face wash)")
    else:
        print("if u want offer buy one more product")
elif(Customer=="Face cream"):
    if(Customer=="BB cream"):
        print("2+2 offer (Face cream,BB cream + Face cream,face wash)")
    else:
        print("if u want offer buy one more product")
else:
    print("Thank you for shopping")