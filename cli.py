from helpers import (
    exit_program,
    list_categories,
    find_category_by_name,
    find_category_by_id,
    create_category,
    update_category,
    delete_category,
    list_products,
    find_product_by_name,
    find_product_by_id,
    create_product,
    update_product,
    delete_product
)
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_categories()
        elif choice == "2":
            find_category_by_name()
        elif choice == "3":
            find_category_by_id()
        elif choice == "4":
            create_category()
        elif choice == "5":
            update_category()
        elif choice == "6":
            delete_category()
        elif choice == "7":
            list_products()
        elif choice == "8":
            find_product_by_name()
        elif choice == "9":
            find_product_by_id()
        elif choice == "10":
            create_product()
        elif choice == "11":
            update_product()
        elif choice == "12":
            delete_product()
        else:
            print(Fore.RED + "Invalid choice")

def menu():
    print(Fore.YELLOW + "Please select an option:")
    print("0. Exit the program")
    print("1. List all categories")
    print("2. Find category by name")
    print("3. Find category by id")
    print("4. Create category")
    print("5. Update category")
    print("6. Delete category")
    print("7. List all products")
    print("8. Find product by name")
    print("9. Find product by id")
    print("10. Create product")
    print("11. Update product")
    print("12. Delete product")

if __name__ == "__main__":
    main()
