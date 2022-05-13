from flask import Flask
from flask_restful import Resource, Api
from view.job import JobView, JobCreateView

def get_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(JobView, '/api/job/<int:job_id>')
    api.add_resource(JobCreateView, '/api/job/create')

    return app, api


def main():
    app, api = get_app()
    app.run(debug=True)


if __name__ == '__main__':
    main()