# Playwright test automation guide By Jason Dynes

<!-- TOC -->
* [Playwright test automation guide By Jason Dynes](#playwright-test-automation-guide-by-jason-dynes)
  * [Useful references](#useful-references)
    * [Installation](#installation-)
    * [Writing Tests - Basic Actions, Assertions, Test Isolation and fixtures](#writing-tests---basic-actions-assertions-test-isolation-and-fixtures)
    * [Generating tests using CodeGen](#generating-tests-using-codegen)
    * [Running and Debugging tests](#running-and-debugging-tests)
      * [Run tests in headed mode](#run-tests-in-headed-mode)
      * [Run tests on different browsers](#run-tests-on-different-browsers)
      * [Run specific tests](#run-specific-tests)
      * [Run tests in parallel](#run-tests-in-parallel)
      * [Configure slow mo](#configure-slow-mo)
      * [Configure base-url](#configure-base-url)
    * [Actions](#actions)
      * [Text Input](#text-input)
        * [Text input](#text-input-1)
      * [Date input](#date-input)
      * [Time input](#time-input)
      * [Local datetime input](#local-datetime-input)
    * [Checkboxes and radio buttons](#checkboxes-and-radio-buttons)
      * [Check the checkbox](#check-the-checkbox)
      * [Assert the checked state](#assert-the-checked-state)
      * [Select the radio button](#select-the-radio-button)
    * [Select options](#select-options)
      * [Single selection matching the value or label](#single-selection-matching-the-value-or-label)
      * [Single selection matching the label](#single-selection-matching-the-label)
      * [Multiple selected items](#multiple-selected-items)
    * [Mouse Click](#mouse-click)
      * [Generic click](#generic-click)
      * [Double click](#double-click)
      * [Right click](#right-click)
      * [Shift + click](#shift--click)
      * [Hover over element](#hover-over-element)
      * [Click the top left corner](#click-the-top-left-corner)
      * [Forcing the click](#forcing-the-click)
    * [Focus element](#focus-element)
<!-- TOC -->


## Useful references
https://playwright.dev/python/

https://learn.microsoft.com/en-us/training/modules/build-with-playwright/

https://www.browserstack.com/guide/playwright-python-tutorial

### Installation 
Instructions can be found on https://playwright.dev/python/docs/intro


### Writing Tests - Basic Actions, Assertions, Test Isolation and fixtures
https://playwright.dev/python/docs/writing-tests


### Generating tests using CodeGen
https://playwright.dev/python/docs/codegen-intro

Actions like click or fill by simply interacting with the page
Assertions by clicking on one of the icons in the toolbar and then clicking on an element on the page to assert against. 
You can choose:
* 'assert visibility' to assert that an element is visible
* 'assert text' to assert that an element contains specific text
* 'assert value' to assert that an element has a specific value

You can generate locators with the test generator.

* Press the 'Record' button to stop the recording and the 'Pick Locator' button will appear.
* Click on the 'Pick Locator' button and then hover over elements in the browser window to see the locator highlighted underneath each element.
* To choose a locator click on the element you would like to locate and the code for that locator will appear in the locator playground next to the Pick Locator button.
* You can then edit the locator in the locator playground to fine tune it and see the matching element highlighted in the browser window.
* Use the copy button to copy the locator and paste it into your code.

### Running and Debugging tests

#### Run tests in headed mode
***pytest --headed***

#### Run tests on different browsers
To specify which browser you would like to run your tests on, use the --browser flag followed by the name of the browser.

***pytest --browser webkit***

To specify multiple browsers to run your tests on, use the --browser flag multiple times followed by the name of each browser.

***pytest --browser webkit --browser firefox***

#### Run specific tests
To run a single test file, pass in the name of the test file that you want to run.

***pytest test_login.py***

To run a set of test files, pass in the names of the test files that you want to run.

***pytest tests/test_todo_page.py tests/test_landing_page.py***

To run a specific test, pass in the function name of the test you want to run.

***pytest -k test_add_a_todo_item***

#### Run tests in parallel

To run your tests in parallel, use the --numprocesses flag followed by the number of processes you would like to run your tests on. We recommend half of logical CPU cores.

***pytest --numprocesses 2***

(This assumes pytest-xdist is installed. 
For more information see https://playwright.dev/python/docs/test-runners#parallelism-running-multiple-tests-at-once.)

#### Configure slow mo
Run tests with slow mo with the --slowmo argument.

***pytest --slowmo 100***

#### Configure base-url
Start Pytest with the base-url argument. The pytest-base-url plugin is used for that which allows you to set the base url from the config, CLI arg or as a fixture.
***pytest --base-url http://localhost:8080***

### Actions
Playwright can interact with HTML Input elements such as text inputs, checkboxes, radio buttons, select options, mouse clicks, type characters, keys and shortcuts as well as upload files and focus elements.

#### Text Input
Using locator.fill() is the easiest way to fill out the form fields. It focuses the element and triggers an input event with the entered text. It works for input, textarea and contenteditable elements.

##### Text input
page.get_by_role("textbox").fill("Peter")

#### Date input
page.get_by_label("Birth date").fill("2020-02-02")

#### Time input
page.get_by_label("Appointment time").fill("13:15")

#### Local datetime input
page.get_by_label("Local time").fill("2020-03-02T05:15")

### Checkboxes and radio buttons

Using locator.set_checked() is the easiest way to check and uncheck a checkbox or a radio button. This method can be used with input[type=checkbox], input[type=radio] and [role=checkbox] elements.

#### Check the checkbox
page.get_by_label('I agree to the terms above').check()

#### Assert the checked state
expect(page.get_by_label('Subscribe to newsletter')).to_be_checked()

#### Select the radio button
page.get_by_label('XL').check()

### Select options
Selects one or multiple options in the <'select'> element with locator.select_option(). You can specify option value, or label to select. Multiple options can be selected.

#### Single selection matching the value or label
page.get_by_label('Choose a color').select_option('blue')

#### Single selection matching the label
page.get_by_label('Choose a color').select_option(label='Blue')

#### Multiple selected items
page.get_by_label('Choose multiple colors').select_option(['red', 'green', 'blue'])

### Mouse Click
Performs a simple human click.

#### Generic click
page.get_by_role("button").click()

#### Double click
page.get_by_text("Item").dblclick()

#### Right click
page.get_by_text("Item").click(button="right")

#### Shift + click
page.get_by_text("Item").click(modifiers=["Shift"])

#### Hover over element
page.get_by_text("Item").hover()

#### Click the top left corner
page.get_by_text("Item").click(position={ "x": 0, "y": 0})

#### Forcing the click
page.get_by_role("button").click(force=True)

### Focus element
For the dynamic pages that handle focus events, you can focus the given element with locator.focus().
page.get_by_label('password').focus()



