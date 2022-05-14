from flask_restful import Resource
from flask import request, Response, jsonify
from utils.jobdatabase import JobDatabaseEngine


class JobCreateView(Resource):
    """
    Job 생성 View

    (POST)  /api/job/create     Job 생성
    """
    def post(self):
        """
        JOB 생성
        """
        job_id, success, err = JobDatabaseEngine().save(request.get_json())
        if not success:
            # 유효성 실패
            return {'error': str(err)}, 400
        return {'job_id': job_id}, 201


class JobView(Resource):
    """
    Job 데이터 관리 뷰

    (GET)       /api/job/<int:job_id>   Job 정보 얻기
    (PATCH)     /api/job/<int:job_id>   Job 수정
    (DELETE)    /api/job/<int:job_id>   Job 삭제
    """
    def get(self, job_id):
        """
        아이디 검색
        """
        res_data, success, err = JobDatabaseEngine().get_item(job_id)
        return ({'err': 'Data Not Found'}, 404) if err else (res_data, 200)

    def patch(self, job_id):
        """
        데이터 수정
        """
        return {'hello': 'world'}

    def delete(self, job_id):
        """
        데이터 삭제
        """
        success, err = JobDatabaseEngine().remove(job_id)
        if err:
            return ({'err': str(err)}), 400
        else:
            return                                              \
                ({'err': 'data not found'}, 404) if not success \
                else ({'deleted': job_id}, 204)


class JobRunView(Resource):
    def get(self, job_id):
        return {'hello': 'world'}
