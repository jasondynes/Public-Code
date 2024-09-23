Feature: Restful Booker API - Get Bookings
  As a user,
  I want to be able to get booking details via a REST API,
  So that I can use bookings details to execute POST, PUT and DELETE operations.

  Scenario: Restful Booker API Get All Bookings
    Given the Restful Booker API is online
    When a "bookings" GET booking request filtered by "all" is sent
    Then the response status code is "200"
    And the response contains all bookings
    And the response time is less than "1000"ms

  Scenario: Restful Booker API Get Booking By ID
    Given the Restful Booker API is online
    When a "bookings" GET booking request filtered by "id" is sent
    Then the response status code is "200"
    And the response contains bookings filtered by "id"
    And the response time is less than "1000"ms

  Scenario: Restful Booker API Get Booking By firstname
    Given the Restful Booker API is online
    When a "bookings" GET booking request filtered by "firstname" is sent
    Then the response status code is "200"
    And the response contains bookings filtered by "firstname"
    And the response time is less than "1000"ms

  Scenario: Restful Booker API Get Booking By lastname
    Given the Restful Booker API is online
    When a "bookings" GET booking request filtered by "lastname" is sent
    Then the response status code is "200"
    And the response contains bookings filtered by "lastname"
    And the response time is less than "1000"ms

  Scenario: Restful Booker API Get Booking By firstname&lastname
    Given the Restful Booker API is online
    When a "bookings" GET booking request filtered by "firstname&lastname" is sent
    Then the response status code is "200"
    And the response contains bookings filtered by "firstname&lastname"
    And the response time is less than "1000"ms

  Scenario: Restful Booker API Get Booking By checkinDate
    Given the Restful Booker API is online
    When a "bookings" GET booking request filtered by "checkinDate" is sent
    Then the response status code is "200"
    And the response contains bookings filtered by "checkin"
    And the response time is less than "1000"ms

  Scenario: Restful Booker API Get Booking By checkoutDate
    Given the Restful Booker API is online
    When a "bookings" GET booking request filtered by "checkoutDate" is sent
    Then the response status code is "200"
    And the response contains bookings filtered by "checkout"
    And the response time is less than "1000"ms