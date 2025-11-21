CREATE_SHOPPING = """
CREATE TABLE IF NOT EXISTS Items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    completed INTEGER DEFAULT 0
);
"""

INSERT_STUF = "INSERT INTO Items (name, completed) VALUES (?, 0);"

SELECT_ALL = "SELECT id, name, completed FROM Items ORDER BY id DESC;"
SELECT_COMPLETED = "SELECT id, name, completed FROM Items WHERE completed = 1 ORDER BY id DESC;"
SELECT_ACTIVE = "SELECT id, name, completed FROM Items WHERE completed = 0 ORDER BY id DESC;"

UPDATE_COMPLETED = "UPDATE Items SET completed = ? WHERE id = ?;"
DELETE_STUF = "DELETE FROM  Items WHERE id = ?;"
