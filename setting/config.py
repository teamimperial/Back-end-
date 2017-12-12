from flask import Flask
from flask.ext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'richbeach'
app.config['MYSQL_DATABASE_DB'] = 'webproject'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql=MySQL(app)

