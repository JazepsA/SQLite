import sqlite3

#Savienojums ar datubāzi "Interneta veikals" 

conn=sqlite3.connect("Interneta_veikals.db")
cursor=conn.cursor()




#1.Datu ievadīšana produktos
cursor.execute('''INSERT INTO Produkti(produkta_id,nosaukums,cena,noliktava) VALUES (?,?,?,?)''',(6,'Apple Iphone 13',999.99,"ir"))

#2. Datu ievadīšana klientu tabulā
cursor.execute('''INSERT INTO Klients(klienta_id,vards,epasts,telefons) VALUES (?,?,?,?)''',(6,'Janis','curka@gmail.com',"155325235"))

#3.Datu ievadīšana pasūtījumos
cursor.execute('''INSERT INTO Pasutijumi(pasutijuma_id,datums,kopsumma) VALUES (?,?,?)''',(6,'2024-11-02',999.99))

#4. Datu ievadīšana pasūtījuma detaļās

cursor.execute('''INSERT INTO Detalas(detalas_id,pasutijuma_id,produkta_id,daudzums) VALUES(?,?,?,?) ''',(9,1,1,1))

#Saglabāt izmaiņas

conn.commit()




# 5.Datu nolasīšana 

cursor.execute('SELECT * FROM Pasutijumi')
orders=cursor.fetchall()
print("Pasūtījumi:")
for order in orders:
    print(order)
 
#6. Datu nolasīšana ar sasaisti(piem:pasūtījumu detaļas ar produktiem un klientiem)


cursor.execute('''
SELECT 
    Klients.vards,
    Klients.telefons,
    Pasutijumi.datums,
    Pasutijumi.kopsumma,
    Produkti.nosaukums,
    Produkti.cena,
    Detalas.daudzums,
    Produkti.cena*Detalas.daudzums 
FROM 
    Klients

INNER JOIN Pasutijumi

ON Klients.klienta_id = Pasutijumi.klienta_id



INNER JOIN Detalas

ON Pasutijumi.pasutijuma_id = Detalas.pasutijuma_id

INNER JOIN Produkti 

ON Produkti.produkta_id = Detalas.produkta_id

''')

order_details=cursor.fetchall()
print("\n Pasūtījuma detaļas:")
for detail in order_details:
    print(detail)


#Savienojuma aizvēršana
conn.close()
