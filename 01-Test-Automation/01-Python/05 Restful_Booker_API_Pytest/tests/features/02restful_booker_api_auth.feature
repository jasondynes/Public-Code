Feature: Restful Booker API - Create Token
  As a user,
  I want to be able to get a Token via a REST API,
  So that I can execute PUTS and DELETE operations.

  Scenario Outline: Restful Booker API Create Token - Valid User Name and Password
    Given the Restful Booker API is online
    When a "auth" POST request is sent with Valid "<user_name>" and "<password>"
    Then the response status code is "200"
    And the response contains "token"
    And the response time is less than "1000"ms

    Examples:
      | user_name |password |
      | admin |password123 |

  Scenario Outline: Restful Booker API Create Token - Invalid User Name and Password
    Given the Restful Booker API is online
    When a "auth" POST request is sent with Invalid "<user_name>" and "<password>"
    Then the response status code is "200"
    And the response contains "{"reason":"Bad credentials"}"
    And the response time is less than "1000"ms

    Examples:
      | user_name |password |
      | jasond |password123 |
      | tester |test123 |
      | admin |pwd123 |