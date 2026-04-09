import sqlite3
def create_connection():
    return sqlite3.connect('Storage.db')

if __name__ == '__main__':
    create_connection()
    print("database connect successfully")