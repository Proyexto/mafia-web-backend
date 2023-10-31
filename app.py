import flask
from flask import request, json, jsonify
from flask_mysqldb import MySQL


app = flask.Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mafiaweb'
 
mysql = MySQL(app)

from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
@app.route("/users/<user_id>")
def get_user(user_id):
    user= {"id_user": user_id, "email": "test", "username": "pass", "id_img": "1"}
    
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