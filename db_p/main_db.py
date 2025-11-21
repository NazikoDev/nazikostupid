import sqlite3
from db_p import queries
from config import path_db

def init_db():
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.CREATE_SHOPPING)

def add_shop(name_stuf):
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.INSERT_STUF, (name_stuf,))
        return cursor.lastrowid

def get_shops(filter_type="all"):
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        if filter_type == "completed":
            cursor.execute(queries.SELECT_COMPLETED)
        elif filter_type == "active":
            cursor.execute(queries.SELECT_ACTIVE)
        else:
            cursor.execute(queries.SELECT_ALL)
        return cursor.fetchall()

def set_completed(item_id, completed):
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.UPDATE_COMPLETED, (completed, item_id))

def delete_shop(item_id):
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.DELETE_STUF, (item_id,))
