Feature: Popup UI Functionality

  Scenario: Verify user can add information
    Given the user is on the "Add User Information" popup
    When the user selects "James George" from the "User Name" dropdown
    And the user enters "james.george@bnpparibas-pf.co.uk" in the "Email" field
    And the user clicks the "Save" button
    Then the user information should be saved successfully

  Scenario: Verify user can cancel adding information
    Given the user is on the "Add User Information" popup
    When the user clicks the "Cancel" button
    Then the popup should close without saving

  Scenario: Confirm update popup appears
    Given the user performs an update action
    Then a confirmation popup should appear with the text "Are you sure you want to update this activity?"
    And the popup should contain "Confirm" and "Cancel" buttons

  Scenario: Confirm deletion popup appears
    Given the user deletes an activity
    Then a confirmation popup should appear with the text "Activity deleted successfully!"
    And the popup should contain "Confirm" and "Cancel" buttons

  Scenario: Verify closing the popup
    Given a popup is displayed
    When the user clicks the close (X) button
    Then the popup should close
