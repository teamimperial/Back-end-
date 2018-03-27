from setting.config import mysql
from flask import Blueprint, request, abort, jsonify, session
from users.get_student import GetStudent
from security.change_password_student import ChangePasswordStudent
from werkzeug.security import check_password_hash


class UpdateStudent:
    @classmethod
    def update_students_photo(cls, photo, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE infoaboutstudent SET Photo = %s where idStudents = %s'
        param = (photo, id_students)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def update_students_city(cls, city, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE infoaboutstudent SET City = %s WHERE idStudents = %s'
        param = (city, id_students)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def update_students_country(cls, country, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE infoaboutstudent SET Country = %s WHERE idStudents = %s'
        param = (country, id_students)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def update_students_date_of_birth(cls, date_of_birth, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE infoaboutstudent SET DateOfBirth = %s WHERE idStudents = %s'
        param = (date_of_birth, id_students)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def update_students_university(cls, university, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE infoaboutstudent SET University = %s WHERE idStudents = %s'
        param = (university, id_students)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def update_students_styding_time(cls, styding_time, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE infoaboutstudent SET TimeOfStyding = %s WHERE idStudents = %s'
        param = (styding_time, id_students)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def update_students_linked_in(cls, linked_in, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE infoaboutstudent SET LinktoLinkedIn = %s WHERE idStudents = %s'
        param = (linked_in, id_students)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def update_students_about_student(cls, about_student, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE infoaboutstudent SET AboutStudent = %s WHERE idStudents = %s'
        param = (about_student, id_students)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def update_students_cv(cls, cv, id_students):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE infoaboutstudent SET CV = %s WHERE idStudents = %s'
        param = (cv, id_students)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def check_equal_password_student(cls, password_from_db, password):
        if check_password_hash(password_from_db, password):
            value = 1
        else:
            value = 0
        return value

    @classmethod
    def update_student_first_name(cls, id_student, first_name):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE students SET StudentsName = %s where idStudents = %s'
        param = (first_name, id_student)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def update_student_last_name(cls, id_student, last_name):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE students SET StudentsLastName = %s where idStudents = %s'
        param = (last_name, id_student)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def check_student_email(cls, email):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT exists(SELECT * from students, company where students.StudentsEmail = %s or company.CompanyEmail = %s)'
        param = (email, email)
        cursor.execute(query, param)

        result = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return result

    @classmethod
    def update_student_email(cls, id_student, email):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE students SET StudentsEmail = %s where idStudents = %s'
        param = (email, id_student)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()


update_students = Blueprint('update_students', __name__)


@update_students.route('/student/update', methods=['POST'])
def api_update_students():
    value = 0
    print (request.json)
    if 'student' in session:
        login = session['student']
        id_student = GetStudent.get_students_id_from_db(login)
        if 'first_name' in request.json:
            first_name = request.json['first_name']
            if first_name != "":
                UpdateStudent.update_student_first_name(id_student, first_name)
                value = 1

        if 'last_name' in request.json:
            last_name = request.json['last_name']
            if last_name != "":
                UpdateStudent.update_student_last_name(id_student, last_name)
                value = 1

        if 'img' in request.json:
            photo = request.json['img']
            if photo != "":
                UpdateStudent.update_students_photo(photo, id_student)
                value = 1

        if 'city' in request.json:
            city = request.json['city']
            if city == "Null":
                value = 0
            elif city != "":
                UpdateStudent.update_students_city(city, id_student)
                value = 1

        if 'country' in request.json:
            country = request.json['country']
            if country == "Null":
                value = 0
            elif country != "":
                UpdateStudent.update_students_country(country, id_student)
                value = 1

        if 'date_of_birth' in request.json:
            date_of_birth = request.json['date_of_birth']
            if date_of_birth != "":
                UpdateStudent.update_students_date_of_birth(date_of_birth, id_student)
                value = 1

        if 'time_of_studing' in request.json:
            study_time = request.json['time_of_studing']
            print(study_time)
            if study_time != "":
                UpdateStudent.update_students_styding_time(study_time, id_student)
                value = 1

        if 'university' in request.json:
            university = request.json['university']
            if university != "":
                UpdateStudent.update_students_university(university,id_student)
                value = 1

        if 'link' in request.json:
            linked_in = request.json['link']
            if linked_in != "":
                UpdateStudent.update_students_linked_in(linked_in,id_student)
                value = 1

        if 'bio' in request.json:
            about_student = request.json['bio']
            if about_student != "":
                UpdateStudent.update_students_about_student(about_student,id_student)
                value = 1

        if 'CV' in request.json:
            cv = request.json['CV']
            if cv != "":
                UpdateStudent.update_students_cv(cv,id_student)
                value = 1

        if 'email' in request.json:
            email = request.json['email']
            if email != "":
                check_email = UpdateStudent.check_student_email(email)
                if check_email == 1:
                    return jsonify(redirect='false', message='This email is already exist'), 201
                elif check_email == 0:
                    UpdateStudent.update_student_email(id_student, email)
                    value = 1

        if 'new_password' in request.json and 'old_password' in request.json and 'confirm_password' in request.json:
            new_password = request.json['new_password']
            old_password = request.json['old_password']
            confirm_password = request.json['confirm_password']
            if new_password != "" and old_password != "" and confirm_password != "":
                if confirm_password == new_password:
                    value = ChangePasswordStudent.equals_password(old_password, login, new_password)
                    if value == 0:
                        return jsonify(redirect='false', message='Incorrect old password'), 200
                else:
                    return jsonify(redirect='false',message='Password don`t match. Try again....'), 200
        if value == 1:
            return jsonify(redirect='true', redirect_url='/user/student/' + login,message='Save changes.'), 201
        else:
            return jsonify(redirect='false', message='Something bag!!'), 201

    else:
        return 'Please login'