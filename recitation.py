import pyodbc

try:
    try:
        connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Downloads\Database01.accdb;')
        print("Database is Connected")

        database = connect.cursor()
        database.execute('''INSERT INTO Table1(ID,FullName,Age,Address,Birthdate,SemGrade) VALUES(?,?,?,?,?,?)''',
                     (11,'John Fred B. Delos Santos', 19, 'Palawan', '22/08/2002', 99))
        database.commit()
        print("Record is added")

    except:
        print("Record is already in the database")

except pyodbc.Error:
    print("Error in Connection")