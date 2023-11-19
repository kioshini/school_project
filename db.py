import sqlite3


class Database:
    def __init__(self, database_file):
        self.connect = sqlite3.connect(database_file)
        self.cursor = self.connect.cursor()

    def create_db(self, database):
        with self.connect:
            self.cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER UNIQUE NOT NULL,
active INTEGER DEFAULT (1)
)
''')

    def user_exists(self, user_id):
        with self.connect:
            result = self.cursor.execute("SELECT * FROM `Users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id):
        with self.connect:
            return self.cursor.execute("INSERT INTO `Users` (`user_id`) VALUES (?)", (user_id,))

    def set_active_user(self, user_id, active):
        with self.connect:
            return self.cursor.execute("UPDATE `Users` SET `active` = ? WHERE `user_id` = ?", (active, user_id,))

    def get_users(self):
        with self.connect:
            return self.cursor.execute("SELECT `user_id`, `active` FROM `Users`").fetchall()
