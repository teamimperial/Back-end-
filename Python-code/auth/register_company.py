from flask import Blueprint, jsonify, request, abort, render_template, session
from setting.config import mysql
from users.get_company import GetCompany
from werkzeug.security import generate_password_hash, check_password_hash


class Company:
    def __init__(self, name, email, login, password):
        self.name = name
        self.email = email
        self.login = login
        self.password = password

    @classmethod
    def check_login_for_used(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_login_company = 'select exists(select * from company where CompanyLogin=%s)'
        param_login_company = (login)
        cursor.execute(query_login_company, param_login_company)
        if cursor.fetchone()[0] == 1:
            check = 0
            return check

        query_login_student = 'select exists(select * from students where StudentsLogin=%s)'
        param_login_studetns = (login)
        cursor.execute(query_login_student, param_login_studetns)
        if cursor.fetchone()[0] == 1:
            check = 0
            return check

        connect.commit()
        cursor.close()

    @classmethod
    def check_email_for_used(cls, email):
        conn = mysql.connect()
        cur = conn.cursor()

        query_email_company = 'select exists(select * from company where CompanyEmail = %s)'
        param_email_compamy = (email)
        cur.execute(query_email_company, param_email_compamy)
        if cur.fetchone()[0] == 1:
            check = 0
            return check

        query_email_students = 'select exists(select * from students where StudentsEmail = %s)'
        param_email_studets = (email)
        cur.execute(query_email_students, param_email_studets)
        if cur.fetchone()[0] == 1:
            check = 0
            return check

        conn.commit()
        cur.close()

    @classmethod
    def save_company_user(cls, login, name, email, password):
        connect = mysql.connect()
        cursor = connect.cursor()
        query_save = 'insert into Company(CompanyLogin,CompanyEmail,CompanyPassword,CompanyName,idTypeOfUsers,Company_Check) values(%s,%s,%s,%s,2,0)'
        param_save = (login, email, password, name)
        cursor.execute(query_save, param_save)
        connect.commit()
        cursor.close()

    @classmethod
    def save_info_about_company(cls, id_company):
        connect = mysql.connect()
        cursor = connect.cursor()
        query_save = 'insert into InfoAboutCompany(idCompany) values(%s)'
        param_save = (id_company)
        cursor.execute(query_save, param_save)
        connect.commit()
        cursor.close()


register_company = Blueprint('register_company', __name__)


@register_company.route('/api/register/company', methods=['POST'])
def register_company_api():
    if not request.json:
        abort(400)
    if 'login' not in request.json and 'name' not in request.json and 'password' not in request.json and 'email' not in request.json and 'confirm' not in request.json:
        abort(400)

    login = request.json['login']
    name = request.json['name']
    password = request.json['password']
    email = request.json['email']
    confirm = request.json['confirm']
    if password != confirm:
        return jsonify(redirect='false', message='Passwords don`t match. Try again....'), 400
    else:
        if Company.check_login_for_used(login) == 0:
            return jsonify(redirect='false', message='Your login already exist. Try again....'), 400
        if Company.check_email_for_used(email) == 0:
            return jsonify(redirect='false', message='Your email already exist. Try again....'), 400

        else:
            password_enc = generate_password_hash(password)
            Company.save_company_user(login, name, email, password_enc)
            id = GetCompany.get_company_id_from_db(login)
            Company.save_info_about_company(id)
            session['company'] = login

        return jsonify(redirect='true',redirect_url='/user/company/'+login), 200
