from setting.config import mysql
from flask import Blueprint, request, abort, jsonify
from users.get_student import GetStudent


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


update_students = Blueprint('update_students', __name__)


@update_students.route('/student/update', methods=['POST'])
def api_update_students():
    value = 0

    if not request.json and 'login' not in request.json:
        abort(404)

    login = request.json['login']
    id_student = GetStudent.get_students_id_from_db(login)

    if 'Photo' in request.json:
        photo = request.json['Photo']
        UpdateStudent.update_students_photo(photo,id_student)
        value = 1

    if 'City' in request.json:
        city = request.json['City']
        UpdateStudent.update_students_city(city, id_student)
        value = 1

    if 'Country' in request.json:
        country = request.json['Country']
        UpdateStudent.update_students_country(country, id_student)
        value = 1

    if 'DateOfBirth' in request.json:
        date_of_birth = request.json['DateOfBirth']
        date = date_of_birth.split('.')
        day = date[0]
        month = date[1]
        year = date[2]
        time = year + "." + month + "." + day
        UpdateStudent.update_students_date_of_birth(time,id_student)
        value = 1

    if 'StudyTime' in request.json:
        styding_time=request.json['StudyTime']
        UpdateStudent.update_students_styding_time(styding_time, id_student)
        value=1

    if 'University' in request.json:
        university = request.json['University']
        UpdateStudent.update_students_university(university,id_student)
        value = 1

    if 'LinkedIn' in request.json:
        linked_in = request.json['LinkedIn']
        UpdateStudent.update_students_linked_in(linked_in,id_student)
        value = 1

    if 'AboutStudent' in request.json:
        about_student = request.json['AboutStudent']
        UpdateStudent.update_students_about_student(about_student,id_student)
        value = 1

    if 'CV' in request.json:
        cv = request.json['CV']
        UpdateStudent.update_students_cv(cv,id_student)
        value = 1

    if value == 1:
        return jsonify(status="success"), 201

    else:
        return jsonify(status="something bad"), 404