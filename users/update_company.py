from flask import Blueprint, request, abort, jsonify
from setting.config import mysql
from users.get_company import GetCompany


class UpdateCompany:
    def __init__(self,login, country,city,image,company_name,web_site,about_company):
        self.login = login
        self.country = country
        self.city = city
        self.image = image
        self.company_name = company_name
        self.web_site = web_site
        self.about_company = about_company

    @classmethod
    def update_web_site(cls, id_company , web_site):
        connect = mysql.connect()
        cursor = connect.cursor()
        query = 'update infoaboutcompany Set WebSite=%s where idCompany=%s'
        param = (web_site, id_company)
        cursor.execute(query,param)
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
        query = 'update infoaboutcomapny SET Photo = %s where idCompany = %s'
        param = (photo, id_copmany)
        cursor.execute(query, param)
        connect.commit()
        cursor.close()

    @classmethod
    def update_company_name(cls):
        connect = mysql.connect()
        cursor = connect.cursor()
        query = ''
        param = ()
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
    def update_about_company(cls):
        connect = mysql.connect()
        cursor = connect.cursor()
        query = ''
        param = ()
        cursor.execute(query, param)
        connect.commit()
        cursor.close()

    @classmethod
    def update_email_company(cls):
        connect = mysql.connect()
        cursor = connect.cursor()
        query = ''
        param = ()
        cursor.execute(query, param)
        connect.commit()
        cursor.close()

update_company = Blueprint('update_company', __name__)

@update_company.route('/company/update', methods=['POST'])
def api_update_company():
    value = 0

    if not request.json and 'login' not in request.json:
        abort(400)

    login = request.json['login']
    id_company = GetCompany.get_company_id_from_db(login)

    if 'webSite' in request.json:
        web_site = request.json['WebSite']
        UpdateCompany.update_web_site(id_company, web_site)
        value = 1

    if 'City' in request.json:
        city = request.json['City']
        UpdateCompany.update_city(city, id_company)
        value = 1

    if 'Country' in request.json:
        country = request.json['Country']
        UpdateCompany.update_country(country, id_company)
        value = 1

    if 'Photo' in request.json:
        photo = request.json['Photo']
        UpdateCompany.update_image(photo, id_company)
        value = 1

    if value == 0:
        return jsonify(status='something bad'), 404
    if value == 1:
        return jsonify(status='success'), 201



