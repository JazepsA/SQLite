import sqlite3
#izveidojam DB savienojumu ar Python
conn=sqlite3.connect('test.db')

#print("Datubāze ir izveidota! ")

print("Datubāze ir atvērta")
#izveidosim kursoru,kas norāda uz to vietu kur atrodas dati atmiņā 
cursor=conn.execute("SELECT * from COMPANY")
for i in cursor:
    print("ID=", i[0])
    print("NAME=",i[1])
    print("AGE=",i[2])
    print("ADDRESS=",i[3])
    print("SALARY=",i[4],"\n")

print("Dati ir veiksmīgi nolasīti!")
#atjauninam info
#conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 2")
#conn.commit()
#print("Kopējo izmaiņu skaits:",conn.total_changes)

#Nonemam info
conn.execute("DELETE from COMPANY where ID = 1;")
conn.commit()
print("Dzēstu vienību skaits: ",conn.total_changes)


'''
conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(1,'Paul',32,'California',2000.00)");
conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(2,'Alex',22,'Latvia',15000.00)");
conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(3,'Jups',42,'Malta',1000.00)");
conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(4,'Dainis',19,'Gornica',500.00)");
'''

"""
conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT NOT NULL,
             ADDRESS CHAR(50),
             SALARY REAL);''')
"""
#print("Tabula ir izveidota!")
#conn.commit()
#print("Ieraksti ir izeidoti!")
conn.close()