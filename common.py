import random
import ui
import smtplib
import data_manager
import os


def generate_random(table=[[]]):
    while True:
        generated = ''

        for k in range(2):
            generated = generated + (random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        for k in range(2):
            generated = generated + (random.choice("abcdefghijklmnopqrstuvwxyz"))
        for k in range(2):
            generated = generated + (random.choice("0123456789"))
        for k in range(2):
            generated = generated + (random.choice('!@#$%^&*()?'))

        for i in table:
            if generated not in i:
                return generated


def convert_to_list(csv_file):
    list1 = []
    with open(csv_file, "r") as f:
        for line in f.readlines():
            list1.append(line.strip("\n").split(";"))
    return list1


def common_add(table, list):
    new_item = (ui.get_inputs(list, "Please provide the console informations"))
    os.system('clear')
    new_item.insert(0, generate_random(table))
    table.append(new_item)
    return table


def common_remove(table, id_):
    for i in table:
        if id_ in i:
            table.remove(i)

    return table


def common_update(table, list, id_):
    for i in range(len(table)):
        if id_ in table[i]:
            table[i] = []
            new_item = (ui.get_inputs(list, "Please provide the console informations"))
            os.system('clear')
            new_item.insert(0, id_)
            for items in new_item:
                table[i].append(items)
    return table


def caesar(plaintext, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def username_pass(lst, mail):
    tries = 3
    while True:
        User = ui.get_inputs(["Username: ", "Password: "], "Please provide the console informations")
        os.system('clear')
        password = User[1]
        new_pass = caesar(password, 5)
        User[1] = new_pass
        User = [[User[0]], [User[1]]]
        if User == lst:
            return True
        else:
            tries -= 1
            if tries == 0:
                verification_code = generate_random()
                ui.print_error_message("You have no more tries, sorry :(")
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("erpinformationltd@gmail.com", "Hermelin123?")
                msg = "Subject: ERP login \n" + "Dear " + str(lst[0][0]) + "," + "\nSomebody tried to enter your ERP account 3 times with wrong password.\nIf you want to change your password, use this verification code:\n" + \
                    str(verification_code)
                server.sendmail("erpinformationltd@gmail.com", mail, msg)
                server.quit()
                return verification_code
            ui.print_error_message("\nYou entered wrong password, you have " + str(tries) + " tries left\n")


def new_password_request(ver_code, user, filename):
    answer = ui.get_inputs(["Enter yes or no: "], "Do you want to change your password?\n")
    os.system('clear')
    answer = answer[0]
    if answer == "yes":
        input_verification = ui.get_inputs(["Verification code: "], "Please enter the verification code we sent you.\n")
        input_verification = input_verification[0]
        os.system('clear')
        if input_verification == ver_code:
            new_pass = ui.get_inputs(["Your new password: "], "Please enter your new password.\n")
            os.system('clear')
            coded_pass = caesar(new_pass[0], 5)
            psword = coded_pass
            Username = user[0][0]
            table_users = [[Username], [psword]]
            data_manager.write_table_to_file(filename, table_users)
            print("Your code is succesfully changed.")
        else:
            os.system('clear')
            ui.print_error_message("\nYou entered wrong verification code\n")
