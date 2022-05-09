import sqlite3
import sys

connection = sqlite3.connect("userinfo.db")
cursor = connection.cursor()

# returns a list of every user registered in the program
def getUserList():
    cursor.execute("SELECT name FROM sqlite_master")
    userList = []
    for table in cursor.fetchall():
        userList.append("".join(table).lower())
    return userList

# returns a list containing the data for a specified user
def getUserData(userSelection):
    data = []
    for row in cursor.execute(f"SELECT * FROM {userSelection}"):
        data.append(" ".join(row))
    return data[0].split(" ")

# print the users registered in the database
def printUsers(message):
    userList = getUserList()
    if len(userList) == 0:
        print("There are no users registered to delete")
        return "No users"
    print(message)
    for user in userList:
        print(user.capitalize())

# prints the information provided for a given user
def printUserInfo(userSelection):
    info = ["Sid", "Auth", "Personal number", "Twilio number"]
    data = getUserData(userSelection)
    for i in range(0, 4):
        print(info[i] + ": " + data[i])

# removes a user from the database
def removeUser(userSelection):
    cursor.execute(f"DROP TABLE IF EXISTS {userSelection}")
    connection.commit()

# check user input, and perform the given function passed into it
def getInput(function):
    userSelection = input()
    if userSelection.lower() in getUserList():
        function(userSelection)
        return "break"
    elif userSelection.lower() == "exit":
        sys.exit()
    else:
        print(f"{userSelection} is not a valid user. Please try again")
        print("Enter 'exit' if you wish to leave the program")

# this will only run if Users.py is called directly (not being imported)
if __name__ == "__main__":
    print("Enter 'exit' at any point to leave the program")
    choice = input("1. add a new user\n2. view user information\n3. delete a user\n")
    firstUse = True

    # main loop to add users / view user information / delete a user
    while True:

        if not firstUse:
            again = input("Continue using Users.py? [y/n] ")
            if again == "n":
                break
            else:
                choice = input("1. add a new user\n2. view user information\n3. delete a user\n")

        while True:
            if choice == "1":
                user = input("what is the user's name? ").upper()
                if user == "EXIT":
                    sys.exit()
                elif user.lower() in getUserList():
                    print(f"The user {user.capitalize()} is already registered. Use a different name")
                    continue
                cursor.execute(f"""CREATE TABLE IF NOT EXISTS {user}
                                (sid text, auth text, personalNumber text, twilioNumber text)""")

                sid = input("enter the sid: ").strip()
                auth = input("enter the auth: ").strip()
                while True:
                    personalNumber = input("enter your personal number: ").strip()
                    if "+" not in personalNumber:
                        print("The international dialing prefix was not included in the personal number. If you are based in the U.S, this means your phone number should start with +1")
                        continue
                    twilioNumber = input("enter your given twilio number: ").strip()
                    if "+" not in twilioNumber:
                        print("The international dialing prefix was not included in the twilio number. Copy down the twilio number exactly as given to you from Twilio.com")
                        continue
                    break

                if "exit" in [sid.lower(), auth.lower(), personalNumber.lower(), twilioNumber.lower()]:
                    print("Keyword 'Exit' detected in user information. Aborting the program...")
                    sys.exit()

                INSERT_QUERY = f"""INSERT INTO {user}
                                (sid, auth, personalNumber, twilioNumber) 
                                VALUES 
                                ('{sid}','{auth}','{personalNumber}','{twilioNumber}')"""

                cursor.execute(INSERT_QUERY)
                connection.commit()
                firstUse = False
                break

            elif choice == "2":
                if printUsers("Which user would you like to view?") == "No users": break
                while True:
                    if getInput(printUserInfo) == "break": break
                connection.commit()
                firstUse = False
                break

            elif choice == "3":
                if printUsers("Which user would you like to remove?\nUsers Registered:") == "No users": break
                while True:
                    if getInput(removeUser) == "break": break
                connection.commit()
                firstUse = False
                break

            elif choice.lower() == "exit":
                sys.exit()

            else:
                print("Invalid input. Enter '1', '2', or '3'")
                choice = input("1. add a new user\n2. view user information\n3. delete a user\n")
