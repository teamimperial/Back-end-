from flask import Blueprint, jsonify
from users.get_company import GetCompany

get_info_about_company = Blueprint('get_info_about_company', __name__)


@get_info_about_company.route("/user/company/<login>", methods=["GET"])
def api_info_about_company(login):
    if login == "":
        return jsonify(status="User`s login is null"), 404
    else:
        name = GetCompany.get_company_name_from_db(login)
        email = GetCompany.get_company_email_from_db(login)
        id_company = GetCompany.get_company_id_from_db(login)
        web_site = GetCompany.get_company_web_site(id_company)
        city = GetCompany.get_company_city(id_company)
        country = GetCompany.get_company_country(id_company)
        about_company = GetCompany.get_about_company(id_company)
        photo = GetCompany.get_photo_company(id_company)

        return jsonify(status='Success',name=name,email=email,web_site=web_site,city=city,country=country,about_company=about_company,photo=photo), 201
