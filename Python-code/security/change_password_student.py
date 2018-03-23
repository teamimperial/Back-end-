from werkzeug.security import check_password_hash, generate_password_hash
from setting.config import mysql


class ChangePasswordStudent:
    @classmethod
    def equals_password(cls, new_password, id_student):
        connect = mysql.connect()
        cursor = connect.cursor()

        password_enc = generate_password_hash(new_password)

        query = ('update students set password = %s where idStudents=%s')
        param = (password_enc, id_student)

        cursor.execute(query, param)

        connect.comit()
        cursor.close()
