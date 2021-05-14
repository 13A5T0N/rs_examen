import user ,flask,conn,vakken,klassen,examen
from flask import * 

# declare variables
db = conn.cursor

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Test</h1>"

@app.route('/login',methods=['POST'])
def login():
    if 'email' in request.form and 'pwd' in request.form:
        email = request.form.get("email")
        pwd = request.form.get("pwd")
    else:
        return "Error: No data inserted"
    return jsonify(user.login(db,email,pwd))

@app.route('/vak',methods=['GET'])
def vak():
   return jsonify(vakken.get_vak(db)) 

@app.route('/vak/add',methods=['POST'])
def add_vak():
    if 'vak_naam' in request.form:
        vak_naam = request.form.get("vak_naam")
        vakken.add_vak(db,vak_naam)
        return jsonify("true")
    else:
        return "Error: No data inserted"
   

@app.route('/vak/latest',methods=['GET'])
def latest_vak():
    return jsonify(vakken.latest_vak(db))

@app.route('/klas',methods=['GET'])
def klas():
    return jsonify(klassen.get_klas(db))

@app.route('/klas/add',methods=['POST'])
def add_klas():
    if 'naam' in request.form:
        naam = request.form.get("naam")
        klassen.add_klas(db,naam)
        return jsonify('True')
    else:
        return "Error: No data inserted"
    
@app.route('/klas/latest',methods=['GET'])
def latest_klas():
    return jsonify(klassen.latest_klas(db)) 

@app.route('/studenten/add',methods=['POST'])
def add_student():
    if 'naam' in request.form and 'voornaam' in request.form and 'email' in request.form:
        naam = request.form.get('naam')
        voornaam = request.form.get('voornaam')
        email = request.form.get('email')
        user.add_student(db,naam,voornaam,email)
        return jsonify("True")
    else:
        return "Error: No data inserted"

@app.route('/studenten',methods=['GET'])
def get_student():
    return jsonify(user.get_studenten(db))

@app.route('/studenten/latest',methods=['GET'])
def latest_student():
    return jsonify(user.latest_student(db))  

@app.route('/examen/add', methods=['POST'])
def add_examen():
    titel = request.form.get('titel')
    vak = request.form.get('vak')
    klas = request.form.get('klas')
    file = request.form.get('file')
    examen.add_examen(db,titel,vak,klas)
    examen.add_antw(db,file)
    return jsonify('true')

@app.after_request
def after_request(response):
  response.headers.set('Access-Control-Allow-Origin', '*')
  response.headers.set('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.set('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response 

app.run()