import pickle
from regestredUsers import User
import os
from getpass import getpass
from datetime import datetime
import hashlib
from colorama import Fore, Back, Style
from package_info import show_package_info

logo = rf"""{Fore.MAGENTA}
{Fore.RED}    )                                         
 ( /(                   *   )              )  
 )\())   (   (        ` )  /(    )      ( /(  
((_)\   ))\  )(    (   ( )(_))( /(  (   )\()) 
{Fore.YELLOW} _((_) /((_)(()\   )\ (_(_()) )(_)) )\ ((_)\  
| \| |(_))   ((_) ((_)|_   _|((_)_ ((_)| |(_) 
{Fore.MAGENTA}| .` |/ -_) | '_|/ _ \  | |  / _` |(_-<| / /{Fore.CYAN}
|_|\_|\___| |_|  \___/  |_|  \__,_|/__/|_\_\ 
{Style.RESET_ALL}
"""

helpMessage = f"""
<< {Fore.CYAN} Welcome to {Fore.MAGENTA} NeroTask! {Fore.CYAN} {Style.BRIGHT} Here are the options available to you >>{Style.RESET_ALL}

{Fore.YELLOW}!!-All this commands are not case-sensitive-!!{Style.RESET_ALL}

> ({Fore.GREEN}help{Style.RESET_ALL}): {Style.BRIGHT}displays a list of all available commands and their explanations.{Style.RESET_ALL}
> ({Fore.RED}exit{Style.RESET_ALL}): {Style.BRIGHT}{Fore.RED}Exit{Fore.WHITE} the NeroTask app.{Style.RESET_ALL}
> ({Fore.RED}logout{Style.RESET_ALL}): {Style.BRIGHT}logs you out of the app.{Style.RESET_ALL}
> ({Fore.CYAN}list{Style.RESET_ALL}): {Style.BRIGHT}displays all of your current ToDos. | ({Fore.BLUE}list--sort{Fore.WHITE})-> displays all of your current ToDos sorted buy importance{Style.RESET_ALL}
> ({Fore.RED}delete{Style.RESET_ALL}): {Style.BRIGHT}prompts you to select a ToDo to delete. | ({Fore.RED}delete--all{Fore.WHITE})-> delete all ToDos{Style.RESET_ALL}
> ({Fore.MAGENTA}create{Fore.WHITE}): {Style.BRIGHT}allows you to create a new ToDo and add it to your list.{Style.RESET_ALL}
> ({Fore.CYAN}clear{Fore.WHITE}):{Style.BRIGHT} clear screen buffer{Style.RESET_ALL}
> ({Fore.YELLOW}edit{Fore.WHITE}): {Style.BRIGHT}allows you to edit your ToDo.{Style.RESET_ALL}
"""

# the user want to sing in or sign up

def loginOrSignUp():
    print(logo,"\n")
    print(f"{Style.BRIGHT}Welcome to {Fore.MAGENTA}NeroTask{Fore.WHITE} we are more than pleased to have you!\n{Style.RESET_ALL}")
    x = f"Log In ({Fore.GREEN}L{Style.RESET_ALL}) : Sign-Up ({Fore.GREEN}S{Style.RESET_ALL}): "
    LogInOrSignUp = input(x)
    
    while not (LogInOrSignUp.upper() in 'SL'):
        LogInOrSignUp = input(x)
    clear()
    if(LogInOrSignUp.upper() == "L"):
        logIn()
    else:
        signUp()
# get all the users from users.dat

def getUsers():
    with open("users.dat","rb") as F:
        users = (pickle.load(F))
    F.close

    return users
# check if username and password already exist


def userExist(username,passwd):
    users = getUsers()


    userExist = False

    for user in users:
        if(user.user == username and verifyPassword(user.passwd,passwd)):
            userExist = True
            break
    return userExist

# check if username already exist


def userNameExist(username):
    users = getUsers()
    userNameFound = False
    for user in users:
        if(user.user == username):
            userNameFound = True
    return userNameFound

def searchForUser(username):
    users = getUsers()
    for user in users:
        if(user.user == username):
            return user
    return 0
    
    
# user want's to register

def signUp():

    signedUp = False

    if(signedUp == False):
        print("SignUp: ")
        userName = input("\n>> User Name: ")
        passwd = getpass(">> Password: ")


        if(os.path.exists("users.dat")):
            while(userNameExist(userName) ):
                print("Sorry, the user name you have chosen is already taken")
                userName = input("\n>> User Name: ")
        while not (len(userName) >= 3):
            print("Your user name must be at least 3 characters long")
            userName = input("\n>> User Name: ")
        while not (len(passwd) >= 8 ):
            print("Your password must be at least 8 characters long")
            passwd = getpass(">> Password: ")
        if not (os.path.exists("users.dat")):
            with open("users.dat","wb") as F:
                pickle.dump([User(userName,hashPassword(passwd))],F)
        else:
            users = getUsers()
            users.append(User(userName,hashPassword(passwd)))
            with open("users.dat","wb") as F:
                pickle.dump(users,F)
        F.close()
        print("Process went successfully! ")
        signedUp == True

    logIn()

# user want's to login

def logIn():

    if(os.path.exists("users.dat")):
        print("LogIn: ")
        userName = input("\n>> User Name: ")
        passwd = getpass(">> Password: ")
        global logged
        while not (userExist(userName,passwd)):
            print("Incorrect username or password")
            userName = input("\n>> User Name: ")
            passwd = getpass(">> Password: ")
        print(f"Welcome {userName}, you have logged in successfully at {datetime.now()}")
        logged = userName
        console()
    else:
        print("There is no registred accounts")

def logOut():
    clear()
    loginOrSignUp()

# hash user's password before storing it 

def hashPassword(password:str):
    """Hash a password for storing."""
    salt = os.urandom(16)
    pwd = password.encode('utf-8')
    salted_hash = hashlib.sha256(salt + pwd).hexdigest()
    return (salt + salted_hash.encode())

# verify if user's password is correct

def verifyPassword(stored_password:bytes, provided_password:str):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:16]
    stored_password = stored_password[16:].decode()
    pwd = provided_password.encode('utf-8')
    return stored_password == hashlib.sha256(salt + pwd).hexdigest()



# print all of the user's ToDos organised 

def printToDos(sort = False):
    toDos = getUserToDos(logged)
    if(len(toDos) == 0):
        print("There is 0 ToDos to show")
    else:
        if(sort == True):
            noChange = False
            while(noChange == False):
                noChange = True
                for i in range(0,len(toDos)-1):
                    if(toDos[i+1]["importance"] > toDos[i]["importance"]):
                        aux = toDos[i]
                        toDos[i] = toDos[i+1]
                        toDos[i+1] = aux
                        noChange = False

        for toDo in toDos:
            print(f"{Fore.MAGENTA}/{Style.RESET_ALL}"*30 + "\n")
            print(f"{Style.BRIGHT}Title{Style.RESET_ALL}: " + toDo["title"] + "\n")
            print(f"{Style.BRIGHT}Task{Style.RESET_ALL}: \n" + toDo["task"] + "\n")
            print(f"{Style.BRIGHT}Date{Style.RESET_ALL}: " + toDo["date"] + "\n")
            print(f"{Style.BRIGHT}importance{Style.RESET_ALL}: " + str(toDo["importance"]) + "\n")
            print(f"{Fore.MAGENTA}/{Style.RESET_ALL}"*30 + "\n")



# create new ToDos and add it to the user's todo list

def createToDo():

    clientToDos = getUserToDos(logged)

    title = input("Title: ")

    for todo in clientToDos:
        while(todo["title"] == title):
            print("Title must be unique")
            title = input("Title: ")

    while(len(title) == 0):
        title = input("Title: ")
    task = input("Task: ")
    while(len(task) == 0):
        task = input("Task: ")
    date = str(datetime.now())

    while(True):
        try:
            importance = int(input("Enter a value between [1,5]: "))
            if(0<importance<=5):
                break
            else:
                print("value must be between 1 and 5")
        except ValueError:
            print("invalid input! please enter an integer")
    clients = getUsers()
    done = False
    for client in clients:
        if(client.user == logged):
            client.appendToDos(dict(title = title, task = task, date = date, importance = importance))
            done = True
    if(done):
        with open("users.dat","wb") as F:
            pickle.dump(clients,F)
        F.close() 

# delete todos from user's todo list  

def deliteToDos():
    x = f"{Fore.RED}Are you sure you want to delete all your toDos? (Y/N): {Style.RESET_ALL}"
    confirm = input(x)
    while not (confirm.upper() in "YN"):
        confirm = input(x)
    if(confirm.upper() == "Y"):
        clients = getUsers()
        for client in clients:
            if (client.user == logged):
                client.setToDos([])
        with open("users.dat","wb") as F:
            pickle.dump(clients,F)
        F.close()
    return

def deliteToDo():
    clientToDos = getUserToDos(logged)   
    if(len(clientToDos) == 0):
        print("there is 0 toDo to delete! ")
        return

    titleToDelet = input("Enter title of task you which to delete: ")
        
    for toDo in clientToDos:
        x = f"{Fore.RED}Are you sure you want to delete this task permanently? (Y/N): {Style.RESET_ALL}"
        if (toDo["title"] == titleToDelet):
            confirm = input(x)
            while not (confirm.upper() in "YN"):
                confirm = input(x)
            clientToDos.remove(toDo)
            if(confirm.upper() == "Y"):
                users = getUsers()
                for user in users:
                    if(user.user == logged):
                        user.setToDos(clientToDos)
                with open("users.dat","wb") as F:
                    pickle.dump(users,F)
                F.close()   
                print("ToDo deleted sucsussfully! ")
                return
            else:
                print("Process cancelled ")
                return
    print("There is no ToDo with this title ! ")


def getUserToDos(userName):
    try:
        return searchForUser(userName).getToDos()
    except:
        print("There is no such user! ")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def editToDo():
    clientToDos = getUserToDos(logged)
    if len(clientToDos) == 0:
        print("There is 0 ToDos to edit!")
        return

    titleToEdit = input("Enter the title of the task you wish to edit: ")
    toDoToEdit = None

    for toDo in clientToDos:
        if toDo["title"] == titleToEdit:
            toDoToEdit = toDo
            break

    if toDoToEdit is None:
        print("There is no ToDo with this title!")
        return

    print("Leave blank to keep the current value.")

    newTitle = input(f"Current Title: {toDoToEdit['title']}\nNew Title: ")
    if newTitle.strip() != "":
        toDoToEdit["title"] = newTitle

    newTask = input(f"Current Task: {toDoToEdit['task']}\nNew Task: ")
    if newTask.strip() != "":
        toDoToEdit["task"] = newTask

    while True:
        try:
            newImportance = input(f"Current Importance: {toDoToEdit['importance']}\nNew Importance [1,5]: ")
            if newImportance.strip() == "":
                break
            newImportance = int(newImportance)
            if 0 < newImportance <= 5:
                toDoToEdit["importance"] = newImportance
                break
            else:
                print("Value must be between 1 and 5")
        except ValueError:
            print("Invalid input! Please enter an integer")

    users = getUsers()
    for user in users:
        if user.user == logged:
            user.setToDos(clientToDos)

    with open("users.dat", "wb") as F:
        pickle.dump(users, F)
    F.close()
    print("ToDo edited successfully!")
    
# allows the user to access and operate various tasks management features.
# allow the user to view ToDos, create new ToDos,editing ToDos and deleting ToDos.

def console():
    x = f"{Style.BRIGHT + Fore.BLUE}Inter a command:{Style.RESET_ALL} "
    command = input(x)



    while(command.lower() != "exit"):

        while(command.lower() not in ["clear","help","exit","list","list--sort","delete","create","edit","logout","sort","delete--all"]):
            print("command not found enter (help) for help: ")
            command = input(x)
        if(command.lower() == 'help'):
            command = input(helpMessage + "\n" + x)
        if(command.lower() == "list"):
            printToDos()
            command = input("\n" + x)
        if(command.lower() == "list--sort"):
            printToDos(sort=True)
            command = input("\n" + x)
        if(command.lower() == "create"):
            createToDo()
            command = input("\n" + x)
        if(command.lower() == "delete"):
            deliteToDo()
            command = input("\n" + x)
        if(command.lower() == "delete--all"):
            deliteToDos()
            command = input("\n" + x)
        if(command.lower() == "clear"):
            clear()
            command = input("\n" + x)
        if(command.lower() == "logout"):
            confirm = input("Are you sure you want to Log-out of NeroTask? (Y/N): ") 
            while not (confirm.upper() in "YN"):
                confirm = input("Are you sure you want to Log-out of NeroTask? (Y/N): ") 
            if(confirm.upper() == "Y"):
                logOut()
            command = input("\n"+ x)
        if command.lower() == "edit":
            editToDo()
            command = input("\n"+x)


if __name__ == "__main__":
    show_package_info()
    loginOrSignUp()


