from flask_restful import Resource
from flask import request, Response, jsonify
from utils.jobdatabase import JobDatabaseEngine


class JobCreateView(Resource):
    def post(self):
        """
        JOB 생성
        """
        job_id, success, err = JobDatabaseEngine().save(request.get_json())
        if not success:
            # 유효성 실패
            return {"error": str(err)}, 400
        return {'job_id': job_id}, 201


class JobView(Resource):
    def get(self, job_id):
        """
        아이디 검색
        """
        res_data, success, err = JobDatabaseEngine().get_item(job_id)
        return ({"err": "Data Not Found"}, 404) if err else (res_data, 200)

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


class JobRunView(Resource):
    def get(self, job_id):
        return {"hello": "world"}
