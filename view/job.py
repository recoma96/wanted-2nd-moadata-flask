from flask_restful import Resource, Api

class JobCreateView(Resource):
    def post(self):
        """
        JOB 생성
        """
        return {"hello": "scale"}

class JobView(Resource):
    def get(self):
        """
        아이디 검색
        """
        return {"hello": "world"}

    def patch(self):
        """
        데이터 수정
        """
        return {"hello": "world"}

    def delete(self):
        """
        데이터 삭제
        """
        return {"hello": "world"}