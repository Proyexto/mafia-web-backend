import flask
from flask import Flask, request, json, jsonify
import random, string
#from flask_mysqldb import MySQL


app = flask.Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mafiaweb'
 
#mysql = MySQL(app)
 
app = Flask(__name__)
 
 #Generar un codigo alphanumerico de 6 caracteres para asi tener la ID de las salas
@app.route("/code/<int:longitud>")
def generar_codigo_alphanumerico(longitud):
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(longitud))
    return jsonify(codigo), 200

 
@app.route("/users/<user_id>")
def get_user(user_id): #devolver dato de una base de datos
    user= {"id_user": user_id, "email": "test", "username": "test", "pass": "codigo", "id_img": "1"}
    
    return jsonify(user), 200

@app.route("/users/add", methods=['POST']) #usar postman para probar
def add_user():
    data = request.get_json()
    data["status"] = "user created"
    return jsonify(data), 201
'''
Abre tu solicitud en Postman.

Ve a la sección "Headers" en la solicitud.

Asegúrate de que tienes un encabezado llamado "Content-Type".

En el valor de "Content-Type", cambia "text/plain" a "application/json".
'''
@app.route("/users/delete")
def delete_user():
    return 'a'
    
if __name__ == '__main__':
    app.run(debug=True)
