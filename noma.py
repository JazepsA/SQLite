import sqlite3 as db

with db.connect('nomat.db') as con:
    cur=con.execute(""" SELECT vards FROM  Nomnieks 
                    WHERE tel_nr='513526'""")
    nomnieki=cur.fetchall()#norada,kur ppiegadatie dati
    cur=con.execute(""" SELECT * FROM  Produkts """)
    produkti=cur.fetchall()#norada,kur ppiegadatie dati
    for i in nomnieki:
        print(i) # izdruka visas rindas
        print(i[1],"ar personas kodu: ",i[3],'\n')
    for i in produkti:
        print(i) # izdruka visas rindas

