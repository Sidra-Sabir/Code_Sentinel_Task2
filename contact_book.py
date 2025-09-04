
while True:
    print("...Contact Book...")
    print("1. Add your contact")
    print("2. View your contacts")
    print("3. you can Exit")

    choice = input("Enter your choice/Option: ")

    if choice == "1":
        print("Add your contact")
        name = input("Enter you name: ")
        print(f"Name is: {name} ")
        phone_num = input("Enter your contact: ")
        print(f"Contact is: {phone_num} ")

        with open("contacts.txt", "a") as f:
            f.write(f"{name} , {phone_num}\n")
    
    elif choice == "2":
        print("You can view your saved contacts: ")  #you can view your saved contacts

        try:
            with open("contacts.txt", "r") as f:
                contacts = f.readlines()  # this function read your all lines
                if not contacts:
                    print("current contacts file not exist here")
                
                else: 
                    for contact in contacts:
                        if "," in contact:
                            name , phone_num = contact.strip().split(",", 1) #strip() funtion remove extra spaces from code 
                                                                             #while split used for formatting
                            print(f"{name} - {phone_num}")
                        
        except FileNotFoundError:
            print("no file found here")

    elif choice == "3":
        print("Say! Byeee")
        break #if we don't used this break program never ending
    else:
        print("invalid")
        

