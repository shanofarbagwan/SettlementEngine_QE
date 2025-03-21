Feature: Metadata Exceptions Table UI Testing

  Scenario: Verify Exceptions Table Page Loads Successfully
    Given I am logged into the BNP Paribas system as an admin
    When I navigate to the "Exceptions" section
    Then I should see the "Exceptions Update" form

  Scenario: Filter Exceptions by Rule Type and Severity
    Given I am on the "Exceptions" page
    When I select "RT100842" as the Rule Type
    And I select "High" as the Severity
    Then I should see exceptions filtered by Rule Type "RT100842" and Severity "High"

  Scenario: Edit an Exception Rule
    Given I am on the "Exceptions" page
    When I locate "ED58462" in the exceptions list
    And I click the edit button for "ED58462"
    And I update the Source Attribute to "Transaction Amount"
    And I click the "Submit" button
    Then I should see "ED58462" with Source Attribute "Transaction Amount"

  Scenario: Delete an Exception Rule
    Given I am on the "Exceptions" page
    When I locate "ED10273" in the exceptions list
    And I click the delete button for "ED10273"
    And I confirm the deletion
    Then "ED10273" should be removed from the exceptions list

  Scenario: Download the Exceptions List
    Given I am on the "Exceptions" page
    When I click the "Download" button
    Then the exceptions list should be downloaded as a file
