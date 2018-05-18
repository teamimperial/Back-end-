from flask import Blueprint, request, abort, session, jsonify
from setting.config import mysql

class DeleteReviewCompany:

    def __init__(self):
        pass

    @classmethod
    def delete_company_review(cls, id_review, id_course):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'DELETE FROM coursereviews WHERE coursereviews.id_course_reviews=%s and coursereviews.idCourse=%s'
        param = (id_review, id_course)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()


delete_comment_company = Blueprint('delete_comment_company',__name__)


@delete_comment_company.route('/delete/comment/company', methods=['POST'])
def delete_comment_about_company():
    if 'company' in session:
        if not request.json or 'review_id' not in request.json or 'course_id' not in request.json:
            return abort(400)
        else:
            id_review = request.json['review_id']
            id_course = request.json['course_id']
            DeleteReviewCompany.delete_company_review(id_review, id_course)
        return jsonify(status='deleted'), 200
    else:
        return jsonify('Please log in'), 200
