Feature: Login and Verification for PF UK Settlement Engine

  Scenario: Successful Smart Card Login
    Given the user is on the PF UK Settlement Engine login page
    When the user enters a valid smart card number
    And clicks the continue button
    Then the user should be logged in successfully

  Scenario: Unsuccessful Smart Card Login
    Given the user is on the PF UK Settlement Engine login page
    When the user enters an invalid smart card number
    And clicks the continue button
    Then an error message should be displayed

Feature: Exceptions Page Verification

  Scenario: Verify Exceptions Page Elements
    Given the user is logged into the PF UK Settlement Engine
    When the user navigates to the Exceptions page
    Then the Exceptions header should be displayed
    And the Exceptions table should contain data
    And the Response button should be visible

Feature: Data Quality Assignment Verification

  Scenario: Verify Data Quality Assignment Elements
    Given the user is logged into the PF UK Settlement Engine
    When the user navigates to the Data Quality Assignment page
    Then the Data Quality Assignment header should be displayed
    And the Data Quality form should be visible
    And the Applied Data Quality table should contain data

  Scenario: Add a new Data Quality Assignment
    Given the user is logged into the PF UK Settlement Engine
    When the user navigates to the Data Quality Assignment page
    And the user fills in the Data Quality Assignment form
    And clicks the Save button
    Then the new Data Quality Assignment should be added successfully

  Scenario: Try adding an incomplete Data Quality Assignment
    Given the user is logged into the PF UK Settlement Engine
    When the user navigates to the Data Quality Assignment page
    And the user leaves required fields empty
    And clicks the Save button
    Then an error message should be displayed

  Scenario: Verify Download Button
    Given the user is logged into the PF UK Settlement Engine
    When the user navigates to the Data Quality Assignment page
    Then the Download button should be visible