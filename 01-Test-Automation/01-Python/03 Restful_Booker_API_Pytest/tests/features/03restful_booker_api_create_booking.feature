Feature: Restful Booker API - Create Booking
  As a user,
  I want to be able to create booking details via a REST API,
  So that I can create a new booking

  Scenario: Restful Booker API Create Booking
    Given the Restful Booker API is online
    When a "create_booking" POST request is sent
    Then the response status code is "200"
    And a booking id is returned
    And the response time is less than "1000"ms