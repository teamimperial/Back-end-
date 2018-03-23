from werkzeug.security import check_password_hash, generate_password_hash
from setting.config import mysql
from flask import jsonify
from users.get_company import GetCompany


class ChangePasswordCompany:
    @classmethod
    def equals_password(cls, password, login, new_password):
        value = ChangePasswordCompany.check_password(login, password)
        print(value)
        if value == 1:
            connect = mysql.connect()
            cursor = connect.cursor()

            password_enc = generate_password_hash(new_password)
            id_company = GetCompany.get_company_id_from_db(login)

            query = 'update company SET CompanyPassword = %s WHERE idCompany = %s'
            param = (password_enc, id_company)
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

        query = 'select CompanyPassword from company where CompanyLogin=%s'
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
