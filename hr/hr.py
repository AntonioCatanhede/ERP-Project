import os
import ui
import data_manager
import common

e_mail = "semmiertelme13@gmail.com"
Login = False
the_list = data_manager.get_table_from_file("hr/persons.csv")
menu_list = ["name:", "birth_date:"]


def start_module():
    while True:
        users = data_manager.get_table_from_file("hr/password.csv")
        ui.print_menu("Accounting", ["show_table", "add", "remove", "update", "login",
                                     "most profitable year", "avarage amount"], "Go back to main menu")
        menu_choose_list = ui.get_inputs(["Choose: "], "")
        menu_choose = int(menu_choose_list[0])
        if menu_choose == 1:
            os.system('cls')
            show_table(the_list)
            menu_list.remove("id")
            ui.get_inputs(["Press a button: "], "")
            os.system('cls')
        elif menu_choose == 2:
            os.system('cls')
            try:
                if Login:
                    add(the_list)
            except NameError:
                ui.print_error_message("\nYou don't have permission to do that!\nPlease login first!\n")
        elif menu_choose == 3:
            os.system('cls')
            try:
                if Login:
                    show_table(the_list)
                    menu_list.remove("id")
                    id = ui.get_inputs(["ID: "], "Please enter an id: ")
                    id = id[0]
            except NameError:
                ui.print_error_message("\nYou don't have permission to do that!\nPlease login first!\n")
        elif menu_choose == 4:
            os.system('cls')
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
            os.system('cls')
            Logged = common.username_pass(users, e_mail)
            if Logged == True:
                print("You logged in succesfully.")
                Login = True
            else:
                common.new_password_request(Logged, users, "hr/password.csv")
        elif menu_choose == 6:
            os.system('cls')
            ui.print_result(get_oldest_person(the_list), "The oldest persons : ")
        elif menu_choose == 7:
            os.system('cls')
            ui.print_result(get_persons_closest_to_average(the_list), "The closest to the average age : ")
        elif menu_choose == 0:
            os.system('cls')
            data_manager.write_table_to_file("hr/persons.csv", the_list)
            return
        else:
            raise KeyError("There is no such options")


def show_table(table):
    menu_list.insert(0, "id")
    ui.print_table(table, menu_list)


def add(table):
    while True:
        returnable_list = common.common_add(table, menu_list)

        if (returnable_list[-1][1]).isdigit() == False and (returnable_list[-1][2]).isdigit():
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

        if (comparable_list[1]).isdigit() == False and (comparable_list[2]).isdigit():
            return returnable_list
        else:
            ui.print_error_message("\nYou entered wrong inputs\n")


def get_oldest_person(table):

    oldest_person_list = []
    oldest_names = []
    for i in table:
        oldest_person_list.append(i[2])
    oldest_person_age = min(oldest_person_list)
    for i in table:
        if oldest_person_age in i:
            oldest_names.append(i[1])
    if len(oldest_names) == 1:
        ui.print_result(oldest_names[0], "The oldest person is : ")
    else:
        return oldest_names


def get_persons_closest_to_average(table):

    list1 = []
    ages = []
    sum_ages = 0
    minimum = 100
    avarage_list = []
    for line in table:
        sum_ages += int(line[2])
    avg = sum_ages / len(table)
    for line in table:
        list1.append([line[2], line[1]])
    for i in range(len(list1)):
        list1[i][0] = (abs(float(list1[i][0]) - avg))
    for i in range(len(list1)):
        if float(list1[i][0]) < minimum:
            minimum = float(list1[i][0])
    for line in list1:
        if minimum in line:
            avarage_list.append(line[1])
    return avarage_list
