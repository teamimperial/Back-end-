from flask import Blueprint, abort, request, jsonify
from setting.config import mysql


class EditCourse:
    def __init__(self):
        pass

    @classmethod
    def edit_course_name(cls, id_course, course_name):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = "update courses Set CoursesName=%s where idCourse=%s"
        param = (course_name, id_course)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def edit_licensed_amount(cls, id_course, licensed_amount):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = "update courses Set CoursesAmount=%s where idCourse=%s"
        param = (licensed_amount, id_course)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()


    @classmethod
    def edit_city(cls, id_course, city):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = "update courses Set CoursesCity=%s where idCourse=%s"
        param = (city, id_course)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def edit_country(cls, id_course, country):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = "update courses Set CoursesCountry=%s where idCourse=%s"
        param = (country, id_course)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def edit_date_of_start(cls, id_course, date_of_start):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = "update courses Set CoursesStart=%s where idCourse=%s"
        param = (date_of_start, id_course)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def edit_date_of_end(cls, id_course, date_of_end):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = "update courses Set CoursesEnd=%s where idCourse=%s"
        param = (date_of_end, id_course)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def edit_info(cls, id_course, info):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = "update courses Set CoursesInfo=%s where idCourse=%s"
        param = (info, id_course)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def edit_status(cls, id_course, status):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = "update courses Set CoursesStatus=%s where idCourse=%s"
        param = (status, id_course)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()


edit_course = Blueprint('edit_course', __name__)


@edit_course.route('/edit/course', methods=['POST'])
def edit_course_company():
    value = 0
    print(request.json)
    if not request.json or 'id_course' not in request.json:
        abort(400)

    id_course = request.json['id_course']

    if 'name' in request.json:
        course_name = request.json['name']
        if course_name != "":
            EditCourse.edit_course_name(id_course, course_name)
            value = 1

    if 'amount' in request.json:
        licensed_amount = request.json['amount']
        if licensed_amount != "":
            EditCourse.edit_licensed_amount(id_course, licensed_amount)
            value = 1

    if 'city' in request.json:
        city = request.json['city']
        if city != "Null":
            if city != "":
                EditCourse.edit_city(id_course, city)
                value = 1

    if 'country' in request.json:
        country = request.json['country']
        if country != "Null":
            if country != "":
                EditCourse.edit_country(id_course, country)
                value = 1

    if 'date_of_start' in request.json:
        date_of_start = request.json['date_of_start']
        if date_of_start != "":
            EditCourse.edit_date_of_start(id_course, date_of_start)
            value = 1

    if 'date_of_end' in request.json:
        date_of_end = request.json['date_of_end']
        if date_of_end != "":
            EditCourse.edit_date_of_end(id_course, date_of_end)
            value = 1

    if 'status' in request.json:
        status = request.json['status']
        if status != "":
            EditCourse.edit_status(id_course, status)
            value = 1

    if 'info' in request.json:
        info_about = request.json['info']
        if info_about != "":
            EditCourse.edit_info(id_course, info_about)
            value = 1

    if value == 1:
        return jsonify(redirect='true', message="Changes have been successfully saved", redirect_url=''), 200
    else:
        return jsonify(redirect='false', message='Something went wrong. Try again later!!!'), 200
