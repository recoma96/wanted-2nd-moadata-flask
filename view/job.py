from flask_restful import Resource
from flask import request, Response
from utils.validator_chains import get_job_validator_chain


class JobCreateView(Resource):
    def post(self):
        """
        JOB 생성
        """
        # json 데이터 얻기, 없으면 400 호출
        data = request.get_json()
        validator = get_job_validator_chain()
        is_valid, err = validator(data)
        if not is_valid:
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
