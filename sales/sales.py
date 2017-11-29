# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

the_list = data_manager.get_table_from_file("sales/sales.csv")
menu_list = ["title:", "price:", "month:", "day:", "year:"]


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    ui.print_menu("Sales", ["show_table", "add", "remove", "update"], "Go back to main menu")
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
    elif menu_choose == 0:
        data_manager.write_table_to_file("sales/sales.csv", the_list)
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

    # your code

    return common.common_update(table, list, id_)


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):

    # your code

    pass


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass
