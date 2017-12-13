# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

e_mail = "semmiertelme13@gmail.com"
Login = False
the_list = data_manager.get_table_from_file("store/games.csv")
menu_list = ["title:", "manufacturer:", "price:", "in_stock:"]


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    while True:
        users = data_manager.get_table_from_file("store/password.csv")
        ui.print_menu("Store", ["show_table", "add", "remove", "update", "login",
                                "manufacturer count", "stock avarage"], "Go back to main menu")
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
                common.new_password_request(Logged, users, "strore/password.csv")
        elif menu_choose == 6:
            os.system('clear')
            ui.print_result(get_counts_by_manufacturers(the_list), "Games by manufacturer:")
        elif menu_choose == 7:
            os.system('clear')
            manufacturer_input = ui.get_inputs(["Enter a manufacturer name : "], "The avarage game in stock")
            manufacturer_input = manufacturer_input[0]
            ui.print_result(get_average_by_manufacturer(the_list, manufacturer_input), "The avarage games in stock:")
        elif menu_choose == 0:
            data_manager.write_table_to_file("store/games.csv", the_list)
            return


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
            return returnable_list
        else:
            ui.print_error_message("\nYou entered wrong inputs\n")


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    manufacturer_list = []
    manufacturer_count = {}
    for line in table:
        manufacturer_list.append(line[2])
    for manufacturers in manufacturer_list:
        if manufacturers in manufacturer_count:
            manufacturer_count[manufacturers] += 1
        else:
            manufacturer_count[manufacturers] = 1
    return manufacturer_count


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    average_list = []
    sum_items = 0
    for line in table:
        if manufacturer in line:
            average_list.append(line[4])
    for item in average_list:
        sum_items += int(item)
    if len(average_list) == 0:
        return("No item by the given manufacturer")
    else:
        average = sum_items / len(average_list)
    return average
