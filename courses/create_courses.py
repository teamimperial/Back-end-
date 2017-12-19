from setting.config import mysql
from flask import Blueprint, request, abort, session, jsonify
from users.get_company import GetCompany


class CreateCourses:
    @classmethod
    def create_course(cls, id_company, course_name, amount, city, country, date_of_start, date_of_end, info):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'insert into courses(idCompany,CoursesName,CoursesAmount,CoursesCity,CoursesCountry,CoursesStart,CoursesEnd,CoursesInfo) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        param = (id_company, course_name, amount, city, country, date_of_start, date_of_end, info)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()


create_course = Blueprint('create_course', __name__)


@create_course.route('/create_course', methods=['POST'])
def api_create_courses():
    if request.json:
        if 'company' in session:
            if 'name' not in request.json and 'amount' not in request.json and 'city' not in request.json and 'country' not in request.json and 'date_of_start' not in request.json and 'date_of_end' not in request.json and 'info' not in request.json:
                abort(404)
            login = session['company']
            name = request.json['name']
            amount = request.json['amount']
            city = request.json['city']
            country = request.json['country']
            date_of_start = request.json['date_of_start']
            date_of_end = request.json['date_of_end']
            info = request.json['info']
            id_company = GetCompany.get_company_id_from_db(login)
            CreateCourses.create_course(id_company,name,amount,city,country,date_of_start,date_of_end,info)
            return jsonify(redirect='true', redirect_url='/company/course')
        else:
            return 'please log in'
    if not request.json:
        return 'something wrong with you request'