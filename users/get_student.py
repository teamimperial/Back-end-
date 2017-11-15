from setting.config import mysql


class GetStudent:
    def __int__(self, login):
        self.login = login

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
