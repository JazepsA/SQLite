import sqlite3 as db

with db.connect('nomat.db') as con:
    #cur=con.execute(""" SELECT * FROM  Nomnieks """)

    cur=con.cursor()

    cur.execute(""" SELECT Nomnieks.vards,Nomnieks.uzvards,Nomnieks.tel_nr,Noma.beind_datums,Produkts.nomas_cena_diena FROM Nomnieks INNER JOIN Noma ON Noma.id_nomnieks = Nomnieks.id_nomnieks INNER JOIN Produkts ON Noma.id_produkts= Produkts.id_produkts WHERE  Nomnieks.tel_nr='1234245'""")

    nomniek= cur.fetchall()

print("Izdrukā nomnieku vārdus ,uzvārdus, mob.nr,kad jāatdod produkts,ja tel nr sakrit ar noradito ")
sum=0

for r in nomniek:
    print(r)
    sum=sum+ int(r[4])
print("\nPar iznomātām precēm dienā jāsamaksā ",sum)







'''
    cur=con.execute(""" SELECT vards FROM  Nomnieks WHERE tel_nr='1234245' """)
    print("Izdruka vardu pec tel nr")
    nomniek_tel=cur.fetchall()
    for rinda in nomniek_tel:
        print(rinda)
    nomnieki=cur.fetchall()#norada,kur ppiegadatie dati
    for i in nomnieki:
        print(i) # izdruka visas rindas
        print(i[1],"ar personas kodu: ",i[3],'\n')
    cur=con.execute(""" SELECT * FROM  Produkts """)

    produkti=cur.fetchall()#norada,kur ppiegadatie dati
    for i in produkti:
        print(i) # izdruka visas rindas



    nomniek_vards=con.execute("""  SELECT vards,uzvards FROM Nomnieks WHERE vards='Andrejs' """).fetchall()


    print('\nIzdrukātu vārdu,uzvadru pēc vārda')
    for i in nomniek_vards:
        print(i)
    '''
