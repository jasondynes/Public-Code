"""
This module contains step definitions for service.feature.
It uses the requests package:
http://docs.python-requests.org/
"""

import requests

from pytest_bdd import scenarios, given, then, parsers


# Shared Variables

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'


# Scenarios

scenarios('../features/duckduckgo_api.feature', example_converters=dict(phrase=str))


# Given Steps

@given('the DuckDuckGo API is queried with "<phrase>"')
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    file = open("api_response.json", "a")
    file.write("Test result for DuckDuckGo phrase search of " + phrase + " :\n" + response.text + "\n")
    file.close()
    return response

# Then Steps

@then('the response contains results for "<phrase>"')
def ddg_response_contents(ddg_response, phrase):
    # A more comprehensive test would check 'RelatedTopics' for matching phrases
    assert phrase.lower() == ddg_response.json()['Heading'].lower()

@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code
