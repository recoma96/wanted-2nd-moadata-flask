from flask_restful import Resource
from flask import request, Response
from utils.jobdatabase import JobDatabaseEngine


class JobCreateView(Resource):
    def post(self):
        """
        JOB 생성
        """
        res, success, err = JobDatabaseEngine().save(request.get_json())
        if not success:
            # 유효성 실패
            return Response({'error', str(err)},
                            status=400,
                            mimetype='application/json')
        return Response({'error': 'success'},
                        status=201,
                        mimetype='application/json')


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


class JobRunView(Resource):
    def get(self, job_id):
        return  {"hello": "world"}