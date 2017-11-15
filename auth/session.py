from flask import Session


class UserSession:
    def __int__(self, login):
        self.login = login

    @classmethod
    def create_session_student(cls, login):
        Session['student'] = login
