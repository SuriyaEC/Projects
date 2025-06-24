import mysql.connector

def connect():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root@S0L",
        database = "user_authentication_db"
    )