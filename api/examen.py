import conn,numpy as np
import pandas as pd
from flask import jsonify,json

db = conn.cursor

def add_examen(db,titel,vak,klas):
     sql = "INSERT INTO examen(examen_titel,vak,klas) value('" + titel + "','" + vak + "','" + klas + "')" 
     db.execute(sql)
     conn.db.commit()
     
def import_vragen(path):
     # df = pd.DataFrame(pd.read_csv (r'%s' %path), columns = ['Vraag','Antwoord1','Antwoord2','Antwoord3','Antwoord4','CorrecteAntwoord'])
     df = pd.read_csv (r'%s' %path)
     data = df.to_dict(orient='records')
     for record in data:
          # Antwoord1,Antwoord2,Antwoord3,Antwoord4,CorrecteAntwoord,Vraag = record
          db.execute('''
                INSERT INTO vragen (vraag, ant_1, ant_2,ant_3,ant_4)
                VALUES (%s,%s,%s,%s,%s)
                ''',
                (
               record['Vraag'], 
                record['Antwoord1'],
                record['Antwoord2'],
                record['Antwoord3'],
                record['Antwoord4']
                )
               )
          print(record)
     return 'True'
 
# print (df)
     # sql= ""
     # db.execute(sql)
     # conn.db.commit()

def add_antw(db,file):
     # import CSV 
     data = pd.read_csv(file)
     df = pd.DataFrame(data, columns = ['Vraag','Antwoord1','Antwoord2','Antwoord3','Antwoord4','CorrecteAntwoord'])
     # insert data 
     for row in df.itertuple():
          db.execute('''
                INSERT INTO  vragen (vraag, ant_1, ant_2,ant_3,ant_4,cor_ant)
                VALUES (?,?,?,?,?)
                ''',
                row.Vraag, 
                row.Antwoord1,
                row.Antwoord2,
                row.Antwoord3,
                row.Antwoord4,
                row.CorrecteAntwoord
                )
     conn.db.commit()
