"""
This is simple login test program. First try.
Plan:
1. Create a file if it does not exist.
2. Open file and store data of user login and password.
3. Try to log in with that data from txt file.
"""


def input_data():
    """
    Take information from the user
    and store it in txt file.
    :return:
    """
    data = open("data.txt", "a+")
    unique_login = False

    f = open("data.txt", "r")
    login_set = set()
    for i in f.readlines():
        i = i.strip().split(":")
        login_set.add(i[0])

    while not unique_login:
        user_log_in = input("Input your log_in: ")
        if user_log_in not in login_set:
            unique_login = True
        else:
            print("This login already exist.")

    password = input("Input your password: ")
    data.write(f"{user_log_in}")
    data.write(":")
    data.write(f"{password}")
    data.write("\n")
    data.close()


def log_in():
    """
    Try to log_in using data from txt file.
    :return:
    """
    f = open("data.txt", "r")
    access = False
    login_and_password_dict = {}
    for i in f.readlines():
        i = i.strip().split(":")
        login_and_password_dict[i[0]] = i[1]

    login = input("Enter your login please:")
    password = input("Enter your password please:")
    for key, value in login_and_password_dict.items():
        if key == login and value == password:
            access = True

    if  access == True:
        print("Access granted.")
        return True
    else:
        print("Wrong login or password.")


def main_check():

    for i in range(3):
        if log_in():
            break
    else:
        print("\nYou are out of tries.  Access denied!")

input_data()
