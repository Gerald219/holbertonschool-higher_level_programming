#!/usr/bin/python3
"""small helper to create products sqlite db"""

import os
import sqlite3


def create_database():
    """make products.db with a simple products table"""
    db_path = os.path.join(os.path.dirname(__file__), "products.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    # only seed when table is empty
    cursor.execute("SELECT COUNT(*) FROM Products")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany(
            "INSERT INTO Products (id, name, category, price) VALUES (?, ?, ?, ?)",
            [
                (1, "Laptop", "Electronics", 799.99),
                (2, "Coffee Mug", "Home Goods", 15.99),
            ],
        )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
