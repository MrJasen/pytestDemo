import pytest
from testcases.conftest import api_data
from testcases.conftest import rank_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return api_data.get(testcase_name)

def testcase_rankData(request):
    testcase_name = request.function.__name__
    return rank_data.get(testcase_name)