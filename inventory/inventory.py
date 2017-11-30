# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

the_list = data_manager.get_table_from_file("inventory/inventory.csv")
menu_list = ["name:", "manufacturer:", "purchase_date:", "durability:"]


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    ui.print_menu("Inventory", ["show_table", "add", "remove", "update", "avaliable items",
                                "average durability by manufacturers"], "Go back to main menu")
    menu_choose = int(input("Please enter a number: "))
    if menu_choose == 1:
        show_table(the_list)
        menu_list.remove("id")
        start_module()
    elif menu_choose == 2:
        add(the_list)
        start_module()
    elif menu_choose == 3:
        id = ui.get_inputs(["ID: "], "Please enter an id: ")
        id = id[0]
        remove(the_list, id)
        start_module()
    elif menu_choose == 4:
        id = ui.get_inputs(["ID: "], "Please enter an id: ")
        id = id[0]
        update(the_list, menu_list, id)
        start_module()
    elif menu_choose == 5:
        print(get_available_items(the_list))
        start_module()
    elif menu_choose == 6:
        print(get_average_durability_by_manufacturers(the_list))
        start_module()
    elif menu_choose == 0:
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

    return common.common_add(table, menu_list)


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
    return common.common_update(table, list, id_)


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
        if (int(line[3]) + int(line[4])) >= 2017:
            for item in line:
                one_line.append(item)
            avaliable_items.append(one_line)
    for list in range(len(avaliable_items)):
        avaliable_items[list][3] = int(avaliable_items[list][3])
        avaliable_items[list][4] = int(avaliable_items[list][4])
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
