import conn 
import panda as pd
db = conn.cursor

def add_examen(db,titel,vak,klas):
     sql = "INSERT INTO examen(examen_titel,vak,klas) value('" + titel + "','" + vak + "','" + klas + "')" 
     db.execute(sql)
     conn.db.commit()

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