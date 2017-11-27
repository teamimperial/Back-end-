from flask import Blueprint, jsonify
from users.get_student import GetStudent

get_info_about_student = Blueprint('get_info_about_students', __name__)


@get_info_about_student.route("/students/<login>", methods=["GET"])
def api_info_about_students(login):
    if login == "":
        return jsonify(status="User`s login is null"), 404
    else:
        first_name=GetStudent.get_student_first_name_from_db(login)
        last_name=GetStudent.get_student_last_name_from_db(login)
        email=GetStudent.get_student_email_from_db(login)
        return jsonify(status="User is in database",first_name=first_name,last_name=last_name,email=email), 201