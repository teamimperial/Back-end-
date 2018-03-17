from flask import Blueprint, render_template
from setting.config import mysql


class GetStudentStatement:
    def __init__(self):
        pass

    @classmethod
    def get_student_statement(cls, id_course):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'Select students.idStudents, students.StudentsName, students.StudentsLastName ' \
                'from students, student_apply where students.idStudents=student_apply.idStudents ' \
                'and student_apply.idCourse = %s;'

        param = id_course
        cursor.execute(query, param)

        result = cursor.fetchall()
        return result


approve_student = Blueprint('approve_student', __name__)


@approve_student.route('/list_of_statement/<id_course>')
def list_of_statement(id_course):
    print(id_course)
    students = GetStudentStatement.get_student_statement(id_course)
    print(students)
    list_of_students = []
    for student in students:
        student_name = student[1]
        student_last_name = student[2]
        student = {
            'student_name': student_name,
            'student_last_name': student_last_name
        }
        list_of_students.append(student)

    return render_template('applications-c.html', students=list_of_students)