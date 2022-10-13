import os
import sys
import json

from pytest import fixture

CWD = os.path.dirname(__file__)

@fixture(scope='session')
def load_json():
    def _load(_filename):
        with open(
                file=os.path.join(CWD, 'fixtures', _filename),
                mode='r',
                encoding='utf-8'
        ) as json_file:
            return json.load(json_file)
    return _load

def pytest_configure():
    sys.path.append(os.path.join(os.getcwd(), 'shared_layer'))
