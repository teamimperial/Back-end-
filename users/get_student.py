from setting.config import mysql


class GetStudent:
    def __int__(self, login):
        self.login = login

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

        query_get_first_name = 'select StudentsName from students where StudentsLogin=%s'
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

        query_get_last_name = 'select StudentsLastName from students where StudentsLogin=%s'
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

        query_get_email = 'select StudentsEmail from students where StudentsLogin=%s'
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

        query = 'select City from infoaboutstudent where idStudents=%s'
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

        query = 'select Country from infoaboutstudent where idStudents=%s'
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

        query = 'select DateOfBirth from infoaboutstudent where idStudents=%s'
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

        query = 'select University from infoaboutstudent where idStudents=%s'
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

        query = 'select TimeOfStyding from infoaboutstudent where idStudents=%s'
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

        query = 'select LinkToLinkedIn from infoaboutstudent where idStudents=%s'
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

        query = 'select AboutStudent from infoaboutstudent where idStudents=%s'
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

        query = 'select Photo from infoaboutstudent where idStudents=%s'
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

        query = 'select CV from infoaboutstudent where idStudents=%s'
        param = (id_student)
        cursor.execute(query, param)
        cv = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return cv