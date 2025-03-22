Feature: Metadata Source File Management

  Scenario: Verify adding a new data source file with valid details
    Given I navigate to the "Meta Data" page
    When I click on "Add New"
    And I enter "test_file_001" in the "File Name" field
    And I enter "CSV" in the "File Type" field
    And I enter "/source/test_file_001" in the "File path raw" field
    And I enter "/destination/test_file_001" in the "File Path Cleansed" field
    And I enter "test_file_001" in the "File Pattern" field
    And I enter "10" in the "File Max Size(MB)" field
    And I enter "," in the "File Delimeter" field
    And I enter "header_1" in the "Header Identifier" field
    And I click on "Submit"
    Then I should see the file "test_file_001" added in the table

  Scenario: Verify the reset functionality
    Given I navigate to the "Meta Data" page
    When I click on "Add New"
    And I enter "dummy_file" in the "File Name" field
    And I click on "Reset"
    Then all input fields should be cleared

  Scenario: Verify cancel button functionality
    Given I navigate to the "Meta Data" page
    When I click on "Add New"
    And I enter "cancel_file" in the "File Name" field
    And I click on "Cancel"
    Then I should return to the "Meta Data" page without changes

  Scenario: Verify deletion of an existing file entry
    Given I navigate to the "Meta Data" page
    When I click on the delete icon for file "test_1223"
    And I confirm the deletion
    Then I should not see "test_1223" in the file table
