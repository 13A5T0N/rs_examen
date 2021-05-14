import mysql.connector


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "", 
    database = "rs_examen"
)

cursor = db.cursor(dictionary=True)
