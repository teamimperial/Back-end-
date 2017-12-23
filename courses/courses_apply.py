from flask import request, Blueprint, session, jsonify, redirect
from setting.config import mysql
from users.get_student import GetStudent


class ApplyOnCourse:
    @classmethod
    def check_course(cls, id_course, id_company):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'select count(*) from courses where idCourse=%s and idCompany=%s'
        param = (id_course, id_company)

        cursor.execute(query, param)
        check = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return check

    @classmethod
    def apply_students(cls, id_course, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'insert into student_apply(idStudents,idCourse) values(%s,%s)'
        param = (id_students, id_course)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def api_check_already_applied(cls, id_course, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'select exists(select * from student_apply where idCourse = %s and idStudents = %s)'
        param = (int(id_course), int(id_students))

        cursor.execute(query, param)

        check = cursor.fetchone()[0]

        return check



apply_on_course = Blueprint('apply_on_course', __name__)


@apply_on_course.route('/apply', methods=['POST'])
def api_apply_on_course():
    if 'student' in session and request.json:
        link = request.json['link']
        id_course = link[0][1:3]
        id_company = link[1][1:3]
        check_course = ApplyOnCourse.check_course(id_course, id_company)
        if check_course == 0 or check_course > 1:
            print('bad')
            return 'hello'
        else:
            student_login = session['student']
            id_student = GetStudent.get_students_id_from_db(student_login)
            check_apply = ApplyOnCourse.api_check_already_applied(id_course, id_student)
            print(check_apply)
            if check_apply == 1:
                return jsonify(redirect='false', redirect_url='/course/!' + id_course + '/!' + id_company,
                               message='You are already exists on this course.'), 200
            else:
                ApplyOnCourse.apply_students(id_course, id_student)
                return jsonify(redirect='true', redirect_url='/courses'), 200
