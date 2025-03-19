#data_quality_rule.feature
Feature: Data Quality Rule Management
  As a user
  I want to manage data quality rules
  So that I can ensure data integrity

  Scenario: Add new data quality rule
    Given the user is on the Data Quality Rule page
    When the user enters Rule ID "RD1234"
    And the user enters Rule Expression "Lookup"
    And the user enters Rule Description "Description of what the rule does"
    And the user clicks "Save"
    Then the rule should be added successfully

  Scenario: Reset data quality rule form
    Given the user is on the Data Quality Rule page
    When the user enters Rule ID "RD1234"
    And the user enters Rule Expression "Lookup"
    And the user enters Rule Description "Description of what the rule does"
    And the user clicks "Reset"
    Then the form should be reset

  Scenario: Verify existing rules in the table
    Given the user is on the Data Quality Rule page
    Then the rule table should display existing rules

