Feature: Restful Booker API - Health Check
  As a user,
  I want to get a health check result via a REST API,
  So that I know the API is working.

  Scenario: Restful Booker API Health Check - Valid
    Given the Restful Booker API is online
    When a ping GET request is sent
    Then the response status code is "201"
    And the response contains "Created"
    And the response time is less than "1000"ms

