print("enter your choice")
print("1 = bike")
print("2 = car")

choice=int(input("Enter your choice 1 or2"))

if (choice==1):
    print("What type of bike ")
    print("1 Splender")
    print("2 KTM")
    bike=int(input("Enter your second choice"))
    if bike==1:
        print("You have selected splender")
    else:
        print("You have selected KTM")
elif (choice==2):
    print("What type of Car ")
    print("1 Lanborghini")
    print("2 Bughatti")
    car=int(input("Enter your third and last choice "))
    if car==1:
        print("You have selected Lamborghini")
    else:
        print("You have selected Bughatti")
else:
    print("Yopu entera wrong choice")