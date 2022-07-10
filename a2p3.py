#########################
# Author: Zouber Ismail
# Assignment 2 Problem 1
# Date july 8 2022
#########################

import pdb

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
    length = len(products)+1
    for x in range(length):
        if x == len(products):
            menu += str(x+1)+". " + "Complete Order\n"
        else:
            menu += str(x+1)+". " + products[x][0] + " ($"+str(products[x][1])+", "+ str(products[x][2])+ " in stock"   +")"+"\n"
        
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
    if 0 < selection <= len(products)+1:
        return True
    print("Im Sorry, thats not a Valid selection. Please Enter a selection from 1-4\n")
    return False
def remove_inventory(item_index, products, num_items):
    if num_items <= products[item_index][2]:
        #products[item_index][2] -= num_items
        products[item_index] = (products[item_index][0], products[item_index][1], products[item_index][2] - num_items)
        return True
    print(f"Sorry, we don't have that many {products[item_index][0]}")
    return False
def get_num_product(products, selection):
    """
    Get the number of a product, identified by the selection number, requested by the customer
    Args: 
        - List[Tuple(str, int)], list of pairs of product names and prices
        - int, selection number
    Returns: int, number of products requested by customer

    """
    #pdb.set_trace()
    is_valid = False
    while not is_valid:
        num_item = int(input("How many "+  products[selection-1][0]+"s would you like to purchase? "))
        is_valid = num_item > 0

        if not is_valid:
            print("Please enter a value greater than or equal to 0")
    return num_item

def display_receipt(cust_name, cart, products):
    """
    Display and prints customer receipt
    Args: 
        - str, customer name
        - int, number of products requested
        - str, product name
        - int, product price 
    Returns: None

    """

    order = ""
    cost = 0
    for i in cart:
        order += "\t"+str(cart[i]) + " "+ products[i][0]+"\n"
        cost += products[i][1]*cart[i]
    

    
    receipt = \
    f"""
    {cust_name}, here is your receipt: 
    -----------------------------------
    {order}
    -----------------------------------
    Total cost: ${cost:.2f}
    Thank you, Have a nice day!
    """

    print(receipt)


def add_to_cart(cart,num_items,item_index,products):
    if item_index in cart:
            cart[item_index] += num_items
            
    else:
        cart[item_index] = num_items
    
def start_store(products):
    """
    Starts the store interface
    Args: 
        - List[Tuple(str, int)], list of pairs of product names and prices
    Returns: None

    """
    is_valid = False
    selection = 0
    cart = {}
    name = get_name()

    while selection < len(products)+1:
        while not is_valid:
            disp_menu(products)
            selection = get_selection()
            is_valid = is_select_valid(products, selection)

        if selection == len(products)+1:
            continue
        #pdb.set_trace()
        num_item = get_num_product(products,selection)

        is_add = remove_inventory(selection-1, products, num_item)  
        if is_add:
            add_to_cart(cart,num_item,selection-1,products) 
        is_valid = False


    display_receipt(name, cart,products)

if __name__ == "__main__":
    products = [
        ("Desktop Computer",850, 15), 
        ("LAPTOP COMPUTER", 1225, 15),
        ("Tablet", 600, 15),
        ("Toaster Oven", 85, 15)
    ]
    start_store(products) 