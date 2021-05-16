import conn 
import pandas as pd
from flask import jsonify

db = conn.cursor

def add_examen(db,titel,vak,klas):
     sql = "INSERT INTO examen(examen_titel,vak,klas) value('" + titel + "','" + vak + "','" + klas + "')" 
     db.execute(sql)
     conn.db.commit()
     
def import_vragen(path):
     df = pd.read_csv (r'%s' %path)
     data = jsonify(df.to_dict(orient='records'))
     for record in data:
          Antwoord1,Antwoord2,Antwoord3,Antwoord4,CorrecteAntwoord,Vraag = record
     #      sql = "INSERT INTO vragen(examen_titel,vak,klas) value('" + titel + "','" + vak + "','" + klas + "')" 
     #      print(sql)
     return data

# print (df)
     # sql= ""
     # db.execute(sql)
     # conn.db.commit()