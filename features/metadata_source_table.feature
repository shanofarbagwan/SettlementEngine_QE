Feature: Metadata Source Table Functionality

  Scenario: Verify Metadata Source Table page loads successfully
    Given the user is logged in as "Admin"
    When the user navigates to the "Metadata Source Table" page
    Then the page title should be "Metadata Source Table"
    And the "File Information" and "File Identification Settings" sections should be visible
    And the "Submit" and "Reset" buttons should be displayed

  Scenario: Verify the metadata source table is displayed
    Given the user is on the "Metadata Source Table" page
    Then the metadata source table should be visible
    And it should display columns "File Type", "File Name", "File Path Raw", "File Date", "Created By"

  Scenario: Verify file information input fields
    Given the user is on the "Metadata Source Table" page
    When the user enters "TestFile" in the "File Name" field
    And the user selects "CSV" from the "File Type" dropdown
    And the user enters "Pattern123" in the "File Pattern" field
    And the user enters "1000" in the "File Max Size (MB)" field
    Then the respective input fields should contain the entered values

  Scenario: Submit metadata source file information
    Given the user is on the "Metadata Source Table" page
    When the user fills in file information details
    And the user clicks the "Submit" button
    Then a success message should be displayed
    And the new file entry should be added to the metadata source table

  Scenario: Reset file information form
    Given the user is on the "Metadata Source Table" page
    When the user fills in file information details
    And the user clicks the "Reset" button
    Then all input fields should be cleared

  Scenario: Verify file identification settings input fields
    Given the user is on the "Metadata Source Table" page
    When the user enters "Header1" in the "Header Identifier" field
    And the user enters "Column1" in the "Column Identifier" field
    And the user enters "Body1" in the "Body Identifier" field
    Then the respective fields should contain the entered values

  Scenario: Submit metadata file identification settings
    Given the user is on the "Metadata Source Table" page
    When the user fills in file identification settings
    And the user clicks the "Submit" button
    Then a success message should be displayed

  Scenario: Navigate through metadata source table pages
    Given the user is on the "Metadata Source Table" page
    When the user clicks the "Next Page" button
    Then the next set of metadata source entries should be displayed
    When the user clicks the "Previous Page" button
    Then the previous set of metadata source entries should be displayed
