import os
import ui
import data_manager
import common
e_mail = "kovacsgaboo@gmail.com"
Login = False
the_list = data_manager.get_table_from_file("crm/customers.csv")
menu_list = ["name:", "email:", "subscribed:"]


def start_module():
    while True:
        users = data_manager.get_table_from_file("crm/password.csv")
        ui.print_menu("Accounting", ["show_table", "add", "remove", "update", "login",
                                     "most profitable year", "avarage amount"], "Go back to main menu")
        menu_choose_list = ui.get_inputs(["Choose: "], "")
        menu_choose = int(menu_choose_list[0])
        if menu_choose == 1:
            os.system('clear')
            show_table(the_list)
            menu_list.remove("id")
            ui.get_inputs(["Press a button: "], "")
            os.system('clear')
        elif menu_choose == 2:
            os.system('clear')
            try:
                if Login:
                    add(the_list)
            except NameError:
                ui.print_error_message("\nYou don't have permission to do that!\nPlease login first!\n")
        elif menu_choose == 3:
            os.system('clear')
            try:
                if Login:
                    show_table(the_list)
                    menu_list.remove("id")
                    id = ui.get_inputs(["ID: "], "Please enter an id: ")
                    id = id[0]
            except NameError:
                ui.print_error_message("\nYou don't have permission to do that!\nPlease login first!\n")
        elif menu_choose == 4:
            os.system('clear')
            try:
                if Login:
                    show_table(the_list)
                    menu_list.remove("id")
                    id = ui.get_inputs(["ID: "], "Please enter an id: ")
                    id = id[0]
                    update(the_list, menu_list, id)
            except NameError:
                ui.print_error_message("\nYou don't have permission to do that!\nPlease login first!\n")
        elif menu_choose == 5:
            os.system('clear')
            Logged = common.username_pass(users, e_mail)
            if Logged == True:
                print("You logged in succesfully.")
                Login = True
            else:
                common.new_password_request(Logged, users, "crm/password.csv")
        elif menu_choose == 6:
            os.system('clear')
            ui.print_result(get_longest_name_id(the_list), "The id of the longest name: ")
        elif menu_choose == 7:
            os.system('clear')
            ui.print_result(get_subscribed_emails(the_list), "Subscribers :")
        elif menu_choose == 0:
            os.system('clear')
            data_manager.write_table_to_file("crm/customers.csv", the_list)
            return
        else:
            raise KeyError("There is no such options")


def show_table(table):
    menu_list.insert(0, "id")
    ui.print_table(table, menu_list)


def add(table):
    while True:
        returnable_list = common.common_add(table, menu_list)

        if (returnable_list[-1][1]).isdigit() == False and \
            "@" in returnable_list[-1][2] and \
                returnable_list[-1][3] == "0" or returnable_list[-1][3] == "1":
            return returnable_list
        else:
            the_list.remove(the_list[-1])
            ui.print_error_message("\nYou entered wrong inputs\n")


def remove(table, id_):
    return common.common_remove(table, id_)


def update(table, list, id_):
    while True:
        returnable_list = common.common_update(table, list, id_)

        for item in returnable_list:
            if id_ in item:
                comparable_list = item

        if (comparable_list[1]).isdigit() == False and \
            "@" in comparable_list[2] and \
                comparable_list[3] == "0" or comparable_list[3] == "1":
            return comparable_list
        else:
            ui.print_error_message("\nYou entered wrong inputs\n")


def get_longest_name_id(table):
    names = []
    longest_name = ""
    longest_names = []
    longest_name_id = []
    for line in table:
        names.append(line[1])
    for name in names:
        if len(name) > len(longest_name):
            longest_name = name
    longest_names.append(longest_name)
    for name in names:
        if len(name) == len(longest_name):
            longest_names.append(name)
    longest_name = min(longest_names)
    for line in table:
        if longest_name in line:
            return line[0]


def get_subscribed_emails(table):
    list = []
    for line in table:
        if line[3] == "1":
            list.append(line[2] + ";" + line[1])
    return list


def get_name_by_id(id):

    the_list = data_manager.get_table_from_file("crm/customers.csv")
    name = ""
    for item in the_list:
        if item[0] == id:
            name = item[1]
    if name == "":
        return None
    else:
        return name


def get_name_by_id_from_table(table, id):
    name = ""
    for item in table:
        if item[0] == id:
            name = item[1]
    if name == "":
        return None
    else:
        return name
