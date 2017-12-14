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
        result = cursor.execute(query_get_id,param_get_id)
        if result == 0:
            id = 0
        else:
            id = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return id

    @classmethod
    def get_company_city(cls, id_copmany):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_id = 'select City from infoaboutcompany where idCompany=%s'
        param_get_id = (id_copmany)
        cursor.execute(query_get_id, param_get_id)
        city = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return city

    @classmethod
    def get_company_web_site(cls, id_copmany):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_id = 'select WebSite from infoaboutcompany where idCompany=%s'
        param_get_id = (id_copmany)
        cursor.execute(query_get_id, param_get_id)
        web_site = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return web_site

    @classmethod
    def get_company_country(cls, id_copmany):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_id = 'select Country from infoaboutcompany where idCompany=%s'
        param_get_id = (id_copmany)
        cursor.execute(query_get_id, param_get_id)
        country = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return country

    @classmethod
    def get_about_company(cls, id_copmany):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_id = 'select AboutCompany from infoaboutcompany where idCompany=%s'
        param_get_id = (id_copmany)
        cursor.execute(query_get_id, param_get_id)
        about = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return about

    @classmethod
    def get_photo_company(cls, id_copmany):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_get_id = 'select Photo from infoaboutcompany where idCompany=%s'
        param_get_id = (id_copmany)
        cursor.execute(query_get_id, param_get_id)
        photo = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return photo

    @classmethod
    def get_check_company(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'select Company_Check from Company where CompanyLogin = %s'
        param = (login)
        cursor.execute(query, param)
        check = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return check

    @classmethod
    def get_password_company(cls, login):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'select CompanyPassword from Company where CompanyLogin = %s'
        param = (login)
        cursor.execute(query,param)
        password = cursor.fetchone()[0]

        connect.commit()
        cursor.close()

        return password