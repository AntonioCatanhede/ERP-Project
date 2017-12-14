import os
import ui
import data_manager
import common

e_mail = "semmiertelme13@gmail.com"
Login = False
the_list = data_manager.get_table_from_file("inventory/inventory.csv")
menu_list = ["name:", "manufacturer:", "purchase_date:", "durability:"]


def start_module():
    while True:
        users = data_manager.get_table_from_file("inventory/password.csv")
        ui.print_menu("Inventory", ["show_table", "add", "remove", "update", "login", "avaliable items",
                                    "average durability by manufacturers"], "Go back to main menu")
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
                common.new_password_request(Logged, users, "inventory/password.csv")
        elif menu_choose == 6:
            os.system('clear')
            ui.print_result(get_available_items(the_list), "Avaible items: ")
        elif menu_choose == 7:
            os.system('clear')
            ui.print_result(get_average_durability_by_manufacturers(the_list), "The avarage durability: ")
        elif menu_choose == 0:
            os.system('clear')
            if ui.get_inputs(["Please enter yes or no: "], "Do you want to save your changes? ")[0] == "yes":
                data_manager.write_table_to_file("inventory/inventory.csv", the_list)
            return
        else:
            raise KeyError("There is no such options")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    menu_list.insert(0, "id")
    ui.print_table(table, menu_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    while True:
        returnable_list = common.common_add(table, menu_list)

        if (returnable_list[-1][1]).isdigit() == False and \
            (returnable_list[-1][2]).isdigit() == False and \
            (returnable_list[-1][3]).isdigit() and \
                (returnable_list[-1][4]).isdigit():
            return returnable_list
        else:
            the_list.remove(the_list[-1])
            ui.print_error_message("\nYou entered wrong inputs\n")


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """
    return common.common_remove(table, id_)


def update(table, list, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """
    while True:
        returnable_list = common.common_update(table, list, id_)

        for item in returnable_list:
            if id_ in item:
                comparable_list = item

        if (comparable_list[1]).isdigit() == False and \
            (comparable_list[2]).isdigit() == False and \
            (comparable_list[3]).isdigit() and \
                (comparable_list[4]).isdigit():
            return comparable_list
        else:
            ui.print_error_message("\nYou entered wrong inputs\n")


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):

    avaliable_items = []
    one_line = []
    for line in table:
        if int(line[3]) + int(line[4]) >= 2017:
            for item in line:
                one_line.append(item)
            avaliable_items.append(one_line)
    for i in range(len(avaliable_items)):
        avaliable_items[i] = avaliable_items[i][0:5]
    for line in range(len(avaliable_items)):
        avaliable_items[line][3] = int(avaliable_items[line][3])
        avaliable_items[line][4] = int(avaliable_items[line][4])
    return avaliable_items


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    manufacturers_set = set()
    returnable_dict = {}
    for line in table:
        manufacturers_set.add(line[2])

    for manufacturer in manufacturers_set:
        counter = 0
        sum_num = 0
        for line in table:
            if manufacturer in line:
                counter += 1
                sum_num += int(line[4])
        returnable_dict[manufacturer] = sum_num / counter
    return returnable_dict
