Feature: Data Quality Assignment Management

  Scenario: Verify Data Quality Assignment Page Loads Successfully
    Given I am logged into the BNP Paribas system as an admin
    When I navigate to the "Applied Data Quality" section
    Then I should see the "Data Quality Assignment" form

  Scenario: Assign a New Data Quality Rule
    Given I am on the "Data Quality Assignment" page
    When I select "Tallyman" as the Source Table
    And I select "Transaction Amount" as the Source Attribute
    And I select "Comparison" as the DQ Rule
    And I enter a Start Date
    And I enter an End Date
    And I click the "Save" button
    Then the new data quality assignment should be displayed in the table

  Scenario: Reset Data Quality Assignment Form
    Given I am on the "Data Quality Assignment" page
    When I enter values in the Data Quality Assignment form
    And I click the "Reset" button
    Then all fields in the Data Quality Assignment form should be cleared

  Scenario: Verify Applied Data Quality Table Displays Entries
    Given I am on the "Data Quality Assignment" page
    Then the Applied Data Quality table should display rule assignments

  Scenario: Edit an Existing Data Quality Assignment
    Given I am on the "Data Quality Assignment" page
    When I click the "Edit" button for a specific assignment
    And I modify the End Date
    And I click the "Save" button
    Then the updated assignment should be saved and displayed in the table

  Scenario: Delete a Data Quality Assignment
    Given I am on the "Data Quality Assignment" page
    When I click the "Delete" button for a specific assignment
    And I confirm the deletion
    Then the assignment should be removed from the table

  Scenario: Download Applied Data Quality
    Given I am on the "Data Quality Assignment" page
    When I click the "Download" button
    Then a file should be downloaded with the applied data quality assignments
