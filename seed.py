#!/usr/bin/env python3

from models import CONN, CURSOR
from models.category import Category
from models.product import Product

def seed_database():
    Product.drop_table()
    Category.drop_table()
    Category.create_table()
    Product.create_table()

    # Create seed data
    electronics = Category.create("Electronics", "Devices and gadgets")
    clothing = Category.create("Clothing", "Apparel and accessories")
    groceries = Category.create("Groceries", "Food and beverages")

    Product.create("Smartphone", 699.99, electronics.id)
    Product.create("Laptop", 999.99, electronics.id)
    Product.create("Jeans", 49.99, clothing.id)
    Product.create("T-Shirt", 19.99, clothing.id)
    Product.create("Apple", 0.99, groceries.id)
    Product.create("Bread", 2.49, groceries.id)

seed_database()
print("Seeded database")

