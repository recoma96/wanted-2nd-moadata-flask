import pytest
from api import get_app, generate_jobdatabase_engine
import json

API = '/api/job'

example_job = {
    'job_name': 'Job1',
    'task_list': {
        'R1': ['R2', 'W1'],
        'R2': ['W1', 'W2'],
        'W1': ['W2'],
        'W2': [],
    },
    'property': {
        'R1': {'task_name': 'read', 'filename': 'a.csv', 'sep': ','},
        'R2': {'task_name': 'read', 'filename': '1.csv', 'sep': ','},
        'W1': {'task_name': 'write', 'filename': 'a.csv', 'sep': ','},
        'W2': {'task_name': 'write', 'filename': 'b.csv', 'sep': ','},
    }
}


@pytest.fixture
def api():
    app, api = get_app()

    # 데이터 하나 올리기
    res = api.post(
        API, data=json.dumps(example_job),
        content_type='application/json'
    )
    assert res.status_code == 201

    yield app.test_client()

    # 테스트 종료 후에 실행되는 코드
    # Job.json에 있는 내용들을 전부 지운다.
    generate_jobdatabase_engine().reset()
