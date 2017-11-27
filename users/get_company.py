from setting.config import mysql


class GetCompany:
    def __int__(self, login):
        self.login = login

    @classmethod
    def get_company_name_from_db(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_name = 'select CompanyName from company where CompanyLogin=%s'
        param_get_name = (login)
        cursor.execute(query_get_name, param_get_name)
        name = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return name

    @classmethod
    def get_company_email_from_db(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_email = 'select CompanyEmail from company where CompanyLogin=%s'
        param_get_email = (login)
        cursor.execute(query_get_email, param_get_email)
        email = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return email

    @classmethod
    def get_company_id_from_db(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_id = 'select idCompany from company where CompanyLogin=%s'
        param_get_id = (login)
        cursor.execute(query_get_id,param_get_id)
        id = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return id