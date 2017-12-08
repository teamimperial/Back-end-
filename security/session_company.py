from flask import session


class CompanySession:
    @classmethod
    def check_in_session_company(cls):
        value = 0
        if 'company' in session:
            login_company = session['company']
            return login_company
        else:
            return value

    @classmethod
    def delete_session_company(cls):
        session.pop('company', None)