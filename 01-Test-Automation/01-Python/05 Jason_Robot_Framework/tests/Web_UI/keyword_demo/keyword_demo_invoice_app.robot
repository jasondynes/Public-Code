# see https://docs.robotframework.org/docs/different_libraries/selenium
# see https://docs.robotframework.org/docs/different_libraries/how_to_find_library

*** Settings ***
# Library    SeleniumLibrary
resource    ${CURDIR}/../../../resources/common.robot
Library    Process

# setup and teardown options at a test level or test suite level
#Test Setup
#Test Teardown
#Suite Setup
#Suite Teardown

*** Variables ***
# insert any global variables here or inline in a given test case

*** Test Cases ***
Test case 1
    [Documentation]     See all invoices
    [Tags]  Smoke
    Navigate to invoice app
    Click 'invoices' on navigation bar
    # Check there are 0 invoices

Test case 2
    [Documentation]     Add valid invoice
    [Tags]  Smoke
    Click 'add invoices' on navigation bar
    Enter valid invoice details
    Submit invoice
    # Check invoice has been created

Test case 3
    [Documentation]     Add invalid invoice
    [Tags]  Smoke
    Click 'add invoices' on navigation bar
    Enter invalid invoice details
    Submit invoice
    Alert Should Be Present
    # Check invoice has not been created

Test case 4
    [Documentation]     Cancel invoice
    [Tags]  Smoke
    Click 'add invoices' on navigation bar
    Enter valid invoice details
    Cancel invoice
    # Check invoice has not been created

Test case 5
    [Documentation]     Teardown
    [Tags]  Smoke
    End test
