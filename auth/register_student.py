from flask import Blueprint, request, abort, jsonify
from setting.config import mysql

register_student = Blueprint('register_student', __name__)


class Student:
    def __int__(self, login, email, first_name, last_name, password):
        self.login = login
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    @classmethod
    def check_login_for_used(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_login_student = 'SELECT exists(SELECT * FROM students WHERE StudentsLogin = %s)'
        param_login_student = (login)
        cursor.execute(query_login_student, param_login_student)
        if cursor.fetchone()[0] == 1:
            check = 0
            return check

        query_login_company = 'SELECT exists(SELECT * FROM company WHERE CompanyLogin = %s)'
        param_login_company = (login)
        cursor.execute(query_login_company, param_login_company)
        if cursor.fetchone()[0] == 1:
            check = 0
            return check

        connect.commit()
        cursor.close()

    @classmethod
    def check_email_for_used(cls, email):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_email_student = 'SELECT exists(SELECT * FROM students WHERE StudentsEmail = %s)'
        param_email_student = (email)
        cursor.execute(query_email_student, param_email_student)
        if cursor.fetchone()[0] == 1:
            check = 0
            return check

        query_email_company = 'SELECT exists(SELECT * FROM company WHERE CompanyEmail = %s)'
        param_email_company = (email)
        cursor.execute(query_email_company, param_email_company)
        if cursor.fetchone()[0] == 1:
            check = 0
            return check

        connect.commit()
        cursor.close()

    @classmethod
    def save_students_user(cls, login, first_name, last_name, email, password):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_save = 'INSERT INTO students(StudentsLogin,StudentsName,StudentsLastName,StudentsEmail,StudentsPassword,idTypeOfUsers) VALUES(%s,%s,%s,%s,%s,1)'
        param_save = (login, first_name, last_name, email, password)
        cursor.execute(query_save, param_save)

        connect.commit()
        cursor.close()


@register_student.route('/api/register/student', methods=['Post'])
def register_student_api():
    if not request.json:
        abort(400)

    if 'login' not in request.json:
        return jsonify(status='Enter login'), 400

    if 'email' not in request.json:
        return jsonify(status='Enter email'), 400

    if 'firstName' not in request.json:
        return jsonify(status='Enter First Name'), 400

    if 'lastName' not in request.json:
        return jsonify(status='Enter LastName'), 400

    if 'password' not in request.json:
        return jsonify(status='Enter password'), 400

    first_name = request.json['firstName']
    last_name = request.json['lastName']
    password = request.json['password']
    login = request.json['login']
    email = request.json['email']

    if Student.check_login_for_used(login) == 0:
        return jsonify(status='Login already exists'), 400
    if Student.check_email_for_used(email) == 0:
        return jsonify(status='Email already exists'), 400

    # password_enc = generate_password_hash(password)

    Student.save_students_user(login, first_name, last_name, email, password)

    return jsonify(status='success'), 201
