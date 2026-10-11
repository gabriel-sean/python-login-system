import time
import os
import sys

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# returns the dictionary of {'user': 'password'}
def load_users():
    users = {}
    try:
        with open('database.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if not line or ':' not in line:
                    continue
                parts= line.split(':')
                if len(parts) != 2:
                    continue
                userid, password = parts
                users[userid] = password
    except FileNotFoundError:
        pass
    return users

# accepts the users dictionary and overwrite it in the file
def save_users(users):
    with open('database.txt', 'w') as f:
        for userid, password in users.items():
            f.write(f"{userid}:{password}\n")

# returns true if userid is available
def is_userid_avaialable(userid):
    users = load_users()
    return userid not in users

# data validation for userid: no space, colon, emptyline
def check_userid_format(userid):
    if ':' in userid:
        return "\nColons are not allowed."
    if ' ' in userid:
        return "\nSpaces are not allowed."
    if not userid:
        return "\nUserid can't be empty."
    return None   # None means "no problem"

def login():
    while True:
        print('Log in\n')
        userid = input('Type -quit to go back to main menu\nEnter your userid: ')
        
        if userid == '-quit':
            clear_console()
            return
        
        users = load_users()
        error = check_userid_format(userid)        
        if error:
            print(error)
            time.sleep(1)
            clear_console()
            continue


        if userid not in users:
            print('\nuserid not found, please try again.')
            time.sleep(1)
            clear_console()
            continue

        password = input('Enter your password: ')
        if password == '-quit':
            clear_console()
            return
        if users[userid] == password:
            print('\nYou\'re in!')
            time.sleep(1)
            clear_console()
            home(userid)
            return
        else:
            print('\nIncorrect password. Please try again.')
            time.sleep(1)
            clear_console()
            continue

def register():

    def create_password(userid):
        while True:    
            print('Now, create your password. A colon \':\' is not allowed\n\nType -quit to go back to main menu')
            firstpassword = input('Enter password: ')
            if firstpassword == '-quit':
                clear_console()
                return

            confirmpassword = input('Confirm your password: ')
            if firstpassword != confirmpassword:
                print('\nPasswords don\'t match, please try again.')
                time.sleep(1)
                clear_console()
                continue

            users = load_users()
            users[userid] = firstpassword
            save_users(users)
            print('\nSuccessfully created your account, you will be redirected back to login page, please sign in.')
            time.sleep(3)
            clear_console()
            return

    while True:
        print('Create a userid. A colon \':\'or space is not allowed\n\nType -quit to go back to main menu')
        userid = input('Enter userid: ')
        error = check_userid_format(userid)
        if error:
            print(error)
            time.sleep(1)
            clear_console()
            continue
        elif userid == '-quit':
            clear_console()
            return
        else:
            if is_userid_avaialable(userid) is False:
                print('\nThis userid is taken, please try again\n')
                time.sleep(1)
                clear_console()
                continue
            clear_console()
            create_password(userid)
            return

#login page 
def main():
    while True:
        clear_console()
        print("Welcome to our login page!\n")
        print("Select a number to proceed:\n")
        print("[0] Login")
        print("[1] Register")
        print("\nType -quit to quit the program")

        option = input("Enter your choice: ")

        if option == '0':
            clear_console()
            login()
        elif option == '1':
            clear_console()
            register()
        elif option == '-quit':
            clear_console()
            sys.exit()
        else:
            print('\nInvalid number')
            time.sleep(1)
            clear_console()
            continue

def home(userid):  
    while True:
        print(f'Welcome to our system, {userid}!')
        print('\nWhat do you want to do today?')
        print("[0] Change my userid")
        print("[1] Change my password")
        print("[2] Delete my account")
        print("[3] See all users and their passwords")
        print("[4] Sign out")
        print("\nType -quit to quit the program")
        choice = input('Enter your choice: ')

        if choice == '-quit':
            clear_console()
            sys.exit()
        elif choice == '0':
            clear_console()
            userid = changeuserid(userid)
        elif choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            return
        else:
            print('Invalid number')
            time.sleep(1)
            clear_console()
            continue

def changeuserid(userid):

    while True:
        users = load_users()
        print(f'Hi, {userid}!')
        print('Create a new userid. A colon \':\'or space is not allowed\n\nType -quit to go back to home page')
        newuserid = input('Please enter your new userid: ')

        error = check_userid_format(newuserid)
        if error:
            print(error)
            time.sleep(1)
            clear_console()
            continue
        if newuserid == userid:
            clear_console()
            print('That\'s already your userid.')
            time.sleep(1)
            continue
        if newuserid == '-quit':
            clear_console()
            return userid
        if not is_userid_avaialable(newuserid):
            print('\nThis userid is already taken, please try again.')
            time.sleep(1)
            clear_console()
            continue

        users[newuserid] = users.pop(userid)
        save_users(users)
        clear_console()
        print(f'Successfully changed your userid to {newuserid}!')
        time.sleep(2)
        clear_console()
        return newuserid

main()