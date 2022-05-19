import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Downloads\Database1.accdb;')
    print("Database is Connected")

    user_id=11
    database = connect.cursor()
    database.execute('delete from Table1 where id=?',(user_id))
    database.commit()
    print("Record is deleted")

except pyodbc.Error:
    print("Error in Connection")