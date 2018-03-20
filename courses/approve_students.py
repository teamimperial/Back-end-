from flask import Blueprint, render_template, redirect, Markup
from setting.config import mysql


class GetStudentStatement:
    def __init__(self):
        pass

    @classmethod
    def get_student_statement(cls, id_course):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT students.idStudents, students.StudentsName, students.StudentsLastName, ' \
                'students.StudentsLogin, student_apply.status FROM students, student_apply WHERE ' \
                'students.idStudents=student_apply.idStudents ' \
                'AND student_apply.idCourse = %s;'

        param = id_course
        cursor.execute(query, param)

        result = cursor.fetchall()
        return result

    @classmethod
    def set_status_in_db(cls, id_course, id_student, status):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE student_apply SET student_apply.status = %s WHERE student_apply.idStudents = %s ' \
                'AND student_apply.idCourse = %s'

        param = (status, id_student, id_course)
        cursor.execute(query, param)

        connect.commit()
        cursor.close()


approve_student = Blueprint('approve_student', __name__)


@approve_student.route('/list_of_statement/<id_course>')
def list_of_statement(id_course):
    global status_view
    students = GetStudentStatement.get_student_statement(id_course)
    list_of_students = []
    for student in students:
        student_id = student[0]
        student_name = student[1]
        student_last_name = student[2]
        student_login = student[3]
        student_status = student[4]
        confirm = '/confirm/' + str(id_course) + "/" + str(student_id)
        delete = '/delete/' + str(id_course) + "/" + str(student_id)
        if student_status is None:
            status_view = Markup('<div class="col-md-7 button-container " style="text-align: center;">'
                                 '<a href=' + confirm + '><button type="button"><span>Confirm</span>'
                                                        '</button></a> <a href=' + delete + '><button type="button">'
                                                                                            '<span>Delete</span'
                                                                                            '></button></a></div>')
        if student_status == 1:
            status_view = Markup('<div class="col-md-7" style="text-align: center;">'
                                 '<span>ACCEPT</span></div>')
        if student_status == 0:
            continue
        student = {
            'student_name': student_name,
            'student_last_name': student_last_name,
            'student_login': "/student/review/" + student_login,
            'status_view': status_view
        }
        list_of_students.append(student)

    return render_template('applications-c.html', students=list_of_students)


set_status_students_on_course = Blueprint('set_status_students_on_course', __name__)


@set_status_students_on_course.route('/confirm/<id_course>/<id_student>')
def confirm_students_on_course(id_course, id_student):
    status = 1
    GetStudentStatement.set_status_in_db(id_course, id_student, int(status))
    link = '/list_of_statement/' + str(id_course)
    return redirect(link)


@set_status_students_on_course.route('/delete/<id_course>/<id_student>')
def delete_student_on_course(id_course, id_student):
    status = 0
    GetStudentStatement.set_status_in_db(id_course, id_student, int(status))
    link = '/list_of_statement/' + str(id_course)
    return redirect(link)
