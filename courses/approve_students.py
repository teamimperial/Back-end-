from flask import Blueprint, render_template
from setting.config import mysql


class GetStudentStatement:
    def __init__(self):
        pass

    @classmethod
    def get_student_statement(cls, id_course):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'Select students.idStudents, students.StudentsName, students.StudentsLastName, ' \
                'students.StudentsLogin from students, student_apply where ' \
                'students.idStudents=student_apply.idStudents ' \
                'and student_apply.idCourse = %s;'

        param = id_course
        cursor.execute(query, param)

        result = cursor.fetchall()
        return result


approve_student = Blueprint('approve_student', __name__)


@approve_student.route('/list_of_statement/<id_course>')
def list_of_statement(id_course):
    students = GetStudentStatement.get_student_statement(id_course)
    list_of_students = []
    for student in students:
        student_name = student[1]
        student_last_name = student[2]
        student_login = student[3]
        student = {
            'student_name': student_name,
            'student_last_name': student_last_name,
            'student_login': "/student/review/" + student_login
        }
        list_of_students.append(student)

    return render_template('applications-c.html', students=list_of_students)


class StudentApplication:
    def __init__(self):
        pass

    @classmethod
    def set_apply_status_DB(id_apply, status):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'insert into student_apply(Apply_Status) values(%s) where idStudent_Apply = %s'
        param = (int(status), int(id_apply))

        cursor.execute(query, param)

        connect.commit()
        cursor.close()

    @classmethod
    def api_check_status(id_apply):
        connect = mysql.connect()
        cursor = connect.cursor()

        #перевірка, що ще немає статусу; має повернути 1
        query = 'select exists(select * from student_apply where idStudent_Apply = %s and Apply_Status is null)'
        param = int(id_apply)

        cursor.execute(query, param)

        check = cursor.fetchone()[0]

        return check

@set_status_on_apply.route('/set_status', methods=['POST'])
def api_approve_student():
    if 'company' in session and request.json:
        id_apply = request.json['id_apply']
        status = request.json['status']
        check_status = StudentApplication.api_check_status(id_apply)
        if check_status != 1:
            print('bad')
            return 'hello'
        else:
            StudentApplication.set_apply_status_DB(id_apply, status)
            return jsonify(redirect='true', redirect_url='/courses'), 200
