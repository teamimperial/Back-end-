from flask import Session, Blueprint


class UserSession:
    def __int__(self, login):
        self.login = login


session_user = Blueprint("session_user", __name__)


@session_user.route("/create/session", methods=['POST'])
def create_session_student(cls, login):
    Session['student'] = login
