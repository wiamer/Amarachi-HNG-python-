#get user details
import random
import string
def userdetails():
    User_firstname = input('What is your First Name: ')
    User_Lastname = input('What is your Last Name: ')
    User_email = input('Please enter your email address: ')
    details = [User_firstname, User_Lastname, User_email]
    user_details = {
        "First Name": User_firstname, 
        "Last Name": User_Lastname, 
        "Email": User_email
    }
    return details
    

#generate password for user
def gen_password():
    characters = string.ascii_lowercase
    lenght = 5
    random_password = ''.join(random.choice(characters)for i in range(lenght))
    password = str(details[0][0:2] + details [1][-2:] + random_password)
    return password

#Main program
status = True
container = []

users = {}
usernumber = 1

while status:
    details = userdetails()

    print ('Your password is: ' + gen_password())
    password_like = input(str('Do you like the generated password, If yes eneter Yes; if no, enter No and supply your password: '))

    password_loop = True
    while password_loop:
        if password_like == 'Yes':
            #add password to userdetails
            details.append(gen_password())


        #add user detsails to overall container
            container.append(details)

            print(container)
        else:
            #enter a password longer or equal to 7
            user_password = input('Enter password longer than or equal to 7: ')

            #password length loop
            pass_len = True

            while pass_len:
                if len(user_password) >= 7:

                    #add password to user details
                    details.append(user_password)

                    #add user details to container
                    container.append(details)

                    #break out of password lenght loop
                    pass_len = False


                else:
                    print('Your password is less than 7')
                    user_password = input('Enter password longer than or equal to 7: ')

                    #break out of the whole password loop
            password_loop = False
            print(container)
            status = True
#new user
new_user = input('would you like to enter a new user? Yes or No: ')

if (new_user == 'No'):

    status = False

else:
    status = True
    
print(container)

