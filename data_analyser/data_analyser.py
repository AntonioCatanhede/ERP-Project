# This module creates reports for marketing department.
# This module can run independently from other modules.
# Has no own datastructure but uses other modules.
# Avoud using the database (ie. .csv files) of other modules directly.
# Use the functions of the modules instead.

# todo: importing everything you need

# importing everything you need
import os
import ui
import common
import data_manager
from sales import sales
from crm import crm


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    ui.print_menu(
        "Data analyser", ["Last buyer name", "Last buyer id", "Name of the most money spent", "Id of the most money spent",
                          "Name of the most frequent buyer(s)", "Id of the most frequent buyer(s)"], "Go back to main menu")
    menu_choose_list = ui.get_inputs(["Choose: "], "")
    menu_choose = int(menu_choose_list[0])
    if menu_choose == 1:
        ui.print_result(get_the_last_buyer_name(), "The last buyer's name: ")
        start_module()
    elif menu_choose == 2:
        ui.print_result(get_the_last_buyer_id(), "The last buyer's id: ")
        start_module()
    elif menu_choose == 3:
        ui.print_result(get_the_buyer_name_spent_most_and_the_money_spent(), "The customer who spent the most money: ")
        start_module()
    elif menu_choose == 4:
        ui.print_result(get_the_buyer_id_spent_most_and_the_money_spent(),
                        "The customer id  who spent the most money: ")
        start_module()
    elif menu_choose == 5:
        input_number = ui.get_inputs(["Number: "], "Number(s) of the last buyers(max 3): ")
        input_number = int(input_number[0])
        if input_number < 4 and input_number > 0:
            ui.print_result(get_the_most_frequent_buyers_names(input_number), "Name of the most frequent buyer(s)")
        else:
            ui.print_error_message("Incorrect input")
        start_module()
    elif menu_choose == 6:
        input_number = ui.get_inputs(["Number: "], "Id(s) of the last buyers(max 3): ")
        input_number = int(input_number[0])
        if input_number < 4 and input_number > 0:
            ui.print_result(get_the_most_frequent_buyers_ids(input_number), "Id of the most frequent buyer(s)")
        else:
            ui.print_error_message("Incorrect input")
        start_module()
    elif menu_choose == 0:
        return
    else:
        raise KeyError("There is no such options")


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        Customer name of the last buyer
    """

    temp_id = sales.get_item_id_sold_last()
    my_id = sales.get_customer_id_by_sale_id(temp_id)
    return crm.get_name_by_id(my_id)


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        Customer id of the last buyer
    """
    temp_id = sales.get_item_id_sold_last()
    return sales.get_customer_id_by_sale_id(temp_id)


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.
    Returns a tuple of customer name and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer name and the sum the customer spent
    """
    dictionary = sales.get_all_sales_ids_for_customer_ids()
    maxim = 0
    for i in dictionary:
        if sales.get_the_sum_of_prices(dictionary[i]) > maxim:
            maxim = sales.get_the_sum_of_prices(dictionary[i])
            max_id = i
    max_name = crm.get_name_by_id(max_id)
    return (max_name, maxim)


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.
    Returns a tuple of customer id and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer id and the sum the customer spent
    """

    dictionary = sales.get_all_sales_ids_for_customer_ids()
    maxim = 0
    for i in dictionary:
        if sales.get_the_sum_of_prices(dictionary[i]) > maxim:
            maxim = sales.get_the_sum_of_prices(dictionary[i])
            max_id = i
    return (max_id, maxim)


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customers' name) who bought most frequently.
    Returns an ordered list of tuples of customer names and the number of their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer names and num of sales
    """

    dict = sales.get_num_of_sales_per_customer_ids()
    my_lst = []
    for i in dict:
        name = crm.get_name_by_id(i)
        appendable = [name, dict[i]]
        my_lst.append(appendable)
    my_lst.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(my_lst)):
        my_lst[i] = tuple(my_lst[i])
    return my_lst[0:num]


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent.
    Returns an ordered list of tuples of customer id and the number their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer ids and num of sales
    """
    dict = sales.get_num_of_sales_per_customer_ids()
    my_lst = []
    for i in dict:
        appendable = [i, dict[i]]
        my_lst.append(appendable)
    my_lst.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(my_lst)):
        my_lst[i] = tuple(my_lst[i])
    return my_lst[0:num]


def get_customer_who_did_not_buy_anything():
    return
