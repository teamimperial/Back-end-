from setting.config import mysql
from flask import Blueprint, session, render_template
from users.get_company import GetCompany


class GetCourses:
    @classmethod
    def api_get_courses(cls, id_company):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'select * from courses where idCompany = %s order by idCourse DESC'
        param = (id_company)

        cursor.execute(query,param)

        result = cursor.fetchall()

        return result


get_courses = Blueprint('get_courses',__name__)


@get_courses.route('/company/course', methods=['GET'])
def api_get_courses():
    if 'company' in session:
        login = session['company']
        id_company = GetCompany.get_company_id_from_db(login)
        results = GetCourses.api_get_courses(id_company)
        courses = []
        for result in results:
            name = result[2]
            amount = result[3]
            city = result[4]
            country = result[5]
            date_of_start = result[6]
            date_of_end = result[7]
            info = result[8]
            course = {
                "name": name,
                "amount": amount,
                "city": city,
                "country": country,
                "date_of_start": date_of_start,
                "date_of_end": date_of_end,
                "info": info
            }
            courses.append(course)
        return render_template('courses-c.html', courses=courses)
