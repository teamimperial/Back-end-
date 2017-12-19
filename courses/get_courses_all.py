from setting.config import mysql
from flask import Blueprint, render_template


class AllGetCourses:
    @classmethod
    def api_get_all_courses(cls):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'select company.CompanyName, courses.CoursesName, courses.CoursesAmount, courses.CoursesCity, courses.CoursesCountry, courses.CoursesStart, courses.CoursesEnd, courses.CoursesInfo from courses, company where courses.idCompany=company.idCompany '
        param = ()
        cursor.execute(query, param)

        result = cursor.fetchall()

        return result


get_all_courses = Blueprint('get_all_courses', __name__)

@get_all_courses.route('/praxis',methods=['GET'])
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
        course = {
            "company_name": company_name,
            "course_name": course_name,
            "amount": amount,
            "city": city,
            "country": country,
            "date_of_start": date_of_start,
            "date_of_end": date_of_end,
            "info": info
        }
        courses.append(course)
    return render_template('praxis.html',courses=courses), 200