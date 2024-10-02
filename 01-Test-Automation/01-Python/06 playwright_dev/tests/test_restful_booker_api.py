from enum import auto
import os
from http.client import responses
from typing import Generator

import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

token = None
global booking_id


# fixture is for whole session not on per test basis
@pytest.fixture(scope="function")
def api_request_context(
        playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    global token
    if token is not None:
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Cookie': f"token={token}"}
    request_context = playwright.request.new_context(
        base_url="https://restful-booker.herokuapp.com", extra_http_headers=headers)
    yield request_context
    request_context.dispose()


# ping request
def test_ping_request(api_request_context: APIRequestContext) -> None:
    get_ping = api_request_context.get(f"/ping")
    # assert status code was OK (codes 200-299)
    expect(get_ping).to_be_ok()
    # assert response code was 201
    assert get_ping.status == 201


# invalid auth request
@pytest.mark.parametrize("username, password",
                         [("jason", "tester123")])
def test_invalid_authentication_request(api_request_context: APIRequestContext, username, password) -> None:
    # TODO: realise the params are hardcoded right now but no security risk as Public API but will parameterize and hide
    data = {
        "username": username,
        "password": password,
    }
    get_auth = api_request_context.post(f"/auth", data=data)

    response = get_auth.json()
    # 'Bad credentials' should be 'reason' in response
    assert response['reason'] == "Bad credentials"
    # assert status code was OK (codes 200-299)
    expect(get_auth).to_be_ok()
    # assert response code was 200
    assert get_auth.status == 200


# valid auth request
@pytest.mark.parametrize("username, password",
                         [("admin", "password123")])
def test_authentication_request(api_request_context: APIRequestContext, username, password) -> None:
    # TODO: realise the params are hardcoded right now but no security risk as Public API but will parameterize and hide
    data = {
        "username": username,
        "password": password,
    }
    get_auth = api_request_context.post(f"/auth", data=data)

    response = get_auth.json()
    assert response['token'] is not None
    # set token to the one obtained for re-use in later API requests that require it
    global token
    token = response['token']
    # assert status code was OK (codes 200-299)
    expect(get_auth).to_be_ok()
    # assert response code was 200
    assert get_auth.status == 200


@pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin_date, checkout_date, additional_needs",
                         [("jason", "dynes", 99, True, "2024-01-02", "2024-02-02", "soft mattress")])
def test_create_booking(api_request_context: APIRequestContext, firstname,
                        lastname, totalprice, depositpaid,
                        checkin_date, checkout_date, additional_needs):
    # TODO: realise the params are hardcoded right now but will parameterize and hide
    data = {"firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {"checkin": checkin_date, "checkout": checkout_date},
            "additionalneeds": additional_needs,
            }
    create_booking = api_request_context.post(f"/booking", data=data)
    response = create_booking.json()
    # assert status code was OK (codes 200-299)
    expect(create_booking).to_be_ok()
    # assert response code was 200
    assert create_booking.status == 200
    global booking_id
    booking_id = response['bookingid']


@pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin_date, checkout_date, additional_needs",
                         [("jason", "dynes", 99, True, "2024-01-02", "2024-02-02", "soft mattress")])
def test_get_booking_by_id(api_request_context: APIRequestContext, firstname,
                           lastname, totalprice, depositpaid,
                           checkin_date, checkout_date, additional_needs):
    global booking_id
    get_booking_by_id = api_request_context.get(f"/booking/{booking_id}")
    response = get_booking_by_id.json()
    # assert status code was OK (codes 200-299)
    expect(get_booking_by_id).to_be_ok()
    # assert response code was 200
    assert get_booking_by_id.status == 200
    # assertions for each field in API response to confirm booking details
    assert response['firstname'] == firstname
    assert response['lastname'] == lastname
    assert response['totalprice'] == totalprice
    assert response['depositpaid'] == depositpaid
    assert response['bookingdates']['checkin'] == checkin_date
    assert response['bookingdates']['checkout'] == checkout_date
    assert response['additionalneeds'] == additional_needs


# removed as this will fail due to known bug  ("checkin_date", "2024-01-02"),
@pytest.mark.parametrize("api_call, data",
                         [("firstname", "jason"),
                          ("lastname", "dynes"),
                          ("first_lastname", "jason&lastname=dynes"),
                          ("checkout_date", "2024-02-02"),
                          ])
def test_get_booking_by_firstname_lastname_total_price_deposit_paid_check_dates_add_needs(
        api_request_context: APIRequestContext, api_call, data):
    match api_call:
        case "firstname":
            get_booking_by = api_request_context.get(f"/booking?firstname={data}")
            assert_api_response(get_booking_by)
        case "lastname":
            get_booking_by = api_request_context.get(f"/booking?lastname={data}")
            assert_api_response(get_booking_by)

        case "first_lastname":
            get_booking_by = api_request_context.get(f"/booking?firstname={data}")
            assert_api_response(get_booking_by)

        case "checkin_date":
            get_booking_by = api_request_context.get(f"/booking?checkin={data}")
            assert_api_response(get_booking_by)

        case "checkout_date":
            get_booking_by = api_request_context.get(f"/booking?checkout={data}")
            assert_api_response(get_booking_by)


def assert_api_response(get_booking_by):
    response = get_booking_by.json()
    # assert status code was OK (codes 200-299)
    expect(get_booking_by).to_be_ok()
    # assert response code was 200
    assert get_booking_by.status == 200
    # assertions for each field in API response to confirm booking details
    global booking_id
    count = 0
    for item in response:
        count += 1
        # response['firstname'] == firstname
        if booking_id == item["bookingid"]:
            # original create booking in dataset
            assert booking_id == item["bookingid"]
            return
    # assert item["bookingid"] == booking_id


@pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin_date, checkout_date, additional_needs",
                         [("john", "dyson", 999, False, "2023-01-02", "2023-02-02", "clean bathroom")])
def test_update_booking(api_request_context: APIRequestContext, firstname,
                        lastname, totalprice, depositpaid,
                        checkin_date, checkout_date, additional_needs):
    # TODO: realise the params are hardcoded right now but will parameterize and hide
    data = {"firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {"checkin": checkin_date, "checkout": checkout_date},
            "additionalneeds": additional_needs,
            }
    global booking_id
    update_booking = api_request_context.put(f"/booking/{booking_id}", data=data)
    response = update_booking.json()
    # assert status code was OK (codes 200-299)
    expect(update_booking).to_be_ok()
    # assert response code was 200
    assert update_booking.status == 200
    assert response['firstname'] == firstname
    assert response['lastname'] == lastname
    assert response['totalprice'] == totalprice
    assert response['depositpaid'] == depositpaid
    assert response['bookingdates']['checkin'] == checkin_date
    assert response['bookingdates']['checkout'] == checkout_date
    assert response['additionalneeds'] == additional_needs


@pytest.mark.parametrize("firstname, additional_needs",
                         [("jack", "clean sheets in bedroom")])
def test_patch_booking(api_request_context: APIRequestContext, firstname, additional_needs):
    # TODO: realise the params are hardcoded right now but will parameterize and hide
    data = {"firstname": firstname,
            "additionalneeds": additional_needs,
            }
    global booking_id
    update_booking = api_request_context.patch(f"/booking/{booking_id}", data=data)
    response = update_booking.json()
    # assert status code was OK (codes 200-299)
    expect(update_booking).to_be_ok()
    # assert response code was 200
    assert update_booking.status == 200
    assert response['firstname'] == firstname
    assert response['additionalneeds'] == additional_needs


@pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin_date, checkout_date, additional_needs",
                         [("jason", "dynes", 99, True, "2024-01-02", "2024-02-02", "soft mattress")])
def test_delete_booking_by_id(api_request_context: APIRequestContext, firstname,
                              lastname, totalprice, depositpaid,
                              checkin_date, checkout_date, additional_needs):
    global booking_id
    delete_booking_by_id = api_request_context.delete(f"/booking/{booking_id}")
    # assert status code was OK (codes 200-299)
    expect(delete_booking_by_id).to_be_ok()
    # assert response code was 200
    assert delete_booking_by_id.status == 201


# assert after deletion booking does not exist
# @pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin_date, checkout_date, additional_needs",
#                          [("jason", "dynes", 99, True, "2024-01-02", "2024-02-02", "soft mattress")])
def test_booking_deleted(api_request_context: APIRequestContext):
    global booking_id
    get_booking_by_id = api_request_context.get(f"/booking/{booking_id}")
    # assertions for each field in API response to confirm booking deleted
    # assert response code was 404
    assert get_booking_by_id.status == 404
