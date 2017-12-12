# implement commonly used functions here

import random
import ui
import smtplib
ver_code_table = [[]]


# generate and return a unique and random string
# other expectations:
# - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """
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
            new_item.insert(0, id_)
            for items in new_item:
                table[i].append(items)
    return table


def caesar(plaintext, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def username_pass(lst):
    tries = 3
    while True:
        User = ui.get_inputs(["Username: ", "Password: "], "Please provide the console informations")
        password = User[1]
        new_pass = caesar(password, 5)
        User[1] = new_pass
        if User in lst:
            return True
        else:
            tries -= 1
            if tries == 0:
                verification_code = generate_random(ver_code_table)
                ui.print_error_message("You have no more tries, sorry :(")
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("erpinformationltd@gmail.com", "Hermelin123?")
                msg = "Subject: ERP login \nSomebody tried to enter your ERP account 3 times with wrong password.\nIf you want to change your password, use this verification code:\n" + \
                    str(verification_code)
                server.sendmail("erpinformationltd@gmail.com", "semmiertelme13@gmail.com", msg)
                server.quit()
                return verification_code
            ui.print_error_message("You entered wrong password, you have " + str(tries) + " tries left")
