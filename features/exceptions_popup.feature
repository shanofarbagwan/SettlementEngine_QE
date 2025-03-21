Feature: Exceptions - Popup Validation

  Scenario: Verify Popup Opens Successfully
    Given I am on the "Exceptions" page
    When I click on an exception entry
    Then the "Exceptions Information" popup should be displayed

  Scenario: Verify Data Displayed in Popup
    Given the "Exceptions Information" popup is open
    Then the popup should display impacted attributes, rule type, account number, and client code

  Scenario: Close the Popup
    Given the "Exceptions Information" popup is open
    When I click the "Cancel" button
    Then the popup should be closed

  Scenario: Ensure Data is Scrollable in Popup
    Given the "Exceptions Information" popup is open
    When I scroll down within the popup
    Then I should be able to view additional exception details
