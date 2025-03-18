Feature: Email Template Functionality

  Scenario: Verify email can be composed and sent
    Given the user is on the "Email Template" page
    When the user selects "Template 1" from the template dropdown
    And enters "testuser@example.com" in the email field
    And enters "Test Subject" in the subject field
    And enters "This is a test email." in the message body
    And clicks the "Send" button
    Then the email should be displayed in the sent list with "testuser@example.com" and "Test Subject"

  Scenario: Verify Cancel button clears the input fields
    Given the user is on the "Email Template" page
    When the user enters "testuser@example.com" in the email field
    And enters "Test Subject" in the subject field
    And enters "This is a test email." in the message body
    And clicks the "Cancel" button
    Then all input fields should be cleared

  Scenario: Verify email list displays sent emails
    Given the user has sent an email
    When the user checks the email list
    Then the email should be visible with correct details
