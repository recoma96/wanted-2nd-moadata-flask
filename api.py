from flask import Flask
from flask_restful import Resource, Api
from view.job import JobView, JobCreateView


def main():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(JobView, '/<int:job_id>')
    api.add_resource(JobCreateView, '/create')

    app.run(debug=True)


if __name__ == '__main__':
    main()