from setting.config import mysql
from flask import Blueprint, request, jsonify, abort
from werkzeug.security import check_password_hash
from users.get_student import GetStudent
from users.get_company import GetCompany
from security.hash_password import Password


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
            return jsonify(status="success"), 201

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
        abort(400)
    if 'login' not in request.json:
        return jsonify(status="Enter login"), 400
    if 'password' not in request.json:
        return jsonify(status="Enter password"), 400

    login = request.json['login']
    password = request.json['password']

    if Login.search_user_in_student_list(login) == 1:
        password_from_db = Login.get_password_from_students(login)
        if Password.check_password(password, password_from_db) == 1:
            first_name = GetStudent.get_student_first_name_from_db(login)
            last_name = GetStudent.get_student_last_name_from_db(login)
            email = GetStudent.get_student_email_from_db(login)
            id_students = GetStudent.get_students_id_from_db(login)
            # UserSession.create_session_student(login)
            return jsonify(idStudents=id_students,firstName=first_name, lastName=last_name, email=email, login=login, userType="student"), 201
        else:
            return jsonify(status="Incorrect password"), 400

    elif Login.search_user_in_company_list(login) == 1:
        password_from_db = Login.get_password_from_Company(login)
        if Login.equals_password(password, password_from_db) == 1:
            name = GetCompany.get_company_name_from_db(login)
            email = GetCompany.get_company_email_from_db(login)
            return jsonify(name=name, email=email, login=login, userType="company"), 201
        else:
            return jsonify(status="Incorrect password"), 400

    else:
        return jsonify(status='Incorrect user login'), 400
