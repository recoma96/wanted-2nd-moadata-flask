import json
from typing import List, Tuple, Dict, Any

import pytest
from api import get_app, generate_jobdatabase_engine
import pandas as pd

"""
해당 테스트의 목적은
결과 값에 대한 판정이 아닌,
해당 Task Logic에 대한 결과를 관찰하는 데 있다.
추가 요구사항에 대한 기능 튜닝을 목적으로 하며
특수한 경우가 아닌 이상 Task Logic에 대한 assert문은 사용하지 말 것
"""

CREATE_API = '/api/job/create'
RUN_API = '/api/job/run'
STORAGE_ROOT = 'storage/data'


@pytest.fixture
def api():
    app, api = get_app()
    yield app.test_client()

    # 테스트 종류 후 실행되는 코드
    # Job.json에 있는 내용들을 전부 지운다
    generate_jobdatabase_engine().reset()


def save_files(files: List[Tuple[str, pd.DataFrame]]):
    for i in range(len(files)):
        name, data = files[i]
        data.to_csv(f'{STORAGE_ROOT}/{name}', index=False, index_label=False)


def upload_job(job: Dict[str, Any], api):
    res = api.post(CREATE_API, data=json.dumps(job),
                   content_type='application/json')
    assert res.status_code == 201


def test_on_way_root(api):
    """
    READ -> DROP -> WRITE 순으로
    이때 결과값이 반드시 일치하게 나와야 한다
    """

    # Data Setting
    input_file = 'b.scv'
    output_file = 'c.csv'

    input_data = pd.DataFrame({
        'id': [1, 2, 3],
        'title': ['title1', 'title2', 'title3']
    })
    save_files([(input_file, input_data)])
    deleted_column = 'title'

    # Job Setting
    job = {
        'job_name': 'Job1',
        'task_list': {
            'R': ['D'],
            'D': ['W'],
            'W': [],
        },
        'property': {
            'R': {'task_name': 'read', 'filename': input_file, 'sep': ','},
            'D': {'task_name': 'drop', 'column_name': deleted_column},
            'W': {'task_name': 'write', 'filename': output_file, 'sep': ','}
        }
    }
    upload_job(job, api)

    # run
    res = api.get(f'{RUN_API}/1')
    assert res.status_code == 200

    output = pd.read_csv(f'{STORAGE_ROOT}/{output_file}')
    answer = input_data.copy().drop([deleted_column], axis=1)
    assert output.equals(answer) is True
