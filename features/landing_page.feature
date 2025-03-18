Feature: Landing Page Functionality

  Scenario: Verify landing page loads successfully
    Given the user is logged in as "Admin"
    When the user navigates to the "Landing Page"
    Then the "PF UK Settlement Engine" heading should be displayed
    And the BNP PARIBAS logo should be visible
    And the user's profile should be displayed

  Scenario: Verify the sections are displayed correctly
    Given the user is on the "Landing Page"
    Then the "Payment" section should be visible
    And the "Exceptions" section should be visible
    And the "Reference Look Up" section should be visible
    And the "Metadata" section should be visible

  Scenario: Navigate to the Payment section
    Given the user is on the "Landing Page"
    When the user clicks the "Payment" section
    Then the user should be navigated to the "Payment" page

  Scenario: Navigate to the Exceptions section
    Given the user is on the "Landing Page"
    When the user clicks the "Exceptions" section
    Then the user should be navigated to the "Exceptions" page

  Scenario: Navigate to the Reference Look Up section
    Given the user is on the "Landing Page"
    When the user clicks the "Reference Look Up" section
    Then the user should be navigated to the "Reference Look Up" page

  Scenario: Navigate to the Metadata section
    Given the user is on the "Landing Page"
    When the user clicks the "Metadata" section
    Then the user should be navigated to the "Metadata" page
