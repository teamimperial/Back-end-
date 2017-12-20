from setting.config import mysql
from flask import Blueprint, render_template

class AllGetCourses:
    @classmethod
    def api_get_all_courses(cls):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'select company.CompanyName, courses.CoursesName, courses.CoursesAmount, courses.CoursesCity, courses.CoursesCountry, courses.CoursesStart, courses.CoursesEnd, courses.CoursesInfo, company.idCompany, courses.idCourse from courses, company where courses.idCompany=company.idCompany order by idCourse DESC'
        param = ()
        cursor.execute(query, param)

        result = cursor.fetchall()
        print(result)
        return result


get_all_courses = Blueprint('get_all_courses', __name__)


@get_all_courses.route('/praxis', methods=['GET'])
def api_get_all_courses():
    results = AllGetCourses.api_get_all_courses()
    courses = []
    for result in results:
        company_name = result[0]
        course_name = result[1]
        amount = result[2]
        city = result[3]
        country = result[4]
        date_of_start = result[5]
        date_of_end = result[6]
        info = result[7]
        id_company = str(result[8])
        id_course = str(result[9])
        course = {
            "company_name": company_name,
            "course_name": course_name,
            "amount": amount,
            "city": city,
            "country": country,
            "date_of_start": date_of_start,
            "date_of_end": date_of_end,
            "info": info,
            "link": '/course/' + id_course + '/' + id_company
        }
        courses.append(course)
    return render_template('praxis.html', courses=courses), 200
