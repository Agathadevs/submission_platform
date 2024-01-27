import sqlite3
db = sqlite3.connect('customers.db')
cursor = db.cursor()

cursor.execute(
'''
    CREATE TABLE HUMAN
    (email TEXT NOT NULL,
    passward INT NOT NULL);
'''
)

db.commit()