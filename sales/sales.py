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
menu_list = ["title:", "price:", "month:", "day:", "year:", "customer_id"]


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    ui.print_menu("Sales", ["show_table", "add", "remove", "update",
                            "lowest price item", "get item between date"], "Go back to main menu")
    menu_choose_list = ui.get_inputs(["Choose: "], "")
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
        ui.print_result(get_lowest_price_item_id(the_list), "was sold for the lowest price")
        start_module()
    elif menu_choose == 6:
        dates = ui.get_inputs(["month from", "day from", "year from", "month to", "day to",
                               "year to"], "enter -date from and -date to want to observ")
        ui.print_result(get_items_sold_between(
            the_list, dates[0], dates[1], dates[2], dates[3], dates[4], dates[5]), "item(s) between the 2 given date")
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

    while True:
        returnable_list = common.common_add(table, menu_list)

        if (returnable_list[-1][1]).isdigit() == False and \
            (returnable_list[-1][2]).isdigit() and \
            (returnable_list[-1][3]).isdigit() and \
            int((returnable_list[-1][3])) > 0 and \
            int((returnable_list[-1][3])) < 13 and \
            (returnable_list[-1][4]).isdigit() and\
            int((returnable_list[-1][4])) > 0 and \
            int((returnable_list[-1][4])) < 32 and \
            (returnable_list[-1][5]).isdigit() and \
            int((returnable_list[-1][5])) < 3000 and \
                int((returnable_list[-1][5])) > 0:
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
            (comparable_list[2]).isdigit() and \
            (comparable_list[3]).isdigit() and \
            int((comparable_list[3])) > 0 and \
            int((comparable_list[3])) < 13 and \
            (comparable_list[4]).isdigit() and\
            int((comparable_list[4])) > 0 and \
            int((comparable_list[4])) < 32 and \
            (comparable_list[5]).isdigit() and \
            int((comparable_list[5])) < 3000 and \
                int((comparable_list[5])) > 0:
            return returnable_list
        else:
            ui.print_error_message("\nYou entered wrong inputs\n")


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    prices = []
    name_list = []
    for line in table:
        prices.append(line[2])
    min_price = min(prices)
    for line in table:
        if min_price in line:
            name_list.append(line[1])
    name = min(name_list)
    for line in table:
        if name in line:
            return line[0]


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    returnable_list = []
    datefrom = int(str(year_from) + str(month_from) + str(day_from))
    dateto = int(str(year_to) + str(month_to) + str(day_to))
    for line in table:
        date = int(str(line[5]) + str(line[3]) + str(line[4]))
        if date > datefrom and date < dateto:
            returnable_list.append(line)
    return returnable_list

# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str the title of the item
    """
    the_list = data_manager.get_table_from_file("sales/sales.csv")
    for line in the_list:
        if line[0] == id:
            return line[1]


def get_title_by_id_from_table(table, id):
    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str the title of the item
    """
    for line in table:
        if line[0] == id:
            return line[1]


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    the_list = data_manager.get_table_from_file("sales/sales.csv")
    dates_id = []
    date = []
    date_lst = []
    for line in the_list:
        date = int(str(line[5]) + str(line[3]) + str(line[4]))
        date_id = [date, line[0]]
        dates_id.append(date_id)
    for item in dates_id:
        date_lst.append(item[0])
    for item in dates_id:
        if max(date_lst) in item:
            return item[1]


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """
    dates_id = []
    date = []
    date_lst = []
    for line in table:
        date = int(str(line[5]) + str(line[3]) + str(line[4]))
        date_id = [date, line[0]]
        dates_id.append(date_id)
    for item in dates_id:
        date_lst.append(item[0])
    for item in dates_id:
        if max(date_lst) in item:
            return item[1]


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _title_ of the item that was sold most recently.
    """

    dates = []
    date = []
    for line in table:
        date = int(str(line[5]) + str(line[3]) + str(line[4]))
        dates_id.append(date, line[1])
    for item in dates_id:
        date.append(item[0])
    for item in dates_id:
        if max(date) in item:
            return item[1]


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """
    the_list = data_manager.get_table_from_file("sales/sales.csv")
    summa = 0
    for item in item_ids:
        for line in the_list:
            if item == line[0]:
                summa += int(line[2])
    return summa


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """
    summa = 0
    for item in item_ids:
        for line in table:
            if item == line[0]:
                summa += int(line[2])
    return summa


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
         sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """

    the_list = data_manager.get_table_from_file("sales/sales.csv")
    customer_id = ""
    for line in the_list:
        if sale_id in line:
            customer_id = line[6]
    if customer_id == "":
        return None
    else:
        return customer_id


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """
    customer_id = ""
    for line in table:
        if sale_id in line:
            customer_id = line[6]
    if customer_id == "":
        return None
    else:
        return customer_id


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.
    Returns a set of customer_ids that are present in the table.
    Returns:
         set of customer_ids that are present in the table
    """

    the_list = data_manager.get_table_from_file("sales/sales.csv")
    ids = []
    for line in the_list:
        ids.append(line[6])
    return set(ids)


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.
    Args:
        table (list of list): the sales table
    Returns:
         set of customer_ids that are present in the table
    """
    ids = []
    for line in table:
        ids.append(line[6])
    return set(ids)


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    the_list = data_manager.get_table_from_file("sales/sales.csv")
    my_dict = {}
    for i in range(len(the_list)):
        if the_list[i][6] not in my_dict:
            my_dict[the_list[i][6]] = [the_list[i][0]]
        else:
            my_dict[the_list[i][6]].append(the_list[i][0])
    return my_dict


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """
    for i in range(len(table)):
        if the_list[i][6] not in my_dict:
            my_dict[the_list[i][6]] = [the_list[i][0]]
        else:
            my_dict[the_list[i][6]].append(the_list[i][0])
    return my_dict


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    the_list = data_manager.get_table_from_file("sales/sales.csv")
    my_list = []
    my_count = {}
    sum_ids = 0
    for line in the_list:
        my_list.append(line[6])
    for item in my_list:
        if item in my_count:
            my_count[item] += 1
        else:
            my_count[item] = 1
    return my_count


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """
    my_list = []
    my_count = {}
    sum_ids = 0
    for line in table:
        my_list.append(line[6])
    for item in my_list:
        if item in my_count:
            my_count[item] += 1
        else:
            my_count[item] = 1
    return my_count
