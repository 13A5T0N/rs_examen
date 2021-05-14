import conn

db = conn.cursor
def get_vak(db):
    vak = []
    db.execute("SELECT * from vak")
    result = db.fetchall()
    resp = result
    return resp

def add_vak(db,naam):
    sql = "INSERT INTO vak(vak_naam) value('" + naam + "')"
    db.execute(sql)
    conn.db.commit()

def latest_vak(db):
    vak = []
    db.execute("SELECT * from vak ORDER BY vak_id DESC LIMIT 1")
    result = db.fetchall()
    resp = result
    return resp