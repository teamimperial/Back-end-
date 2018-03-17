from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1111'
app.config['MYSQL_DATABASE_DB'] = 'webproject'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

