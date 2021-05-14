import conn

db = conn.cursor
def get_klas(db):
    vak = []
    db.execute("SELECT * from klas")
    result = db.fetchall()
    resp = result
    return resp

def add_klas(db,naam):
    sql = "INSERT INTO klas(klas) value('" + naam + "')"
    db.execute(sql)
    conn.db.commit()

def latest_klas(db):
    vak = []
    db.execute("SELECT * from klas ORDER BY klas_id DESC LIMIT 1")
    result = db.fetchall()
    resp = result
    return resp