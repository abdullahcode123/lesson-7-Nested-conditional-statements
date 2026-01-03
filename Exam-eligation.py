mc=input("Enter your Medical Couse y or n= ")
aten=int(input("Enter the students Attendence= "))

if mc=='y':
    print("You  are alowed")
else:
    if aten<=75:
        print("Allowed")
    else:
        print("Not allowed")