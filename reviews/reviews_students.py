from flask import Blueprint, jsonify, render_template
from users.get_student import GetStudent
from security.session_student import StudentSession

get_info_about_student = Blueprint('get_info_about_students', __name__)


@get_info_about_student.route("/user/student/<login>", methods=["GET"])
def api_info_about_students(login):
    if login == "":
        return jsonify(status="User`s login is null"), 404
    else:
        id_student = GetStudent.get_students_id_from_db(login)
        if id_student == 0:
            return 'Not such user in db'
        else:
            result = StudentSession.check_in_session_student()
            if result == 0:
                return 'please Log in'
            if result == login:
                first_name = GetStudent.get_student_first_name_from_db(login)
                last_name = GetStudent.get_student_last_name_from_db(login)
                email = GetStudent.get_student_email_from_db(login)
                city = GetStudent.get_student_city_from_db(id_student)
                country = GetStudent.get_student_country_from_db(id_student)
                date_of_birth = GetStudent.get_student_date_of_birth_from_db(id_student)
                university = GetStudent.get_student_university_from_db(id_student)
                time_of_study = GetStudent.get_student_time_of_study_from_db(id_student)
                link = GetStudent.get_student_linked_in_from_db(id_student)
                about = GetStudent.get_student_about_from_db(id_student)
                photo = GetStudent.get_student_photo_from_db(id_student)
                if photo is None:
                    photo = 'http://placehold.it/500x500'
                else:
                    photo = photo
                student = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "city": city,
                    "country": country,
                    "dateOfBirth": date_of_birth,
                    "university": university,
                    "timeOfStudy": time_of_study,
                    "link": link,
                    "about": about,
                    "photo": photo
                }
                return render_template("profile-s.html", student=student)

            else:
                return 'Please log in'

