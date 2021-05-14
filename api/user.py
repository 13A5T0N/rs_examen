import conn 



def login(db,user,pwd):
    sql = "SELECT * from gebruikers where geb_email = '" + user + "'and geb_password ='" + pwd +"'"
    db.execute(sql)
    result = db.fetchall()
    for row in result: 
        return row

def get_studenten(db):
    vak = []
    db.execute("SELECT * from gebruikers where geb_rol ='student'")
    result = db.fetchall()
    resp = result
    return resp

def add_student(db,naam,voornaam,email):
    sql = "INSERT INTO gebruikers(geb_password,geb_rol,geb_naam,geb_voornaam,geb_email) value('student','student','" + naam + "','" + voornaam + "','" + email + "')" 
    db.execute(sql)
    conn.db.commit()

def latest_student(db):
    vak = []
    db.execute("SELECT * from gebruikers where geb_rol ='student' ORDER BY geb_id DESC LIMIT 1")
    result = db.fetchall()
    resp = result
    return resp