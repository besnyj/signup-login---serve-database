import sqlite3   ### IS WORKING.

def database_init():
    
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        name TEXT,
        age INTEGER,
        gender TEXT,
        email TEXT,
        password TEXT
    )
    """)
    
    connection.commit()
    connection.close()
        

def register_user(name, age, gender, email, password):
    
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()
        
    cursor.execute("""
    INSERT INTO user VALUES 
    ('{}', '{}', '{}','{}', '{}')
    """.format(name, age, gender, email, password))
    connection.commit()
    connection.close()

def check_user(email, password):
    
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()
        
    cursor.execute("""
    SELECT * FROM user
    WHERE email = '{}'
    """.format(email))
        
    result = cursor.fetchone()

    try:
        if password == result[4]:
                return 0
        else:
                message = "Password does not match"
                return 1
    except TypeError:
                message = "User does not exist"
                return 2
        
