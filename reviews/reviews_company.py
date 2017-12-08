from flask import Blueprint, jsonify, render_template
from users.get_company import GetCompany
from security.session_company import CompanySession

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
            print(result)
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
                company = {'name': name, 'email': email, 'website': web_site, 'city': city, 'country': country,
                       'about_company': about_company}
                return render_template("profile-c.html", company=company)
            else:
                return 'Please log in'