from flask import request, Blueprint, session
from setting.config import mysql
from users.get_student import GetStudent

class ApplyOnCourse:
    @classmethod
    def check_course(cls, id_course, id_company):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'select count(*) from courses where idCourse=%s and idCompany=%s'
        param = (id_course,id_company)

        cursor.execute(query,param)
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


apply_on_course = Blueprint('apply_on_course',__name__)


@apply_on_course.route('/apply',methods=['POST'])
def api_apply_on_course():
    if 'student' in session and request.json:
        link = request.json['link']
        id_course = link[0][1:3]
        id_company = link[1][1:3]
        check = ApplyOnCourse.check_course(id_course,id_company)
        if check == 0 or check > 1:
            print('bad')
            return 'hello'
        else:
            student_login = session['student']
            id_student = GetStudent.get_students_id_from_db(student_login)
            ApplyOnCourse.apply_students(id_course, id_student)

            return 'hello'