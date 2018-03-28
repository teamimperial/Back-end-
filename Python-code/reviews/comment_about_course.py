from flask import Blueprint, request, abort, session, jsonify
from users.get_student import GetStudent
from users.get_company import GetCompany
from setting.config import mysql
from datetime import datetime

comment_about_course = Blueprint('comment_about_course', __name__)


class CommentAboutCourse:
    def __init__(self):
        pass

    @classmethod
    def check_student_review_course(cls, student_id, course_id):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT exists(SELECT * FROM student_apply WHERE student_apply.idStudents = %s and student_apply.idCourse = %s);'
        param = (student_id, course_id)

        cursor.execute(query, param)
        result = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return result

    @classmethod
    def save_comment_about_course(cls, course_id, student_id, review, time):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'INSERT INTO coursereviews(idStudents, idCourse, review, time) VALUE (%s,%s,%s,%s)'
        param = (student_id, course_id, review, time)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()


@comment_about_course.route('/comment/course', methods=['POST'])
def comment_about_course_request():
    if not request.json:
        return abort(400)
    if 'course_id' not in request.json:
        return abort(400)
    if 'review' not in request.json:
        return abort(400)
    course_id = request.json['course_id']
    review = request.json['review']
    if 'student' in session:
        student_login = session['student']
        student_id = GetStudent.get_students_id_from_db(student_login)
        check = CommentAboutCourse.check_student_review_course(student_id, course_id)
        if check == 1:
            time = str(datetime.now().strftime('%H:%M, %d.%m.%Y'))
            CommentAboutCourse.save_comment_about_course(course_id, student_id, review, time)
            return jsonify(redirect="true", redirect_url=""), 200
        if check == 0:
            return jsonify(redirect="false", message='You don`t end this course'), 200
    return jsonify(redirect='false', message='Something bad..... Try later!!!')