import sqlite3

conn=sqlite3.connect('gramatas.db')

cursor=conn.cursor()

#Datu nolasīšana 
cursor.execute('SELECT * FROM Gramatas')
orders=cursor.fetchall()
print("Gramatas:")
for order in orders:
    print(order)

cursor.execute('''
SELECT 
    Autori.vards,
    Autori.uzvards,
    Autori.autora_id,
    Gramatas.nosaukums,
    Gramatas.gads
FROM 
    Autori
               
JOIN Gramatas

ON Autori.autora_id = Gramatas.autora_id''')

info=cursor.fetchall()
print("\n Autora darbi un papildus info:")
for a in info:
    print(a)

cursor.execute('''
SELECT 
    Gramatas.nosaukums,
    Gramatas.gads
FROM 
    Gramatas
''')





"""
conn.execute('''CREATE TABLE Gramatas(gramamtas_id INT PRIMARY KEY NOT NULL , nosaukums TEXT NOT NULL , gads INT NOT NULL , autora_id INT NOT NULL);''')

conn.execute('''CREATE TABLE Autori
             (autora_id INT PRIMARY KEY NOT NULL,vards TEXT NOT NULL,uzvards TEXT NOT NULL);''')
"""

"""
conn.execute("INSERT INTO Gramatas(gramamtas_id,nosaukums,gads,autora_id)\
             VALUES(1,'Mācīties dejot lietū',2002,1)");
conn.execute("INSERT INTO Gramatas(gramamtas_id,nosaukums,gads,autora_id)\
             VALUES(2,'Pāru (ne)būšanas',2012,2)");
conn.execute("INSERT INTO Gramatas(gramamtas_id,nosaukums,gads,autora_id)\
             VALUES(3,'Svētdienas atklāsmes',2015,3)");

conn.execute("INSERT INTO Autori(autora_id,vards,uzvards)\
             VALUES(1,'Puzulis','Poika')");
conn.execute("INSERT INTO Autori(autora_id,vards,uzvards)\
             VALUES(2,'Tigeris','Loka')");
conn.execute("INSERT INTO Autori(autora_id,vards,uzvards)\
             VALUES(3,'Dainis','Bernankopelmen')");
"""





conn.commit()
conn.close()
