import pytest
import requests
from pytest_bdd import scenarios, given, when, then, parsers
import json

from tests.conftest import BASE_URL, LOG_FILE

booking_id_to_find = 0

# Arrange == Given
# Act == When
# Assert == Then

# TEST CONFIG


# Load all scenarios from the feature file
scenarios(
    "../features/01restful_booker_api_ping.feature",
    "../features/02restful_booker_api_auth.feature",
    "../features/04restful_booker_api_get_booking.feature",
    "../features/03restful_booker_api_create_booking.feature"
)


# object used by pytest fixture to share the API response
class Api:
    def __init__(self, booking_id, firstname, lastname, totalprice, depositpaid, checkin_date, checkout_date,
                 additional_needs):
        self.booking_id = booking_id
        self.firstname = firstname
        self.lastname = lastname
        self.totalprice = totalprice
        self.depositpaid = depositpaid
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.additional_needs = additional_needs


@pytest.fixture
def api():
    # test line for setting values at moment
    return Api("100", "jason", "dynesey2", 99, "True", "2024-01-01", "2024-09-09", "big breakfast")


# GIVEN steps
@given(parsers.parse('the Restful Booker API is online'))
def check_ok():
    pass


# WHEN steps
@when(parsers.parse('a ping GET request is sent'))
def get_auth_api_call(api):
    api.url_string = BASE_URL + "/ping"
    api_get_request(api)


@when(parsers.parse('a "{api_call_type}" GET booking request filtered by "{criteria}" is sent'))
def get_booking_api_call(api, api_call_type, criteria):
    match api_call_type:
        case "ping":
            api.url_string = BASE_URL + "/ping"

        case "bookings":
            api.url_string = BASE_URL + "/booking"
            # TODO: need to append URL with booking id. No body
            match criteria:
                case "all":
                    # nothing more to add to API call
                    pass

                case "id":
                    # add booking ID to find to URL
                    global booking_id_to_find
                    api.url_string = api.url_string + "/" + str(booking_id_to_find)

                # TODO: Returns all bookings with id (one result)

                case "firstname":
                    api.url_string += "?firstname=" + api.firstname
                # TODO: need to append URL with query param '?firstname=' and value

                case "lastname":
                    api.url_string += "?lastname=" + api.lastname
                # TODO: need to append URL with query param ?lastname={{lastname}}

                case "firstname&lastname":
                    api.url_string += "?firstname=" + api.firstname + "&lastname=" + api.lastname
                # TODO: need to append URL with query param ?firstname={{firstname}}&lastname={{lastname}}

                case "checkinDate":
                    api.url_string += "?checkin=" + api.checkin_date
                # TODO: need to append URL with query param ?checkin={{checkin}}

                case "checkoutDate":
                    api.url_string += "?checkout=" + api.checkout_date
                # TODO: need to append URL with query param ?checkout={{checkout}}

                # case None:
                #     api.url_string = api.url_string + "/invalid"

        case _:
            api.url_string = "value not set"
            # if this assertion fails then there is no case statement for the request option defined in BDD
            assert api.url_string != "value not set"

    api_get_request(api)


@when(parsers.parse('a "auth" POST request is sent with Valid "{user_name}" and "{password}"'))
@when(parsers.parse('a "auth" POST request is sent with Invalid "{user_name}" and "{password}"'))
def api_token(api, user_name, password):
    api.url_string = BASE_URL + "/auth"
    # create body data with user name and pwd
    api.data = {'username': user_name, 'password': password}
    api_post_request(api)


# When a "create_booking" POST request is sent
# booking_id, firstname, lastname, checkin_date, checkout_date, additional_needs
@when(parsers.parse('a "create_booking" POST request is sent'))
# TODO Add post request for create booking
def api_create_booking(api):
    api.url_string = BASE_URL + "/booking"
    # create body data with booking details
    api.header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    api.data = {"firstname": api.firstname,
                "lastname": api.lastname,
                "totalprice": api.totalprice,
                "depositpaid": api.depositpaid,
                "bookingdates": {"checkin": api.checkin_date, "checkout": api.checkout_date},
                "additional_needs": api.additional_needs,
                }
    api.response = requests.post(api.url_string, json=api.data, headers=api.header)
    api_post_request(api)


def api_get_request(api):
    api.header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    api.response = requests.get(api.url_string, headers=api.header)
    file = open(LOG_FILE, "a")
    file.write(
        "Test response for " + api.url_string + "\n" + api.response.text + "\n" + "Response time: " + str(
            api.response.elapsed.total_seconds()) + "\n\n")
    file.close()
    api.url_string = None
    # check booking ID in response


def api_post_request(api):
    # # check whether API GET request needs to send a body and that exists in API object
    if hasattr(api, 'data'):
        api.header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        api.response = requests.post(api.url_string, json=api.data, headers=api.header)
    else:
        api.response = requests.post(api.url_string)
    file = open(LOG_FILE, "a")
    file.write(
        "url: " + api.url_string + "\nrequest body: " + str(api.data) +
        "\nTest response for " + api.url_string + "\n" + api.response.text + "\n" + "Response time: " + str(
            api.response.elapsed.total_seconds()) + "\n\n")
    file.close()
    api.url_string = None


# THEN Steps
@then(parsers.parse('the response status code is "{code:d}"'))
def api_response_code(api, code):
    assert (api.response.status_code == code)


@then(parsers.parse('the response contains "{content}"'))
def response_body(api, content):
    assert content in api.response.text


@then(parsers.parse('the response time is less than "{num:d}"ms'))
def check_response_time(api, num):
    print("time is " + str(api.response.elapsed.total_seconds))
    assert api.response.elapsed.total_seconds() / 1000 < num

    # And the response contains all bookings

    # And the response contains bookings filtered by "id"


####################################################################################
@then(parsers.parse('the response contains all bookings'))
def check_all_bookings(api):
    json_msg = api.response.json()
    global booking_id_to_find
    count = 0
    for item in json_msg:
        count += 1
        if booking_id_to_find == item["bookingid"]:
            # original create booking in dataset
            assert booking_id_to_find == item["bookingid"]
            return
    assert item["bookingid"] == booking_id_to_find


####################################################################################

@then(parsers.parse('the response contains bookings filtered by "id"'))
def check_booking_by_id(api):
    global booking_id_to_find
    assert api.response.json() == {
        'bookingdates': {'checkin': api.checkin_date,
                         'checkout': api.checkout_date},
        'depositpaid': True,
        'firstname': api.firstname,
        'lastname': api.lastname,
        'totalprice': api.totalprice}


@then(parsers.parse('the response contains bookings filtered by "firstname"'))
@then(parsers.parse('the response contains bookings filtered by "lastname"'))
@then(parsers.parse('the response contains bookings filtered by "firstname&lastname"'))
@then(parsers.parse('the response contains bookings filtered by "firstname"'))
@then(parsers.parse('the response contains bookings filtered by "checkin"'))
@then(parsers.parse('the response contains bookings filtered by "checkout"'))
# TODO: refactor to check results contain results based on firstname, lastname etc. ******************
def check_booking_in_result(api):
    json_msg = api.response.json()
    global booking_id_to_find
    # loops through response to see if any items match
    for item in json_msg:
        # booking_id_to_find = 999
        if item["bookingid"] == booking_id_to_find:
            assert item["bookingid"] == booking_id_to_find
            return
    assert item["bookingid"] == booking_id_to_find


@then(parsers.parse('a booking id is returned'))
def check_booking_by_id(api):
    json_msg = api.response.json()
    global booking_id_to_find
    booking_id_to_find = json_msg["bookingid"]
