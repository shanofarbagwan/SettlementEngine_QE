Feature: Login Window Functionality

  Scenario: Successful login with smart card
    Given the user is on the "Login Window" screen
    When the user enters a valid smart card PIN
    And the user clicks the "Continue" button
    Then the user should be redirected to the dashboard

  Scenario: Login fails with invalid smart card PIN
    Given the user is on the "Login Window" screen
    When the user enters an invalid smart card PIN
    And the user clicks the "Continue" button
    Then an error message should be displayed

  Scenario: Visibility toggle for smart card PIN
    Given the user is on the "Login Window" screen
    When the user clicks the visibility toggle button
    Then the smart card PIN should be visible

  Scenario: UI elements are displayed correctly
    Given the user is on the "Login Window" screen
    Then the "BNP PARIBAS" logo should be visible
    And the "PF UK Settlement Engine" title should be displayed
    And the smart card input field should be present
    And the "Continue" button should be enabled
