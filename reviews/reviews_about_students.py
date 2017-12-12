from setting.config import mysql
from flask import Blueprint, request, abort


class ReviewsAboutStudents:
    def __int__(self, id_students):
        self.id_students = id_students

    @classmethod
    def create_reviews_about_students_in_table(cls, reviews_text):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_create = 'insert into ReviewsAboutStudents(ReviewAboutStudent) values(%s)'
        param_create = (reviews_text)
        cursor.execute(query_create, param_create)

        connect.commit()
        cursor.close()

    @classmethod
    def create_reviews_about_students_in_connect(idStudents, idCompany, idReviewsAboutStudents):
        connect = mysql.connect()
        cursor = connect.cursor()

        query_create = 'insert into StudentsCompanyReviews(idReviewAboutStudents,idCompany,idStudents) values(%s,%s,%s)'
        param_create = (idReviewsAboutStudents, idCompany, idStudents)
        cursor.execute(query_create, param_create)

        connect.commit()
        cursor.close()


create_reviews_about_students = Blueprint("create_reviews_about_students", __name__)


@create_reviews_about_students.route("/create/reviews", methods=['POST'])
def create_reviews_about_students_api():
    if not request.json:
        abort(400)
