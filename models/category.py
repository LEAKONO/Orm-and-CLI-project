from models import CONN, CURSOR

class Category:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f'Category(id={self.id}, name={self.name}, description={self.description})'

    @classmethod
    def create_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT
        )''')
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE IF EXISTS categories')
        CONN.commit()

    @classmethod
    def create(cls, name, description):
        CURSOR.execute('INSERT INTO categories (name, description) VALUES (?, ?)', (name, description))
        CONN.commit()
        return cls(CURSOR.lastrowid, name, description)

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM categories')
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute('SELECT * FROM categories WHERE name = ?', (name,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_id(cls, id_):
        CURSOR.execute('SELECT * FROM categories WHERE id = ?', (id_,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    def update(self):
        CURSOR.execute('UPDATE categories SET name = ?, description = ? WHERE id = ?', (self.name, self.description, self.id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM categories WHERE id = ?', (self.id,))
        CONN.commit()

    def products(self):
        """Return list of products associated with current category"""
        from models.Product import Product
        sql = """
            SELECT * FROM products
            WHERE category_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Product(*row) for row in rows
        ]
