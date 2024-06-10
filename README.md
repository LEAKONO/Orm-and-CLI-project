# CLI Product and Category Management

This project is a simple command-line interface (CLI) application for managing products and categories in a database. It allows you to create, read, update, and delete categories and products.

## Features

- Create, list, find, update, and delete categories
- Create, list, find, update, and delete products
- Products are associated with categories

## User Stories

1. **As a user, I want to create a new category, so that I can organize my products.**
2. **As a user, I want to list all categories, so that I can see what categories are available.**
3. **As a user, I want to find a category by name, so that I can quickly locate a specific category.**
4. **As a user, I want to find a category by ID, so that I can quickly locate a specific category using its unique identifier.**
5. **As a user, I want to update a category, so that I can change its name or description.**
6. **As a user, I want to delete a category, so that I can remove categories I no longer need.**
7. **As a user, I want to create a new product, so that I can add new items to my inventory.**
8. **As a user, I want to list all products, so that I can see what products are available.**
9. **As a user, I want to find a product by name, so that I can quickly locate a specific product.**
10. **As a user, I want to find a product by ID, so that I can quickly locate a specific product using its unique identifier.**
11. **As a user, I want to update a product, so that I can change its name, price, or associated category.**
12. **As a user, I want to delete a product, so that I can remove products I no longer need.**

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/LEAKONO/Orm-and-CLI-project
    cd Orm and CLI-project
    ```
## Usage

1. Seed the database with initial data:
    ```bash
    python seed.py
    ```

2. Run the CLI application:
    ```bash
    python cli.py
    ```

3. Follow the on-screen instructions to manage categories and products.

### Example: Create a New Category

To create a new category, run the CLI application and select the option to create a category:

```bash
python cli.py

Please select an option:
0. Exit the program
1. List all categories
2. Find category by name
3. Find category by id
4. Create category
5. Update category
6. Delete category
7. List all products
8. Find product by name
9. Find product by id
10. Create product
11. Update product
12. Delete product
> 4
Enter the category's name: Electronics
Enter the category's description: Devices and gadgets.

