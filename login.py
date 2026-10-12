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

# accepts a modified users dictionary and overwrite it in the file
def save_users(users):
    with open('database.txt', 'w') as f:
        for userid, password in users.items():
            f.write(f"{userid}:{password}\n")

# returns true if userid is available
def is_userid_available(userid):
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

# returns an error message if password format is invalid
def check_password_format(password):
    if ':' in password:
        return "\nColons are not allowed."
    if not password:
        return "\nPassword can't be empty."
    return None

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
            
            isinvalid = check_password_format(firstpassword)
            
            if isinvalid:
                clear_console()
                print(isinvalid, "Please try again.")
                time.sleep(1)
                continue

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
            if is_userid_available(userid) is False:
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

#home page
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
            clear_console()
            change_password(userid)
        elif choice == '2':
            clear_console()
            isdeleted = delete_account(userid)
            if isdeleted:
                return # user deleted, back to main page (login)
        elif choice == '3':
            view_all_users()
        elif choice == '4':
            return
        else:
            print('Invalid number')
            time.sleep(1)
            clear_console()
            continue

def changeuserid(userid):

    while True:
        clear_console()
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
        if not is_userid_available(newuserid):
            print('\nThis userid is already taken, please try again.')
            time.sleep(1)
            clear_console()
            continue

        # users.pop(userid) delete the old userid then assign its password to the new userid added on the dictionary
        users[newuserid] = users.pop(userid)
        save_users(users)
        clear_console()
        print(f'Successfully changed your userid to {newuserid}!')
        time.sleep(2)
        clear_console()
        return newuserid

def change_password(userid):

    while True:
        users = load_users()
        print(f'Hi, {userid}!')
        print('Create a new password. A colon \':\' is not allowed\n\nType -quit to go back to home page')
        password = input('Please enter your current password: ')

        if password == '-quit':
            return

        if password != users[userid]:
            clear_console()
            print('\nIncorrect password, please try again.')
            time.sleep(1)
            continue

        newpassword = input('\nPlease enter your new password: ')
        error = check_password_format(newpassword)
        if error:
            clear_console()
            print(error, "Please try again.")
            time.sleep(1)
            continue

        confirmnewpassword = input('Please confirm your new password: ')
        if newpassword != confirmnewpassword:
            clear_console()
            print('\nYour new password doesn\'t match, please try again.')
            time.sleep(1)
            continue

        users[userid] = newpassword
        save_users(users)
        clear_console()
        print('\nYou have successfully changed your password.')
        time.sleep(1)
        return
    return

def delete_account(userid):
    clear_console()
    # Confirm
    while True:
        print(f'Hi, {userid}!')
        choice = input('Are you sure you want to delete your account? This is not reversible [y/n]: ')
        if choice.lower() == 'y':
            break
        if choice.lower() == 'n':
            return None
        print("\nPlease enter 'y' or 'n'.")
        time.sleep(1)
        clear_console()

    # Password verify

    while True:
        users = load_users()
        print('\nType -quit to go back to home page')
        password = input('Please enter your password to continue deleting your account: ')
        if password == '-quit':
            return None
        if password == users[userid]:
            break
        print('\nIncorrect password, please try again.')
        time.sleep(1)
        clear_console()

    # Delete
    del users[userid]
    save_users(users)
    clear_console()
    print(f'Sorry to see you go, {userid}. Bye!')
    time.sleep(2)
    return True

def view_all_users():
    clear_console()
    users = load_users()
    if not users:
        print('\nNo users registered yet.')
        time.sleep(2)
        clear_console()
        return
    print('userid, password')
    for user in sorted(users):
        print(f'{user}, {users[user]}')

    input('\nPress Enter to continue...')
    clear_console()


main()