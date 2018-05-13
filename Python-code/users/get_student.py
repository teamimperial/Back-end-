from setting.config import mysql


class GetStudent:
    def __init__(self):
        pass

    @classmethod
    def get_students_id_from_db(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_id = 'SELECT idStudents FROM students WHERE StudentsLogin=%s'
        param_get_id = (login)
        result = cursor.execute(query_get_id, param_get_id)
        if result == 0:
            id_students = 0
        else:
            id_students = str(cursor.fetchone()[0])
        connect.commit()
        cursor.close()

        return id_students

    @classmethod
    def get_student_first_name_from_db(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_first_name = 'SELECT StudentsName FROM students WHERE StudentsLogin=%s'
        param_get_first_name = (login)
        cursor.execute(query_get_first_name, param_get_first_name)
        firstName = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return firstName

    @classmethod
    def get_student_last_name_from_db(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_last_name = 'SELECT StudentsLastName FROM students WHERE StudentsLogin=%s'
        param_get_last_name = (login)
        cursor.execute(query_get_last_name, param_get_last_name)
        last_name = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return last_name

    @classmethod
    def get_student_email_from_db(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_email = 'SELECT StudentsEmail FROM students WHERE StudentsLogin=%s'
        param_get_email = (login)
        cursor.execute(query_get_email, param_get_email)
        email = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return email

    @classmethod
    def get_student_city_from_db(cls, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT City FROM infoaboutstudent WHERE idStudents=%s'
        param = (id_student)
        cursor.execute(query, param)
        city = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return city

    @classmethod
    def get_student_country_from_db(cls, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT Country FROM infoaboutstudent WHERE idStudents=%s'
        param = (id_student)
        cursor.execute(query, param)
        country = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return country

    @classmethod
    def get_student_date_of_birth_from_db(cls, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT DateOfBirth FROM infoaboutstudent WHERE idStudents=%s'
        param = (id_student)
        cursor.execute(query, param)
        date_of_birth = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return date_of_birth

    @classmethod
    def get_student_university_from_db(cls, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT University FROM infoaboutstudent WHERE idStudents=%s'
        param = (id_student)
        cursor.execute(query, param)
        university = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return university

    @classmethod
    def get_student_time_of_study_from_db(cls, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT TimeOfStyding FROM infoaboutstudent WHERE idStudents=%s'
        param = (id_student)
        cursor.execute(query, param)
        time_of_study = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return time_of_study

    @classmethod
    def get_student_linked_in_from_db(cls, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT LinkToLinkedIn FROM infoaboutstudent WHERE idStudents=%s'
        param = (id_student)
        cursor.execute(query, param)
        link = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return link

    @classmethod
    def get_student_about_from_db(cls, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT AboutStudent FROM infoaboutstudent WHERE idStudents=%s'
        param = (id_student)
        cursor.execute(query, param)
        about = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return about

    @classmethod
    def get_student_photo_from_db(cls, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT Photo FROM infoaboutstudent WHERE idStudents=%s'
        param = (id_student)
        cursor.execute(query, param)
        photo = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return photo

    @classmethod
    def get_student_cv_from_db(cls, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT CV FROM infoaboutstudent WHERE idStudents=%s'
        param = (id_student)
        cursor.execute(query, param)
        cv = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return cv

    @classmethod
    def get_students_password_from_db(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_id = 'SELECT idStudents FROM students WHERE StudentsLogin=%s'
        param_get_id = (login)
        cursor.execute(query_get_id, param_get_id)

        password = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return password

    @classmethod
    def get_info_about_student_for_review(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT students.StudentsName, students.StudentsLastName, students.StudentsEmail, ' \
                'infoaboutstudent.Photo, infoaboutstudent.City, infoaboutstudent.Country, ' \
                'infoaboutstudent.DateOfBirth, infoaboutstudent.University, ' \
                'infoaboutstudent.TimeOfStyding, infoaboutstudent.LinktoLinkedIN, ' \
                'infoaboutstudent.AboutStudent, infoaboutstudent.CV FROM students, ' \
                'infoaboutstudent WHERE infoaboutstudent.idStudents=students.idStudents ' \
                'AND students.StudentsLogin = %s'

        param = login
        cursor.execute(query, param)
        student = cursor.fetchone()

        connect.commit()
        cursor.close()

        return student

    @classmethod
    def get_comment_about_student(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT studentsreviews.review, studentsreviews.time, company.CompanyName FROM company, students, studentsreviews WHERE studentsreviews.idCompany = company.idCompany AND students.idStudents= studentsreviews.idStudents AND students.StudentsLogin = %s order by studentsreviews.idStudentsCompanyReviews DESC'
        param = login
        cursor.execute(query, param)
        reviews = cursor.fetchall()

        connect.commit()
        cursor.close()

        return reviews
