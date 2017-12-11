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

sales_list = data_manager.get_table_from_file("sales/sales.csv")
crm_list = data_manager.get_table_from_file("crm/customers.csv")


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
        "Data analyser", ["Last buyer name", "Last buyer id", "Name of the most spent", "Id of the most spent",
                          "Name of the most frequent buyers", "Id of the most frequent buyers"], "Go back to main menu")
    menu_choose_list = ui.get_inputs(["Choose: "], "")
    menu_choose = int(menu_choose_list[0])
    if menu_choose == 1:
        ui.print_result(get_the_last_buyer_name(sales_list,crm_list),"The last buyer's name: ")
        start_module()
    elif menu_choose == 2:
        ui.print_result(get_the_last_buyer_id(sales_list),"The last buyer's id: ")
        start_module()
    elif menu_choose == 3:
        get_the_buyer_name_spent_most_and_the_money_spent()
        start_module()
    elif menu_choose == 4:
        get_the_buyer_id_spent_most_and_the_money_spent()
        start_module()
    elif menu_choose == 5:
        get_the_most_frequent_buyers_names(num=1)
        start_module
    elif menu_choose == 6:
        get_the_most_frequent_buyers_ids(num=1)
        start_module()
    elif menu_choose == 0:
        return
    else:
        raise KeyError("There is no such options")


def get_the_last_buyer_name(lst1, lst2):
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        Customer name of the last buyer
    """

    temp_id = sales.get_item_id_sold_last_from_table(lst1)
    my_id=sales.get_customer_id_by_sale_id_from_table(lst1, temp_id)
    return crm.get_name_by_id_from_table(lst2, my_id)


def get_the_last_buyer_id(lst1):
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        Customer id of the last buyer
    """
    temp_id = sales.get_item_id_sold_last_from_table(lst1)
    return sales.get_customer_id_by_sale_id_from_table(lst1, temp_id)



def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.
    Returns a tuple of customer name and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer name and the sum the customer spent
    """

    # your code

    pass


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.
    Returns a tuple of customer id and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer id and the sum the customer spent
    """

    # your code

    pass


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

    # your code

    pass


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

    # your code

    pass

get_the_last_buyer_name(sales_list, crm_list)