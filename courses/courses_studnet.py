from flask import Blueprint, render_template, session, redirect
from setting.config import mysql
from users.get_student import GetStudent

courses_student = Blueprint('courses_student', __name__)


class GetApplyStudentCourse:
    @classmethod
    def get_courses_student(cls, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'select company.CompanyName, company.CompanyLogin, courses.idCourse, ' \
                'courses.idCompany, courses.CoursesName, courses.CoursesAmount, courses.CoursesCity, ' \
                'courses.CoursesCountry, courses.CoursesStart, courses.CoursesEnd, courses.CoursesInfo, ' \
                'courses.CoursesStatus from courses, company, student_apply where ' \
                'student_apply.idCourse=courses.idCourse and courses.idCompany=company.idCompany and ' \
                'student_apply.idStudents=%s order by idStudent_Apply DESC'
        param = (id_student)

        cursor.execute(query, param)

        result = cursor.fetchall()

        connect.commit()
        cursor.close()

        return result


@courses_student.route('/student/course', methods=['GET'])
def api_student_courses():
    if 'student' in session:
        student_login = session['student']
        id_student = GetStudent.get_students_id_from_db(student_login)
        courses = GetApplyStudentCourse.get_courses_student(id_student)
        result = []
        for course in courses:
            student_courses = {
                'company_name': course[0], 'company_login': course[1], 'course_name': course[4], 'amount': course[5],
                'city': course[6], 'country': course[7], 'date_of_start': course[8], 'date_of_end': course[9],
                'info': course[10], 'status': course[11], 'link': '/course/!' + str(course[2]) + '/!' + str(course[3])
            }
            result.append(student_courses)
        print(result)
        return render_template('courses-s.html', courses=result), 200
    else:
        return redirect('/'), 200
