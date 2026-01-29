# Email ID generator/suggester

# Import Using Modules
import random
import time

# Askign the user for what purpose user need Email;

print("Welcome! Dear Sir/Madam")
print("Fill your Details Please")
time.sleep(0.5)
time.sleep(0.5)
print("Processing the Data")
time.sleep(0.5)
time.sleep(0.5)


def main():

    # Ask Details to user

    b = input("Enter your name: ")
    a = int(input("Enter your Age: "))
    c = input("Enter your DOB: ")
    d = input("For what purpose you are making this Email: ")
    e = input("Name of your Profession: ")
    f = input("Enter your Gender (Male/Female): ")
    
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    print("Saving your Details!")
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    # Setting the Gender and respect Call accoring to the user detail;

    if f.lower() == "male":
        Gender = "Male"
        Respect_Call = "Sir"
    else:
        Gender = "Female"
        Respect_Call = "Mam"

    # Making a file of user with it's Details;

    file = open(f"{b}_{e}_Email_ID.txt", "w")
    file.write(f"Your Details {Respect_Call},\n Your name: {b}\n your Age: {a}\n your DOB: {c}\n Your Gender {Gender}\n Email creating purpose: {d}")
    file.close()

    # Asking the computer to Choose random numbers;

    number = random.choice(range(1, 1000))

    # making the list of all the details;
    list = [a,b,c,d,e,f,Gender]

    # Asking computer to choose any thing from the list

    Start_letter = random.choice(list)
    end_letter = random.choice(list)
    Start_letter1 = random.choice(list)
    end_letter1 = random.choice(list)
    Start_letter2 = random.choice(list)
    end_letter2 = random.choice(list)
    Start_letter3 = random.choice(list)
    end_letter3 = random.choice(list)

    # Generating the Email;

    email1 = f"{Start_letter}_{end_letter}_{number}@gmail.com"
    email2 = f"{Start_letter1}_{end_letter1}_{number}@gmail.com"
    email3 = f"{Start_letter2}_{end_letter2}_{number}@gmail.com"
    email4 = f"{Start_letter3}_{end_letter3}_{number}@gmail.com"

    # Printing the Email of user in another file and in the terminal

    user = input("You want Email in File or in Terminal: ")

    if user.lower() == "file":
        file = open(f"{b}_{e}_Email_ID.txt", "a")
        file.write(f"\n\nDear {Respect_Call},\n We have generate four emails for you choose your and create by your choice\n\n email 1 = {email1},\n email 2 = {email2},\n email 3 = {email3},\n email 4 = {email4}\n\n Thanks to use our application, Please visit again! ")
        print(f"Please Check Your file has been generated {Respect_Call}")
        file.close()
    else:
        print(f"\n\nDear {Respect_Call},\n We have generate four emails for you choose your and create by your choice\n\n email 1 = {email1},\n email 2 = {email2},\n email 3 = {email3},\n email 4 = {email4}\n\n Thanks to use our application, Please visit again! ")


# play main from starting of code;
main()

# Asking user to make more;

ask = input("Do you want to generate again! (Yes/No): ")
time.sleep(0.5)
time.sleep(0.5)
print(f"Processing....")
time.sleep(0.5)
time.sleep(0.5)
print(f"Processing....")
time.sleep(0.5)
time.sleep(0.5)
if ask.lower() == "yes":
    main()    
    
print("Thanks to use our code, please visit again!")