Feature: Cafe API
  As a customer,
  I want to search for a cafe in a specified location,
  So that I can find a cafe.

 Scenario Outline: Successfully search for a cafe for location
   Given the customer queries the API using the GET /search with query loc=<location>
   When the cafe location exists in the database
   Then the response status is <expected response code>
   # Then correct number of calculated results are returned
    Examples: Search_Results
        |location| expected response code |
        |London Bridge| 200|
        |london Bridge| 200|
        |London bridge| 200|
        |LONDON BRIDGE| 200|
        |Peckham      | 200|

   Scenario Outline: Unsuccessfully search for a cafe for location
   Given the customer queries the API using the GET /search with query loc=<location>
   When the cafe location does not exist in the database
   Then the response status is <expected response code>
   # Then correct number of calculated results are returned
    Examples: Search_Results
        |location|expected response code |
        |Bedford |404                    |
        |Banksy |404                     |
        |Londonbridge|404                |

    # Examples not needed as will make code run queries on database to get random cafes
    # and calculate expected number of cafes in response to then assert


# consider using https://pypi.org/project/pytest-csv-params/ and then have csv files driving tests




