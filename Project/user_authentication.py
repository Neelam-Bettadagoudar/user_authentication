import re
import os

def login():
    user = input('Please enter your username\email:\n')
    
    found = True
    with open('Users.TXT') as file:
        for line in file:
            line = line.strip()
            if user == line:
                print("User has already registered. Please login:\n")
                found = True
                break
                passcheck = input('Please enter you password:\n')
                pfound = True
                with open('Passwords.TXT') as pfile:
                    for line in pfile:
                        line = line.strip()
                        if passcheck == line:
                            print("Password Found")
                            pfound = True
                            break
                        if not pfound:
                            print ('Password not found')
                            login()
                            if not found:
                                print("user not found")
                                login()

login()
def register():
    username = input ("Please type in an email address:\n ")
    
    if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",username,re.IGNORECASE):
        print("valid")
        
        password=input("Enter password:\n")
        x=re.sub('[^!@#$%^&*]',"",password)
        n=re.sub('[^0-9]',"",password)
        if len(x)>=1 and len(n)>=1 and len(password)>=5 and len(password)<=16:
            password1 = input("Confirm password:\n")
            if password1 == password:
                file = open("Users.txt","a")
                file.write(username)
                file.write(",")
                file.write(password)
                file.write("\n")
                file.close()
                print("Successful")
            
            else:
                print("password doesn't match.Please enter again")
                register()
        else:
            print("passord is weak, Must have minimum one special character,one digit,one uppercase, one lowercase character")
            register()
    else:
        print("Invalid.Enter again")
        register()


register()



              







