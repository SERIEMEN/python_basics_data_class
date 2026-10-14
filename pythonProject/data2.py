import sqlite3

#during august bootcamp an attempt to create an attendance tracker project

ceramic = sqlite3.connect('record.db') #what is squlite3t? Is record.db the database you want to create
print('DB connection initialised...')
database = ceramic.cursor()
database.execute('DROP TABLE IF EXISTS Attendance;') # what is the semicolumn for and what is the sales record a table that already exists?
print('\n') # what are we printing in a new line?
ceramic.execute('CREATE TABLE IF NOT EXISTS Attendance(serial_ID TEXT PRIMARY KEY, student_name TEXT, phone_number INTEGER);')# why did you use capital letter
ceramic.execute('''INSERT INTO Attendance VALUES( 001,'Kelvin', 0709384638);''') #should the text not be an integer?
ceramic.execute('''INSERT INTO Attendance VALUES( 002,'Kingsley',09162749272);''')

ceramic.execute('''ALTER TABLE Attendance ADD COLUMN SEX TEXT ''')
ceramic.execute('''INSERT INTO Attendance VALUES( 003,'Kamsi',09162439272, 'Female');''')
ceramic.execute('''INSERT INTO Attendance VALUES( 004,'Kumasi',09162432272, 'Male');''')

output = ceramic.execute('''SELECT * FROM Attendance''')
for i in output:
    print(i)
print('\n')



if ceramic:
    ceramic.commit()
    ceramic.close()
    print('Connection Closed')

conn = sqlite3.connect('example.db')
database = conn.cursor()
query = 'SELECT sqlite_version();'
database.execute(query)
result = database.fetchall()

print(f'SQLite version is{result}')

if conn:
    conn.commit()
    conn.close()
    print('Connection Closed')



