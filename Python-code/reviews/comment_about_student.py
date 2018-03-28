from flask import Blueprint, request, abort, session, jsonify, redirect
from users.get_company import GetCompany
from users.get_student import GetStudent
from setting.config import mysql
from datetime import datetime

comment_about_student = Blueprint('comment_about_student', __name__)


class CommentAboutStudent:
    def __init__(self):
        pass

    @classmethod
    def comment_about_student(cls, student_id, company_id, comment, time):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'INSERT INTO studentsreviews (idCompany, idStudents, review, time) VALUE (%s,%s,%s,%s)'
        param = (company_id, student_id, comment, time)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def check_student_course(cls, student_login, company_login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT exists (SELECT * FROM students, company, student_apply, courses WHERE students.StudentsLogin=%s AND company.CompanyLogin=%s AND student_apply.idCourse = courses.idCourse AND courses.idCompany = company.idCompany AND student_apply.status = 1 AND courses.CoursesStatus="Finished");'
        param = (student_login, company_login)

        cursor.execute(query, param)

        result = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return result


@comment_about_student.route('/comment/student', methods=['POST'])
def comment_about_student_request():
    print(request.json)
    if not request.json:
        return abort(400)
    if 'student_login' not in request.json:
        return abort(400)
    if 'review' not in request.json:
        return abort(400)
    student_login = request.json['student_login']
    review = request.json['review']
    if 'company' in session:
        company_login = session['company']
        if CommentAboutStudent.check_student_course(student_login, company_login) == 1:
            company_id = GetCompany.get_company_id_from_db(company_login)
            student_id = GetStudent.get_students_id_from_db(student_login)
            time = str(datetime.now().strftime('%H:%M, %d.%m.%Y'))
            CommentAboutStudent.comment_about_student(student_id, company_id, review, time)
            return jsonify(redirect="true", redirect_url=student_login), 200
        else:
            return jsonify(redirect="false", message="This user does not finished your course or "
                                                     "had not approved your course"), 200
