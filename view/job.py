from flask_restful import Resource
from flask import jsonify, request


class JobCreateView(Resource):
    def post(self):
        """
        JOB 생성
        """
        # json 데이터 얻기, 없으면 400 호출
        data = request.get_json()
        return {"hello": "scale"}


class JobView(Resource):
    def get(self, job_id):
        """
        아이디 검색
        """
        return {"hello": "world"}

    def patch(self, job_id):
        """
        데이터 수정
        """
        return {"hello": "world"}

    def delete(self, job_id):
        """
        데이터 삭제
        """
        return {"hello": "world"}
