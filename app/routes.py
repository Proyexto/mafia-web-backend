
from flask import request, jsonify, Blueprint
import random, string
from flask_mysqldb import MySQL
import connection as conn 
'''
Abre tu solicitud en Postman.
Ve a la sección "Headers" en la solicitud.
Asegúrate de que tienes un encabezado llamado "Content-Type".
En el valor de "Content-Type", cambia "text/plain" a "application/json".
'''
api_blueprint = Blueprint('api', __name__)

#Comando para generar numero alphanumerico
@api_blueprint.route('/code/<int:longitud>')
def generar_codigo_alphanumerico(longitud):
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(longitud))
    return jsonify({"codigo": codigo}), 200

#Comando para añadir usuario
@api_blueprint.route('/users/add',  methods=['POST'])
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
            conn.cursor.execute(consulta, values)
            conn.conexion.commit() 
            data["status"] = "user created"
            return jsonify(data), 201
        except Exception as e:
            conn.conexion.rollback()
            return jsonify({"error": "Error al agregar usuario a la base de datos"}), 500
    else:
        return jsonify({"error": "Faltan campos obligatorios en los datos de usuario"}), 400

#Comando para hacer soft delete a un usuario
@api_blueprint.route('/users/delete',  methods=['POST'])
def delete_user():
    data = request.get_json()
    
    if "id_user" in data:
        id_user = data["id_user"]
        
        consulta = "UPDATE users SET users.del_at = CURRENT_DATE() WHERE users.username = %s"
        values = (id_user,)
        
        try:
            conn.cursor.execute(consulta, values)
            conn.conexion.commit() 
            data["status"] = "user deleted"
            return jsonify(data), 201
        except Exception as e:
            conn.conexion.rollback()
            return jsonify({"error": "Error al eliminar usuario a la base de datos"}), 500
    else:
        return jsonify({"error": "Faltan campos obligatorios en los datos de usuario"}), 400

#Comando para modifica un usuario
@api_blueprint.route('/users/modify',  methods=['POST'])
def modify_user():
    data = request.get_json()
    
    if "email" in data and "username" in data and "password" in data and "id_img" in data and "id_user" in data:
        email = data["email"]
        username = data["username"]
        password = data["password"]
        id_img = data["id_img"]
        id_user = data["id_user"]
        
        consulta = "UPDATE users SET email = %s, username= %s, password = %s, id_img = %s WHERE id_user = %s"
        values = (email, username, password, id_img, id_user)
        
        try:
            conn.cursor.execute(consulta, values)
            conn.conexion.commit() 
            data["status"] = "user modify"
            return jsonify(data), 201
        except Exception as e:
            conn.conexion.rollback()
            return jsonify({"error": "Error al modificar usuario a la base de datos"}), 500
    else:
        return jsonify({"error": "Faltan campos obligatorios en los datos de usuario"}), 400