

def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     | type    |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """
    longest_string = ""
    for i in range(len(table)):
        for k in table[i]:
            if len(k) > len(longest_string):
                longest_string = k
    longest_string = len(longest_string)
    print("/" + "- " * (longest_string * len(table[0])) + "\\")
    print("|", end='')
    for i in title_list:
        multiply = int((longest_string - len(i)) // 2)
        print(multiply * " " + i + multiply * " " + "|", end="")
    print("\n|", end="")
    for i in range(len(table)):
        for k in table[i]:
            multiply = int((longest_string - len(k)) // 2)
            print(multiply * " " + k + multiply * " " + "|", end='')
        print("\n|", end="")
    print("\\" + "- " * (longest_string * len(table[0])) + "/")


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """
    print(result)
    print(label)


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print(title)
    for i in range(1, len(list_options) + 1):
        print("\t (" + str(i) + ")", list_options[i - 1])
    print("\t (0)", exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    print(title)
    for i in range(1, len(list_labels) + 1):
        print(list_labels[i - 1] + " : ", end="")
        temp_var = input()
        inputs.append(temp_var)

    return inputs


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print(message)
