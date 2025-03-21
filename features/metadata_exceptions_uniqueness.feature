Feature: Metadata Uniqueness Explorer UI Testing

  Scenario: Verify Uniqueness Explorer Page Loads Successfully
    Given I am logged into the BNP Paribas system as an admin
    When I navigate to the "Exceptions - Uniqueness" section
    Then I should see the "Exceptions Update" form

  Scenario: Select Exception Category and Severity
    Given I am on the "Exceptions - Uniqueness" page
    When I select "Unique" as the Exception Category
    And I select "High" as the Severity
    Then the selected values should be displayed correctly

  Scenario: Add a Uniqueness Rule
    Given I am on the "Exceptions - Uniqueness" page
    When I select "Talyman" as the Input Source
    And I enter "3" as the Number of Attributes
    And I select "Transaction ID" as Attribute 1
    And I select "Agreement ID" as Attribute 2
    And I select "Client ID" as Attribute 3
    And I select "New" as the Status
    And I click the "Save" button
    Then the newly added uniqueness rule should be displayed in the Unique Explorer table

  Scenario: Reset Uniqueness Explorer Form
    Given I am on the "Exceptions - Uniqueness" page
    When I enter values in the Uniqueness Explorer form
    And I click the "Reset" button
    Then all fields in the Uniqueness Explorer form should be cleared
