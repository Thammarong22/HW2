product_list = {} 

def add_product(product_list, product_name, product_quantity): 
    product_name = input("Enter Product Name: ")
    product_quantity = input("Enter Product Quantity: ")
    if product_name in product_list:
        product_list[product_name] += product_quantity
    else:
        product_list[product_name] = product_quantity
 
def show_products(product_list): 
    for key in product_list.keys():
        print(key + " : " + str(product_list[key]))
 
add_product(product_list, "Snack", 10)
add_product(product_list, "Drink", 20)
add_product(product_list, "Snack", 10)
show_products(product_list)
 