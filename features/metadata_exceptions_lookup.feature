Feature: Metadata Lookup Explorer UI Testing

  Scenario: Verify Lookup Explorer Page Loads Successfully
    Given I am logged into the BNP Paribas system as an admin
    When I navigate to the "Exceptions - Look-up" section
    Then I should see the "Exceptions Update" form

  Scenario: Select Exception Category, Severity, and Owner
    Given I am on the "Exceptions - Look-up" page
    When I select "Lookup" as the Exception Category
    And I select "High" as the Severity
    And I select "John Doe" as the Exception Owner
    Then the selected values should be displayed correctly

  Scenario: Add a Lookup Entry
    Given I am on the "Exceptions - Look-up" page
    When I click the "Add Look-up" button
    And I select "Talyman" as the Input Source
    And I set "4" as the No of Attributes
    And I enter "Client Code" in Attribute 1
    And I enter "Shop Code" in Attribute 2
    And I set Attribute 3 and Attribute 4 as "X"
    And I click the "Save" button
    Then the newly added lookup entry should be displayed in the Lookup Explorer table

  Scenario: Delete a Lookup Entry
    Given I am on the "Exceptions - Look-up" page
    When I locate "Lookup2" in the Lookup Explorer table
    And I click the delete button for "Lookup2"
    And I confirm the deletion
    Then "Lookup2" should be removed from the Lookup Explorer table

  Scenario: Reset Lookup Explorer Form
    Given I am on the "Exceptions - Look-up" page
    When I enter values in the Lookup Explorer form
    And I click the "Reset" button
    Then all fields in the Lookup Explorer form should be cleared
