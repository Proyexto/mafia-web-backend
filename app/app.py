import flask
from flask import Flask, request, json, jsonify
import random, string
import mysql.connector
from flask_mysqldb import MySQL


app = flask.Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mafiaweb'

conexion = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)
#mysql = MySQL(app)

app = Flask(__name__)
 
# Creo un objewr to cursor para ejecutar consultas
cursor = conexion.cursor()
 
# consulta = "aca va la consulta"
# cursor.execute(consulta)
 
 #Generar un codigo alphanumerico de 6 caracteres para asi tener la ID de las salas
@app.route("/code/<int:longitud>")
def generar_codigo_alphanumerico(longitud):
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(longitud))
    return jsonify(codigo), 200

 
@app.route("/users/<user_id>")
def get_user(self, user_id): #devolver dato de una base de datos
    user= {"id_user": user_id, "email": "test", "username": "test", "pass": "codigo", "id_img": "1"}
    #consulta = "SELECT * FROM users WHERE id_user = %s", (user_id)" ARREGLAR
    cursor.execute(consulta)
    
    return jsonify(user), 200

@app.route("/users/add", methods=['POST'])
def add_user():
    data = request.get_json()
    
    if "email" in data and "username" in data and "password" in data and "id_img" in data:
        email = data["email"]
        username = data["username"]
        password = data["password"]
        id_img = data["id_img"]
        
        consulta = "INSERT INTO users (email, username, password, id_img) VALUES (%s, %s, %s, %s)"
        values = (email, username, password, id_img)
        
        try:
            cursor.execute(consulta, values)
            conexion.commit() 
            data["status"] = "user created"
            return jsonify(data), 201
        except Exception as e:
            conexion.rollback()
            return jsonify({"error": "Error al agregar usuario a la base de datos"}), 500
    else:
        return jsonify({"error": "Faltan campos obligatorios en los datos de usuario"}), 400
'''
Abre tu solicitud en Postman.

Ve a la sección "Headers" en la solicitud.

Asegúrate de que tienes un encabezado llamado "Content-Type".

En el valor de "Content-Type", cambia "text/plain" a "application/json".
'''
@app.route("/users/delete", methods=["POST"])
def delete_user():
    data = request.get_json()
    
    if "id_user" in data:
        id_user = data["id_user"]
        
        consulta = "DELETE FROM users WHERE id_user = %s"
        values = (id_user,)
        
        try:
            cursor.execute(consulta, values)
            conexion.commit() 
            data["status"] = "user deleted"
            return jsonify(data), 201
        except Exception as e:
            conexion.rollback()
            return jsonify({"error": "Error al eliminar usuario a la base de datos"}), 500

if __name__ == '__main__':
    app.run(debug=True)
