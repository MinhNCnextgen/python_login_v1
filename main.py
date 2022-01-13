# import
import os
import uuid
import data_encryptor as ec

def change_path(dir_name):
    # Changes the working dir
    tmp_path = os.path.join(os.path.dirname(__file__), dir_name)
    if os.path.isdir(tmp_path) == False:
        os.mkdir(dir_name)
    os.chdir(tmp_path)
    return tmp_path


def sign_up(user, pasw):
    # Initiate the sign up process
    user_id = str(uuid.uuid4())
    with open(str(user_id + '.txt'), 'w') as wf:
        wf.write(user + '\n')
        ec_pasw = ec.encrypt(pasw)
        wf.write(ec_pasw + '\n')
        wf.write(user_id + '\n')


def is_user_legal(name, pasw):
    # Checks if us and pasw is valid
    invalid_char = '!@#$%^&*()_+{[}]-=|\/;\'\";,.<>?`~'
    for char in invalid_char:
        if (char in name) or (char in pasw):
            print('Name and/or Password must not special characters!')
            return False
    if (' ' in name) or (' ' in pasw):
        print('Username and/or Password can\'t contain space(s)!')
        return False
    if len(name) < 3 or len(pasw) < 6:
        print('Name(>=3) and/or Password(>=6) is too short!')
        return False
    if len(os.listdir()) != 0:
        for file in os.listdir():
            with open(file, 'r') as rf:
                curr_name = list(rf.readlines())[0].strip()
                if name == curr_name:
                    print('Name already exists!')
                    return False
    return True


def log_in(user, pasw):
    #Initite the log in process
    is_user = False
    is_password = False
    for file in os.listdir():
        with open(file, 'r') as rf:
            raw_data = list(rf.readlines())
            data = []
            for item in raw_data:
                data.append(item.strip())
            if data[0] == user:
                is_user = True
                dc_pasw = ec.decrypt(data[1])
                if dc_pasw == pasw:
                    is_password = True
    if is_user:
        if is_password:
            return data
        else:
            return 'Incorrect Password!'
    else:
        return 'Wrong Username!'


def main():
    # Main function
    PATH = change_path('accounts')
    state = True
    while state:
        print('Hello User, what do you want to do?: Login(0) Signup(1)')
        ask = str(input())
        if ask == '0':
            print("Login initiated")
            state = False
        elif ask == '1':
            print("Signup initiated")
            state = False
        else:
            continue
    state = True
    while state:
        username = input('Enter username: ')
        password = input('Enter password: ')
        if ask == '1':
            if is_user_legal(username, password):
                sign_up(username, password)
                state = False
        elif ask == '0':
            content = log_in(username, password)
            if type(content) is list:
                str_to_print = 'Welcome back, {0} with the user ID of \"{1}\" !'.format(content[0], content[2])
                print(str_to_print)
                state = False
            elif type(content) is str:
                print(content)
    input('Press enter to close the program ')


if __name__ == "__main__":
    if os.path.isfile('secret.key') ==  False:
        ec.make_key()
    main()
    
