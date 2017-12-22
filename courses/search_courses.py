from setting.config import mysql
from flask import render_template, request, Blueprint, session, redirect, jsonify


class CourseSearch:
    @classmethod
    def search_courses_in_db_by_name(cls, courses_name):
        connect = mysql.connect()
        cursor = connect.cursor()
        request_form = '%' + courses_name + '%'
        query = 'select company.CompanyName, courses.CoursesName, courses.CoursesAmount, courses.CoursesCity, courses.CoursesCountry, courses.CoursesStart, courses.CoursesEnd, courses.CoursesInfo, company.idCompany, courses.idCourse from courses, company where courses.idCompany=company.idCompany and CoursesName like %s order by idCourse DESC'
        param = (request_form)

        cursor.execute(query, param)

        result = cursor.fetchall()

        return result


search_courses = Blueprint('search_courses', __name__)


@search_courses.route('/praxis/search/<courses_name>')
def api_search(courses_name):
    if 'student' in session or 'company' in session:

        results = CourseSearch.search_courses_in_db_by_name(courses_name)
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
                "link": '/course/!' + id_course + '/!' + id_company
            }
            courses.append(course)
        return render_template('praxis.html',courses=courses), 200
    else:
        return redirect("/")
