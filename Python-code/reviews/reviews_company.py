from flask import Blueprint, jsonify, render_template
from users.get_company import GetCompany
from security.session_company import CompanySession
from setting.config import mysql

get_info_about_company = Blueprint('get_info_about_company', __name__)


@get_info_about_company.route("/user/company/<login>", methods=["GET"])
def api_info_about_company(login):
    if login == "":
        return jsonify(status="User`s login is null"), 404
    else:
        id_company = GetCompany.get_company_id_from_db(login)
        if id_company == 0:
            return 'Not such User in db'
        else:
            result = CompanySession.check_in_session_company()
            if result == 0:
                return "Please log in"
            if result == login:
                name = GetCompany.get_company_name_from_db(login)
                email = GetCompany.get_company_email_from_db(login)
                web_site = GetCompany.get_company_web_site(id_company)
                city = GetCompany.get_company_city(id_company)
                country = GetCompany.get_company_country(id_company)
                about_company = GetCompany.get_about_company(id_company)
                photo = GetCompany.get_photo_company(id_company)
                check = GetCompany.get_check_company(login)
                if photo is None:
                    photo = 'http://placehold.it/500x500'
                else:
                    photo = photo
                if check == 0:
                    check = "color:transparent"
                    company = {'name': name, 'email': email, 'website': web_site, 'city': city, 'country': country,
                            'about_company': about_company, 'check': check, 'photo': photo}
                    return render_template("profile-c.html", company=company)
                if check == 1:
                    check = "color:grey"
                    company = {'name': name, 'email': email, 'website': web_site, 'city': city, 'country': country,
                               'about_company': about_company, 'check': check, 'photo': photo}
                    return render_template("profile-c.html", company=company)
            else:
                return 'Please log in'


@get_info_about_company.route('/company/review/<login>', methods=['GET'])
def api_get_info_about_company_review(login):
    check = GetCompany.check_such_user_company(login)
    if login != 0:
        id_company = GetCompany.get_company_id_from_db(login)
        name = GetCompany.get_company_name_from_db(login)
        email = GetCompany.get_company_email_from_db(login)
        web_site = GetCompany.get_company_web_site(id_company)
        city = GetCompany.get_company_city(id_company)
        country = GetCompany.get_company_country(id_company)
        about_company = GetCompany.get_about_company(id_company)
        photo = GetCompany.get_photo_company(id_company)
        check = GetCompany.get_check_company(login)
        company = {'name': name, 'email': email, 'website': web_site, 'city': city, 'country': country,
                    'about_company': about_company, 'check': check}
        return render_template("profile-c-reviews.html", company=company)
    else:
        return 'Not such user'


