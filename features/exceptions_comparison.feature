# exceptions_comparison.feature
Feature: Exceptions - Comparison Page Validation

  Scenario: Validate exception creation with comparison rule
    Given the user is on the Exceptions - Comparison page
    When the user selects rule type as "Comparison"
    And the user selects severity as "High"
    And the user enters Source1 as "Tallyman"
    And the user enters Source1 attribute as "Transaction Amt"
    And the user selects comparison operator as ">"
    And the user enters Source2 as "Tallyman"
    And the user enters Source2 attribute as "Agreement Amt"
    And the user selects status as "New"
    And the user clicks on "Save" button
    Then the exception should be saved successfully

  Scenario: Validate reset button functionality
    Given the user is on the Exceptions - Comparison page
    When the user enters Source1 as "Tallyman"
    And the user clicks on "Reset" button
    Then all fields should be cleared

  Scenario: Validate error message on incomplete submission
    Given the user is on the Exceptions - Comparison page
    When the user clicks on "Save" button
    Then an error message should be displayed
