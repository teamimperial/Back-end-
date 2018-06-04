from flask import Blueprint, request, jsonify, session
from setting.config import mysql
from users.get_company import GetCompany
from security.change_password_company import ChangePasswordCompany


class UpdateCompany:
    def __init__(self, login, country, city, image, company_name, web_site, about_company):
        self.login = login
        self.country = country
        self.city = city
        self.image = image
        self.company_name = company_name
        self.web_site = web_site
        self.about_company = about_company

    @classmethod
    def update_web_site(cls, id_company, web_site):
        connect = mysql.connect()
        cursor = connect.cursor()
        query = 'update infoaboutcompany Set WebSite=%s where idCompany=%s'
        param = (web_site, id_company)
        cursor.execute(query, param)
        connect.commit()
        cursor.close()

    @classmethod
    def update_city(cls, city, id_company):
        connect = mysql.connect()
        cursor = connect.cursor()
        query = 'update infoaboutcompany SET City = %s where idCompany=%s'
        param = (city, id_company)
        cursor.execute(query, param)
        connect.commit()
        cursor.close()

    @classmethod
    def update_image(cls, photo, id_copmany):
        connect = mysql.connect()
        cursor = connect.cursor()
        query = 'update infoaboutcompany SET Photo = %s where idCompany = %s'
        param = (photo, id_copmany)
        cursor.execute(query, param)
        connect.commit()
        cursor.close()

    @classmethod
    def update_company_name(cls, company_name, id_company):
        connect = mysql.connect()
        cursor = connect.cursor()
        query = 'update company SET CompanyName=%s where idCompany=%s'
        param = (company_name, id_company)
        cursor.execute(query, param)
        connect.commit()
        cursor.close()

    @classmethod
    def update_country(cls, country, id_company):
        connect = mysql.connect()
        cursor = connect.cursor()
        query = 'update infoaboutcompany SET Country = %s where idCompany = %s'
        param = (country, id_company)
        cursor.execute(query, param)
        connect.commit()
        cursor.close()

    @classmethod
    def update_about_company(cls, about_company, id_company):
        connect = mysql.connect()
        cursor = connect.cursor()
        query = 'update infoaboutcompany SET AboutCompany = %s where idCompany = %s '
        param = (about_company, id_company)
        cursor.execute(query, param)
        connect.commit()
        cursor.close()

    @classmethod
    def check_company_email(cls, email):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT exists(SELECT * from students, company where students.StudentsEmail = %s or company.CompanyEmail = %s)'
        param = (email, email)
        cursor.execute(query, param)

        result = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return result

    @classmethod
    def update_company_email(cls, id_company, email):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE company SET CompanyEmail = %s where idCompany = %s'
        param = (email, id_company)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()


update_company = Blueprint('update_company', __name__)


@update_company.route('/company/update', methods=['POST'])
def api_update_company():
    if 'company' in session:
        global value
        login = session['company']
        id_company = GetCompany.get_company_id_from_db(login)
        value = 0
        if 'webSite' in request.json:
            web_site = request.json['webSite']
            if web_site != "":
                UpdateCompany.update_web_site(id_company, web_site)
                value = 1

        if 'City' in request.json:
            city = request.json['City']
            if city != "" and city != "Null":
                UpdateCompany.update_city(city, id_company)
                value = 1

        if 'Country' in request.json:
            country = request.json['Country']
            if country != "" and country != "Null":
                UpdateCompany.update_country(country, id_company)
                value = 1

        if 'Photo' in request.json:
            photo = request.json['Photo']
            if photo != "":
                UpdateCompany.update_image(photo, id_company)
                value = 1

        if 'CompanyName' in request.json:
            company_name = request.json['CompanyName']
            if company_name != "":
                UpdateCompany.update_company_name(company_name, id_company)
                value = 1

        if 'AboutCompany' in request.json:
            about_company = request.json['AboutCompany']
            if about_company != "":
                UpdateCompany.update_about_company(about_company, id_company)
                value = 1

        if 'Email' in request.json:
            email = request.json['Email']
            if email != "":
                check = UpdateCompany.check_company_email(email)
                if check != 1:
                    UpdateCompany.update_company_email(id_company, email)
                    value = 1

        if 'NewPassword' in request.json and 'OldPassword' in request.json and 'ConfirmPassword' in request.json:
            new_password = request.json['NewPassword']
            old_password = request.json['OldPassword']
            confirm_password = request.json['ConfirmPassword']
            if new_password != "" and old_password != "" and confirm_password != "":
                if confirm_password == new_password:
                    value = ChangePasswordCompany.equals_password(old_password, login, new_password)
                    if value == 0:
                        return jsonify(redirect='false', message='Incorrect old password'), 200
                else:
                    return jsonify(redirect='false',message='Password don`t match. Try again....'), 200
        if value == 1:
            return jsonify(redirect="true", redirect_url='/user/company/' + login,
                           message='Changes have been successfully saved'), 200
        if value == 0:
            return jsonify(redirect="true", redirect_url='/user/company/' + login,
                           message='Something went wrong. Try again later!!!'), 200
    else:
        message = 'Please log in. Something wrong with your session.'
        return jsonify(redirect='true', redirect_url='/error/' + message), 405
