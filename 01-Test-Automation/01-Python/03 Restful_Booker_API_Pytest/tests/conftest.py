import requests
from pytest_bdd import scenarios, given, when, then, parsers
import os

# Constants
BASE_URL = "https://restful-booker.herokuapp.com"
LOG_FILE = "logs/restful_booker_api_response.json"

# File cleanup
if os.path.exists(LOG_FILE):
    print("file deleted")
    os.remove(LOG_FILE)


# Hooks
# def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
#     print(f'Step failed: {step}')

# Fixtures

# @pytest.fixture
# TODO: any fixtures for setup and teardown

# Shared Given Steps
# enter any shared Given steps here
