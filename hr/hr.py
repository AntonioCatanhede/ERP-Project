# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

the_list = data_manager.get_table_from_file("hr/persons.csv")
menu_list = ["name:", "birth_date:"]


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    ui.print_menu("Human resources", ["show_table", "add", "remove", "update",
                                      "oldest person", "closest to the average age"], "Go back to main menu")
    menu_choose_list = ui.get_inputs(["Choose: "], "Please enter a number: ")
    menu_choose = int(menu_choose_list[0])
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
        ui.print_result(get_oldest_person(the_list), "The oldest persons : ")
        start_module()
    elif menu_choose == 6:
        ui.print_result(get_persons_closest_to_average(the_list), "The closest to the average age : ")
        start_module()
    elif menu_choose == 0:
        data_manager.write_table_to_file("hr/person.csv", the_list)
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

    # your code

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

    while True:
        returnable_list = common.common_add(table, menu_list)

        if (returnable_list[-1][1]).isdigit() == False and (returnable_list[-1][2]).isdigit():
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

    while True:
        returnable_list = common.common_update(table, list, id_)

        for item in returnable_list:
            if id_ in item:
                comparable_list = item

        if (comparable_list[1]).isdigit() == False and (comparable_list[2]).isdigit():
            return returnable_list
        else:
            ui.print_error_message("\nYou entered wrong inputs\n")


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
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


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
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
