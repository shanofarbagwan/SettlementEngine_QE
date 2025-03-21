Feature: Data Quality Rule Management

  Scenario: Verify Data Quality Rule Page Loads Successfully
    Given I am logged into the BNP Paribas system as an admin
    When I navigate to the "Data Quality Rule" section
    Then I should see the "Data Quality Rule" form

  Scenario: Add a New Data Quality Rule
    Given I am on the "Data Quality Rule" page
    When I select "Rule Expression" as the Rule Type
    And I select "High" as the Severity
    And I enter "Sample Rule Description" in the Rule Description field
    And I click the "Save" button
    Then the new data quality rule should be displayed in the table

  Scenario: Reset Data Quality Rule Form
    Given I am on the "Data Quality Rule" page
    When I enter values in the Data Quality Rule form
    And I click the "Reset" button
    Then all fields in the Data Quality Rule form should be cleared

  Scenario: Verify Data Quality Rule Table Displays Entries
    Given I am on the "Data Quality Rule" page
    Then the Data Quality Rule table should display rule entries

  Scenario: Edit an Existing Data Quality Rule
    Given I am on the "Data Quality Rule" page
    When I click the "Edit" button for a specific rule
    And I modify the Rule Description to "Updated Description"
    And I click the "Save" button
    Then the updated rule should be saved and displayed in the table

  Scenario: Delete a Data Quality Rule
    Given I am on the "Data Quality Rule" page
    When I click the "Delete" button for a specific rule
    And I confirm the deletion
    Then the rule should be removed from the table
