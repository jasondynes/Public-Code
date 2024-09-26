*** Settings ***


*** Test Cases ***
Test case 1
    [Documentation]     This is some basic info about the test
    [Tags]  Smoke
    Do Something
    Do Something Else

Test case 2
    Do Another Thing
    Do Something Else

*** Keywords ***
Do Something
    Log    I am doing something......


Do Something Else
    Log    I am doing something else.....



Do Another Thing
    Log    I am doing another thing.....


