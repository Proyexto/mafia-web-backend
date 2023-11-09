from flask import Flask, Blueprint
from flask_mysqldb import MySQL
import routes as rt


app = Flask(__name__)


app.register_blueprint(rt.api_blueprint)
'''
@app.route('/code')
def code():
    return rt.generar_codigo_alphanumerico(5)
'''
    
if __name__ == '__main__':
    app.run(debug=True)
