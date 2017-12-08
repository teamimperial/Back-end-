from setting.config import mysql
from flask import Blueprint, request, jsonify, abort, session, redirect
from werkzeug.security import check_password_hash
from users.get_student import GetStudent
from users.get_company import GetCompany


class Login:
    def __int__(self, user_login, password):
        self.login = user_login
        self.password = password

    @classmethod
    def search_user_in_student_list(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_search = 'SELECT exists(SELECT * FROM students WHERE StudentsLogin = %s)'
        param_search = (login)
        cursor.execute(query_search, param_search)
        if cursor.fetchone()[0] == 1:
            check = 1
            return check

        connect.commit()
        cursor.close()

    @classmethod
    def get_password_from_students(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_password = 'SELECT StudentsPassword FROM students WHERE StudentsLogin=%s'
        param_get_password = (login)
        cursor.execute(query_get_password, param_get_password)
        password = str(cursor.fetchone()[0])

        connect.commit()
        cursor.close()

        return password

    @classmethod
    def search_user_in_company_list(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_search = 'SELECT exists(SELECT * FROM Company WHERE CompanyLogin = %s)'
        param_search = (login)
        cursor.execute(query_search, param_search)
        if cursor.fetchone()[0] == 1:
            check = 1
            return check

        connect.commit()
        cursor.close()

    @classmethod
    def get_password_from_Company(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_password = 'SELECT CompanyPassword FROM company WHERE CompanyLogin=%s'
        param_get_password = (login)
        cursor.execute(query_get_password, param_get_password)
        password = str(cursor.fetchone()[0])

        connect.commit()
        cursor.close()

        return password

    @classmethod  # метод не працює
    def check_password(cls, password, password_from_db):
        if check_password_hash(password_from_db, password):
            check = 1
            return check

    @classmethod  # метод для перевірки паролю
    def equals_password(cls, password, password_from_db):
        if password == password_from_db:
            check = 1
            return check
        else:
            check = 0
            return check


login_api = Blueprint('login_api', __name__)


@login_api.route('/login', methods=["Get", "POST"])
def login():
    if not request.json:
        print(request)
        return jsonify(status="Bad request"), 400
    if 'login' not in request.json:
        return jsonify(status="Enter login"), 400
    if 'password' not in request.json:
        return jsonify(status="Enter password"), 400

    login = request.json['login']
    password = request.json['password']

    if Login.search_user_in_student_list(login) == 1:
        password_from_db = Login.get_password_from_students(login)
        if Login.check_password(password, password_from_db) == 1:
            session['student'] = login
            return jsonify(redirect="true",redirect_url="/user/student/"+login), 200

        else:
            return jsonify(status="Incorrect password"), 400

    elif Login.search_user_in_company_list(login) == 1:
        password_from_db = Login.get_password_from_Company(login)
        if Login.check_password(password, password_from_db) == 1:
            name = GetCompany.get_company_name_from_db(login)
            email = GetCompany.get_company_email_from_db(login)
            session['company'] = login
            return jsonify(redirect='true', redirect_url="/user/company/"+login), 200
        else:
            return jsonify(status="Incorrect password"), 400

    else:
        return jsonify(status='Incorrect user login'), 400
