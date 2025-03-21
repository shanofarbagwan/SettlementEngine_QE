Feature: Metadata Table Columns UI Testing

  Scenario: Verify Metadata Table Columns Page Loads Successfully
    Given I am logged into the BNP Paribas system as an admin
    When I navigate to the "Metadata Column" section
    Then I should see the "Metadata Update for Columns" form

  Scenario: Add a New Metadata Column
    Given I am on the "Metadata Table Columns" page
    When I select a file "sample_file.csv"
    And I enter "NEW_COLUMN" in the Column Name field
    And I select "TEXT" as the Column Data Type
    And I enter "N/A" as the Column Null
    And I enter "Pattern" as the Column Match
    And I enter "3 MB" as the Max Size
    And I enter "mm/dd/yyyy" as the Column Date Format
    And I click the "Submit" button
    Then I should see "NEW_COLUMN" in the metadata table column list

  Scenario: Edit an Existing Metadata Column
    Given I am on the "Metadata Table Columns" page
    When I locate "REC_TYPE" in the metadata table column list
    And I click the edit button for "REC_TYPE"
    And I update the Max Size to "4 MB"
    And I click the "Submit" button
    Then I should see "REC_TYPE" with Max Size "4 MB"

  Scenario: Delete a Metadata Column
    Given I am on the "Metadata Table Columns" page
    When I locate "AGREI-NO" in the metadata table column list
    And I click the delete button for "AGREI-NO"
    And I confirm the deletion
    Then "AGREI-NO" should be removed from the metadata table column list
