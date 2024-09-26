# see https://docs.robotframework.org/docs/different_libraries/how_to_find_library
# see https://docs.robotframework.org/docs/different_libraries/requests
# see https://docs.robotframework.org/docs/examples/restfulbooker

*** Settings ***
Library    RequestsLibrary
Library    Collections
Suite Setup    Authenticate as Admin

*** Test Cases ***

Health Check - Ping
    ${response}    GET    https://restful-booker.herokuapp.com/ping
    Log    ${response}
    Status Should Be    201
    Should Be Equal  ${response.text}   Created


Get Bookings from Restful Booker
    ${body}    Create Dictionary    firstname=John
    ${response}    GET    https://restful-booker.herokuapp.com/booking    ${body}
    Status Should Be    200
    Log List    ${response.json()}
    FOR  ${booking}  IN  @{response.json()}
        ${response}    GET    https://restful-booker.herokuapp.com/booking/${booking}[bookingid]
        TRY
            Log    ${response.json()}
        EXCEPT
            Log    Cannot retrieve JSON due to invalid data
        END
    END

Create a Booking at Restful Booker
    ${booking_dates}    Create Dictionary    checkin=2022-12-31    checkout=2023-01-01
    ${body}    Create Dictionary    firstname=Hans    lastname=Gruber    totalprice=200    depositpaid=false    bookingdates=${booking_dates}
    ${response}    POST    url=https://restful-booker.herokuapp.com/booking    json=${body}
    # capture create booking response and store as suite variables for use later
    Set Suite Variable    ${id}  ${response.json()}[bookingid]
    Set Suite Variable    ${firstname}  ${response.json()}[booking][firstname]
    Set Suite Variable    ${lastname}  ${response.json()}[booking][lastname]
    Set Suite Variable    ${totalprice}  ${response.json()}[booking][totalprice]
    Set Suite Variable    ${depositpaid}  ${response.json()}[booking][depositpaid]
    Set Suite Variable    ${checkin}  ${response.json()}[booking][bookingdates][checkin]
    Set Suite Variable    ${checkout}  ${response.json()}[booking][bookingdates][checkout]
    ${response}    GET    https://restful-booker.herokuapp.com/booking/${id}
    Log    ${response.json()}
    Should Be Equal    ${response.json()}[lastname]    Gruber
    Should Be Equal    ${response.json()}[firstname]    Hans
    Should Be Equal As Numbers    ${response.json()}[totalprice]    200
    Dictionary Should Contain Value     ${response.json()}    Gruber

Get Bookings by ID from Restful Booker
    # ${body}    Create Dictionary    firstname=John
    ${response}    GET    https://restful-booker.herokuapp.com/booking/${id}
    Status Should Be    200
    Log List    ${response.json()}


Get Bookings by First Name from Restful Booker
    # ${body}    Create Dictionary    firstname=John
    ${response}    GET    https://restful-booker.herokuapp.com/booking  params=firstname=${firstname}
    Status Should Be    200
    Log List    ${response.json()}

Get Bookings by Last Name from Restful Booker
    ${response}    GET    https://restful-booker.herokuapp.com/booking  params=lastname=${lastname}
    Status Should Be    200
    Log List    ${response.json()}

Delete Booking
    ${header}    Create Dictionary    Cookie=token\=${token}
    ${response}    DELETE    url=https://restful-booker.herokuapp.com/booking/${id}    headers=${header}
    Status Should Be    201    ${response}

*** Keywords ***
Authenticate as Admin
    ${body}    Create Dictionary    username=admin    password=password123
    ${response}    POST    url=https://restful-booker.herokuapp.com/auth    json=${body}
    Log    ${response.json()}
    Dictionary Should Contain Key     ${response.json()}  token
    ${token}    Set Variable    ${response.json()}[token]
    Log    ${token}
    Set Suite Variable    ${token}

