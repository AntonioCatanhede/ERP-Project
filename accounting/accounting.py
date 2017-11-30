# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

the_list = data_manager.get_table_from_file("accounting/items.csv")
menu_list = ["month:", "day:", "year:", "type:", "amount:"]


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.
    Returns:
        None
    """

    ui.print_menu("Accounting", ["show_table", "add", "remove", "update",
                                 "most profitable year", "avarage amount"], "Go back to main menu")
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
        print(which_year_max(the_list))
        start_module()
    elif menu_choose == 6:
        print(avg_amount(the_list, 2015))
        start_module()
    elif menu_choose == 0:
        data_manager.write_table_to_file("accounting/items.csv", the_list)
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

    # your code

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

    # your code

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

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
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
    print(year_profit)
    maximum = max(year_profit.values())
    for i in year_profit:
        if year_profit[i] == max(year_profit.values()):
            return int(i)


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
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

    return (in_sum - out_sum) / item_count
