from flask_restful import Resource
from flask import request
from utils.job_database import JobDatabaseEngine


class JobCreateView(Resource):
    """
    Job 생성 View

    (POST)  /api/job/create     Job 생성
    """

    def post(self):
        job_id, success, err = JobDatabaseEngine().save(request.get_json())
        if not success:
            # 유효성 실패
            return {'error': str(err)}, 400
        return {'job_id': job_id}, 201


class JobView(Resource):
    """
    Job 데이터 관리 뷰

    (GET)       /api/job/<int:job_id>   Job 정보 검색
    (PATCH)     /api/job/<int:job_id>   Job 수정
    (DELETE)    /api/job/<int:job_id>   Job 삭제
    """

    def get(self, job_id):
        res_data, success, err = JobDatabaseEngine().get_item(job_id)
        return ({'err': 'Data Not Found'}, 404) if err else (res_data, 200)

    def patch(self, job_id):
        success, err = JobDatabaseEngine().update(job_id, request.get_json())
        if not success and err:
            # Error가 발생한 경우
            return {'error': str(err)}, 400
        elif not success and not err:
            # job_id에 해당되는 데이터를 못찾은 경우
            return {'error': 'job_id not found'}, 404
        else:
            # 성공
            return {'error': 'success'}, 201

    def delete(self, job_id):
        success, err = JobDatabaseEngine().remove(job_id)
        if err:
            # 내부 에러
            return ({'err': str(err)}), 400
        else:
            return \
                ({'err': 'data not found'}, 404) if not success \
                else ({'deleted': job_id}, 204)


class JobRunView(Resource):
    def get(self, job_id):
        try:
            JobDatabaseEngine().run(job_id)
        except ValueError as e:
            print(e)
            return {'err': 'job not found'}, 404
        return {'status': 'ok'}, 200
