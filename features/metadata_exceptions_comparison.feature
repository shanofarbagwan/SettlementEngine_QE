Feature: Metadata Comparison Explorer UI Testing

  Scenario: Verify Comparison Explorer Page Loads Successfully
    Given I am logged into the BNP Paribas system as an admin
    When I navigate to the "Exceptions - Comparison" section
    Then I should see the "Exceptions Update" form

  Scenario: Select Exception Category and Severity
    Given I am on the "Exceptions - Comparison" page
    When I select "Comparison" as the Exception Category
    And I select "High" as the Severity
    Then the selected values should be displayed correctly

  Scenario: Add a Comparison Rule
    Given I am on the "Exceptions - Comparison" page
    When I select "Talyman" as the Input Source
    And I select "Transaction Amount" as the Attribute
    And I select ">=" as the Comparison Operator
    And I select "Talyman" as the Source2
    And I select "Agreement Amount" as the Source2 Attribute
    And I select "New" as the Status
    And I click the "Save" button
    Then the newly added comparison rule should be displayed in the Comparison Explorer table

  Scenario: Reset Comparison Explorer Form
    Given I am on the "Exceptions - Comparison" page
    When I enter values in the Comparison Explorer form
    And I click the "Reset" button
    Then all fields in the Comparison Explorer form should be cleared
