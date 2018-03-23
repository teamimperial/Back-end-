from flask import session


class GetSessionStudent:
    @classmethod
    def api_get_student_session(cls):
        if 'student' in session:
            result = session['student']
        else:
            result = 0

        return result


class GetSessionCompany:
    @classmethod
    def api_get_company_session(cls):
        if 'company' in session:
            login_company = session['company']
            result = login_company
        else:
            result = 0

        return result
