import os
import ui
import data_manager
import common
e_mail = "semmiertelme13@gmail.com"
the_list = data_manager.get_table_from_file("accounting/items.csv")
menu_list = ["month:", "day:", "year:", "type:", "amount:"]
Login = False


def start_module():
    while True:
        users = data_manager.get_table_from_file("accounting/password.csv")
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
                    id = ui.get_inputs(["ID: "], "Please enter an id: ")
                    id = id[0]
            except NameError:
                ui.print_error_message("\nYou don't have permission to do that!\nPlease login first!\n")
        elif menu_choose == 4:
            os.system('cls')
            try:
                if Login:
                    show_table(the_list)
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
                common.new_password_request(Logged, users, "accounting/password.csv")
        elif menu_choose == 6:
            os.system('cls')
            which_year_max(the_list)
            ui.print_result(which_year_max(the_list), "The year is:")
        elif menu_choose == 7:
            os.system('cls')
            year_input = ui.get_inputs(["Enter the year: "], "")
            year_input = year_input[0]
            ui.print_result(avg_amount(the_list, year_input), "The avarage is:")
        elif menu_choose == 0:
            os.system('cls')
            data_manager.write_table_to_file("accounting/items.csv", the_list)
            return
        else:
            raise KeyError("There is no such options")


def show_table(table):
    menu_list.insert(0, "id")
    ui.print_table(table, menu_list)
    remove(table, id)


def add(table):
    while True:
        returnable_list = common.common_add(table, menu_list)

        if (returnable_list[-1][1]).isdigit() and \
            (returnable_list[-1][5]).isdigit() and \
            (returnable_list[-1][4]) == "in" or (returnable_list[-1][4]) == "out" and \
            int((returnable_list[-1][1])) > 0 and \
            int((returnable_list[-1][1])) < 13 and \
            (returnable_list[-1][2]).isdigit() and \
            int((returnable_list[-1][2])) > 0 and \
            int((returnable_list[-1][2])) < 32 and \
            (returnable_list[-1][3]).isdigit() and \
            int((returnable_list[-1][3])) < 3000 and \
                int((returnable_list[-1][3])) > 0:
            return returnable_list
        else:
            the_list.remove(the_list[-1])
            ui.print_error_message("\nYou enteWred wrong inputs\n")


def remove(table, id_):
    return common.common_remove(table, id_)


def update(table, list, id_):
    while True:
        returnable_list = common.common_update(table, list, id_)

        for item in returnable_list:
            if id_ in item:
                comparable_list = item

        if (comparable_list[1]).isdigit() and \
            (comparable_list[5]).isdigit() and \
            (comparable_list[4]) == "in" or (comparable_list[4]) == "out" and \
            int((comparable_list[1])) > 0 and \
            int((comparable_list[1])) < 13 and \
            (comparable_list[2]).isdigit() and \
            int((comparable_list[2])) > 0 and \
            int((comparable_list[2])) < 32 and \
            (comparable_list[3]).isdigit() and \
            int((comparable_list[3])) < 3000 and \
                int((comparable_list[3])) > 0:
            return returnable_list
        else:
            ui.print_error_message("\nYou entered wrong inputs\n")


def which_year_max(table):

    year_set = set()
    year_profit = {}

    for line in table:
        year_set.add(line[3])

    for year in year_set:
        in_sum = 0
        out_sum = 0
        for line in table:
            if year in line:
                if "in" in line:
                    in_sum += int(line[5])
                elif "out" in line:
                    out_sum += int(line[5])
        year_profit[int(year)] = in_sum - out_sum
    maximum = max(year_profit.values())
    for i in year_profit:
        if year_profit[i] == max(year_profit.values()):
            return int(i)


def avg_amount(table, year):

    in_sum = 0
    out_sum = 0
    item_count = 0
    for line in table:
        if str(year) in line:
            if "in" in line:
                in_sum += int(line[5])
                item_count += 1
            elif "out" in line:
                out_sum += int(line[5])
                item_count += 1
    if item_count == 0:
        return("No item in the given year")
    else:
        result_avg = (in_sum - out_sum) / item_count
        return result_avg
