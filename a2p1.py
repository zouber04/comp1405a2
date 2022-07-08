###################
# Author: Zouber Ismail
# Assignment 2 Problem 1
# Date july 8 2022

def get_name():
    """
    Args:
        -
    Returns: String, customer name
    """
    name = input("Name: ")
    return name

def disp_menu(products):
    """
    Args: tuple of product name and price
        -
    Returns: String, menu
    """
    menu = ""
    for x in range(len(products)):
        menu += str(x+1)+". " + products[x][0] + " ($"+str(products[x][1])+")"+"\n"

    print(menu)

def get_product(products, selection):
     """
    Args: Integer, selection
        -
    Returns: String,
    """
def get_selection():

    selection = int(input("> "))
    return selection
def is_select_valid(products, selection):
    """
    Args: Integer, selection
        -
    Returns: Boolean

    """


    if(0 < selection <= len(products)):
        return True

    else:
        print("Im Sorry, thats not a Valid selection. Please Enter a selection from 1-4\n")
        
        return False



def get_num_product(products, selection):
    """
    Args: 
        -
    Returns: Integer, Number of products
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
    Args: String, Product Integer, Number of product Intege, Cost
        -
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
    Args: list of tuples of products
        -
    Returns: 
    """
    name = get_name()
    disp_menu(products)
    

    selection = get_selection()
    is_valid = is_select_valid(products,selection)

    while is_valid == False:
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