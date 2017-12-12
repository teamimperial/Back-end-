from werkzeug.security import check_password_hash, generate_password_hash
from setting.config import mysql


class ChangePasswordCompany:
    @classmethod
    def equals_password(cls, password, password_from_db, login, new_password):
        if check_password_hash(password_from_db, password):
            connect = mysql.connect()
            cursor = connect.cursor()

            enc_password = generate_password_hash(new_password)

            query = ('update company set password = %s where CompanyLogin=%s')
            param = (enc_password, login)

            cursor.execute(query, param)

            connect.comit()
            cursor.close()
