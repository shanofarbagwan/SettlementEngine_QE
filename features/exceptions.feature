Feature: Exceptions Management

  Scenario: Verify Exceptions Page Loads Successfully
    Given I am logged into the BNP Paribas system as an admin
    When I navigate to the "Exceptions" section
    Then I should see the "Exceptions information" table

  Scenario: Verify Data in Exceptions Table
    Given I am on the "Exceptions" page
    Then the table should display exception details including Account No, Client Code, Shop Code, and Rule Type

  Scenario: Filter Exceptions Data
    Given I am on the "Exceptions" page
    When I enter "Lookup" in the Rule Type filter
    And I apply the filter
    Then only exceptions with the Rule Type "Lookup" should be displayed

  Scenario: Search for a Specific Exception
    Given I am on the "Exceptions" page
    When I enter an Account No in the search box
    And I click the "Search" button
    Then the table should display only the matching exception

  Scenario: Reprocess an Exception
    Given I am on the "Exceptions" page
    When I select an exception from the table
    And I click the "Reprocess" button
    Then the selected exception should be reprocessed successfully
