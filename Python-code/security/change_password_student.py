from werkzeug.security import check_password_hash, generate_password_hash
from setting.config import mysql
from users.get_student import GetStudent


class ChangePasswordStudent:
    @classmethod
    def equals_password(cls, password, login, new_password):
        value = ChangePasswordStudent.check_password(login, password)
        print(value)
        if value == 1:
            connect = mysql.connect()
            cursor = connect.cursor()

            password_enc = generate_password_hash(new_password)
            id_student = GetStudent.get_students_id_from_db(login)

            query = 'update students SET StudentsPassword = %s WHERE idStudents = %s'
            param = (password_enc, id_student)
            cursor.execute(query, param)

            response_value = value

            connect.commit()
            cursor.close()

        else:
            response_value = value

        return response_value

    @classmethod
    def check_password(cls, login, password):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'select StudentsPassword from students where StudentsLogin=%s'
        param = (login)
        cursor.execute(query, param)
        password_from_db = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        if check_password_hash(password_from_db, password):
            value = 1
        else:
            value = 0

        return value
