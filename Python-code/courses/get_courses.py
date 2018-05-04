from setting.config import mysql
from flask import Blueprint, session, render_template, redirect
from users.get_company import GetCompany


class GetCourses:
    def __init__(self):
        pass

    @classmethod
    def api_get_courses(cls, id_company):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT * FROM courses WHERE idCompany = %s ORDER BY idCourse DESC'
        param = id_company

        cursor.execute(query, param)

        result = cursor.fetchall()

        return result


get_courses = Blueprint('get_courses', __name__)


@get_courses.route('/company/course', methods=['GET'])
def api_get_courses():
    if 'company' in session:
        login = session['company']
        id_company = GetCompany.get_company_id_from_db(login)
        results = GetCourses.api_get_courses(id_company)
        photo = GetCompany.get_photo_company(id_company)
        if photo is None:
            photo = 'http://placehold.it/100x100'
        else:
            photo = photo
        courses = []
        for result in results:
            id_course = str(result[0])
            id_company = str(result[1])
            name = result[2]
            amount = result[3]
            city = result[4]
            country = result[5]
            date_of_start = result[6]
            date_of_end = result[7]
            info = result[8]
            status = result[9]
            course = {
                "name": name,
                "amount": amount,
                "city": city,
                "country": country,
                "date_of_start": date_of_start,
                "date_of_end": date_of_end,
                "info": info,
                "status": status,
                "link": '/course/!' + id_course + '/!' + id_company,
                "photo": photo
            }
            courses.append(course)
        return render_template('courses-c.html', courses=courses)
    else:
        return redirect("/")
