import requests
from pytest_bdd import scenarios, given, then, parsers, when

CAFE_API = "http://127.0.0.1:5000"
CAFE_API_SEARCH = "http://127.0.0.1:5000/search?loc="

scenarios('..//features/cafe_api.feature')


@given(parsers.parse('the customer queries the API using the GET /search with query loc={location}'),
       target_fixture="request_result")
def search_location_response(location):
    url = f'{CAFE_API_SEARCH}{location}'
    response = requests.get(url)
    print(location)
    print(f'\nRESPONSE IS: {response.json()}\n')
    return response.status_code


@when(parsers.parse('the cafe location exists in the database'))
def check_cafe_in_db():
    pass


@then(parsers.parse('the response status is {expected_response_code:d}'))
def check_resp_code(expected_response_code, request_result):
    print(expected_response_code, request_result)
    assert request_result == expected_response_code


@then('correct number of calculated results are returned')
def check_num_results():
    pass


@when(parsers.parse('the cafe location does not exist in the database'))
def check_cafe_in_db():
    pass
