*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Navigate to invoice app
    Open Browser    url=http://inv.beaufortfairmont.com/#/  browser=firefox

Click 'invoices' on navigation bar
    Click Link  Invoices

Click 'add invoices' on navigation bar
    Click Link  Add Invoice

Enter valid invoice details
    Wait Until Element Is Visible    css:#invoiceNo_add > input:nth-child(2)
    Input Text    css:#invoiceNo_add > input:nth-child(2)  text1
    Input Text    css:#compName_add > input:nth-child(2)  text 2
    Input Text    css:#typeofwork_add > input:nth-child(2)  text 3
    Input Text    css:#cost_add > input:nth-child(2)  text 4
    Select From List By Label    css:#selectStatus   Paid
    Input Text  css:#invoice_dueDate > input:nth-child(2)  2024-01-01
    Input Text  css:#comments_add > input:nth-child(2)   text5

Enter invalid invoice details
    Wait Until Element Is Visible    css:#invoiceNo_add > input:nth-child(2)
    Input Text    css:#invoiceNo_add > input:nth-child(2)  text1
    # Input Text    css:#compName_add > input:nth-child(2)  text 2
    Input Text    css:#typeofwork_add > input:nth-child(2)  text 3
    # Input Text    css:#cost_add > input:nth-child(2)  text 4
    Select From List By Label    css:#selectStatus   Paid
    Input Text  css:#invoice_dueDate > input:nth-child(2)  adadad
    Input Text  css:#comments_add > input:nth-child(2)   text5

Submit Invoice
    Click Button    css:#createButton

Cancel invoice
    Click Button    css:#content-wrapper > div > div.ng-scope > div > div > form > a:nth-child(9) > button

End test
    Close Browser