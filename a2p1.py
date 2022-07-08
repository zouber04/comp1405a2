#########################
# Author: Zouber Ismail
# Assignment 2 Problem 1
# Date july 8 2022
#########################

def get_name():
    """
    Gets customer name
    Args: None
    Returns: String, customer name

    """
    name = input("Name: ")
    return name

def disp_menu(products):
    """
    Displays and prints menu
    Args: 
        - List[Tuple(str, int)], list of pairs of product names and prices
    Returns: None

    """
    menu = ""
    for x in range(len(products)):
        menu += str(x+1)+". " + products[x][0] + " ($"+str(products[x][1])+")"+"\n"
    print(menu)


def get_selection():
    """
    Request item selection number from customer
    Args: None
    Returns: int, selection number

    """
    selection = int(input("> "))
    return selection

def is_select_valid(products, selection):
    """
    Validates customer selection
    Args:
        - List[Tuple(str, int)], list of pairs of product names and prices
        - int, selection number
    Returns: bool, describes wether selection number is valid

    """
    if 0 < selection <= len(products):
        return True
    print("Im Sorry, thats not a Valid selection. Please Enter a selection from 1-4\n")
    return False

def get_num_product(products, selection):
    """
    Get the number of a product, identified by the selection number, requested by the customer
    Args: 
        - List[Tuple(str, int)], list of pairs of product names and prices
        - int, selection number
    Returns: int, number of products requested by customer

    """
    is_valid = False
    while not is_valid:
        num = int(input("How many "+  products[selection-1][0]+"s would you like to purchase? "))
        is_valid = num > 0

        if not is_valid:
            print("Please enter a value greater than or equal to 0")
    return num

def display_receipt(cust_name, num_product, product_name, product_price):
    """
    Display and prints customer receipt
    Args: 
        - str, customer name
        - int, number of products requested
        - str, product name
        - int, product price 
    Returns: None

    """
    
    receipt = \
    f"""
    {cust_name}, here is your receipt: 
    -----------------------------------
    {num_product} {product_name}{"" if num_product == 1 else "s"}
    -----------------------------------
    Total cost: ${product_price*num_product:.2f}
    Thank you, Have a nice day!
    """

    print(receipt)

def start_store(products):
    """
    Starts the store interface
    Args: 
        - List[Tuple(str, int)], list of pairs of product names and prices
    Returns: None

    """
    is_valid = False
    name = get_name()

    while not is_valid:
        disp_menu(products)
        selection = get_selection()
        is_valid = is_select_valid(products, selection)

    num = get_num_product(products,selection) 
    display_receipt(name, num, products[selection-1][0],products[selection-1][1])

if __name__ == "__main__":
    products = [
        ("Desktop Computer",850), 
        ("LAPTOP COMPUTER", 1225),
        ("Tablet", 600),
        ("Toaster Oven", 85)
    ]
    start_store(products)