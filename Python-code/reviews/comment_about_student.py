from flask import Blueprint, request, abort, session, jsonify
from setting.config import mysql

comment_about_student = Blueprint('comment_about_student',__name__)


class CommentAboutStudent:
    @classmethod
    def comment_about_student(cls, student_login, company_login, comment):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = ''
        param = (student_login, company_login, comment)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()


@comment_about_student.route('/comment_about_student')
def comment_about_student_request():
    if not request.json:
        return abort(400)
    if 'name_student' not in request.json:
        return abort(400)
    if 'comment' not in request.json:
        return abort(400)
    student_name = request.json['name_student']
    comment = request.json['comment']
    if 'company' in session:
        company_login = session['company']
        CommentAboutStudent.comment_about_student(student_login, company_login, comment)
    return jsonify('Ok comment'), 200