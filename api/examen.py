import conn 
db = conn.cursor

def add_examen(db,titel,vak,klas):
     sql = "INSERT INTO examen(examen_titel,vak,klas) value('" + titel + "','" + vak + "','" + klas + "')" 
     db.execute(sql)
     conn.db.commit()