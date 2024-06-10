from models.category import Category
from models.product import Product
from colorama import init, Fore, Style

init(autoreset=True)

def exit_program():
    print(Fore.RED + "Goodbye!")
    exit()

# Category functions

def list_categories():
    categories = Category.get_all()
    for category in categories:
        print(Fore.GREEN + str(category))

def find_category_by_name():
    name = input("Enter the category's name: ")
    category = Category.find_by_name(name)
    if category:
        print(Fore.GREEN + str(category))
    else:
        print(Fore.RED + f'Category {name} not found')

def find_category_by_id():
    id_ = input("Enter the category's id: ")
    category = Category.find_by_id(id_)
    if category:
        print(Fore.GREEN + str(category))
    else:
        print(Fore.RED + f'Category {id_} not found')

def create_category():
    name = input("Enter the category's name: ")
    description = input("Enter the category's description: ")
    try:
        category = Category.create(name, description)
        print(Fore.GREEN + f'Success: {category}')
    except Exception as exc:
        print(Fore.RED + "Error creating category: ", exc)

def update_category():
    id_ = input("Enter the category's id: ")
    category = Category.find_by_id(id_)
    if category:
        try:
            name = input("Enter the category's new name: ")
            description = input("Enter the category's new description: ")
            category.name = name
            category.description = description
            category.update()
            print(Fore.GREEN + f'Success: {category}')
        except Exception as exc:
            print(Fore.RED + "Error updating category: ", exc)
    else:
        print(Fore.RED + f'Category {id_} not found')

def delete_category():
    id_ = input("Enter the category's id: ")
    category = Category.find_by_id(id_)
    if category:
        category.delete()
        print(Fore.GREEN + f'Category {id_} deleted')
    else:
        print(Fore.RED + f'Category {id_} not found')

# Product functions

def list_products():
    products = Product.get_all()
    for product in products:
        print(Fore.CYAN + str(product))

def find_product_by_name():
    name = input("Enter the product's name: ")
    product = Product.find_by_name(name)
    if product:
        print(Fore.CYAN + str(product))
    else:
        print(Fore.RED + f'Product {name} not found')

def find_product_by_id():
    id_ = input("Enter the product's id: ")
    product = Product.find_by_id(id_)
    if product:
        print(Fore.CYAN + str(product))
    else:
        print(Fore.RED + f'Product {id_} not found')

def create_product():
    name = input("Enter the product's name: ")
    price = float(input("Enter the product's price: "))
    category_id = int(input("Enter the product's category id: "))
    try:
        product = Product.create(name, price, category_id)
        print(Fore.CYAN + f'Success: {product}')
    except Exception as exc:
        print(Fore.RED + "Error creating product: ", exc)

def update_product():
    id_ = input("Enter the product's id: ")
    product = Product.find_by_id(id_)
    if product:
        try:
            name = input("Enter the product's new name: ")
            price = float(input("Enter the product's new price: "))
            category_id = int(input("Enter the product's new category id: "))
            product.name = name
            product.price = price
            product.category_id = category_id
            product.update()
            print(Fore.CYAN + f'Success: {product}')
        except Exception as exc:
            print(Fore.RED + "Error updating product: ", exc)
    else:
        print(Fore.RED + f'Product {id_} not found')

def delete_product():
    id_ = input("Enter the product's id: ")
    product = Product.find_by_id(id_)
    if product:
        product.delete()
        print(Fore.CYAN + f'Product {id_} deleted')
    else:
        print(Fore.RED + f'Product {id_} not found')
