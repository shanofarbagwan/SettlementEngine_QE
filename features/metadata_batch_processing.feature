Feature: Metadata Batch Processing Functionality

  Scenario: Verify Metadata Batch Processing page loads successfully
    Given the user is logged in as "Admin"
    When the user navigates to the "Metadata Batch Processing" page
    Then the page title should be "Metadata Batch Processing"
    And the "Batch Processing Information" section should be visible
    And the "Submit" and "Reset" buttons should be displayed

  Scenario: Verify the batch processing table is displayed
    Given the user is on the "Metadata Batch Processing" page
    Then the batch processing table should be visible
    And it should display columns "Batch Name", "Frequency", "Source System", "File Date", "Created By"

  Scenario: Verify dropdown and input field for batch processing
    Given the user is on the "Metadata Batch Processing" page
    When the user clicks on the "Frequency" dropdown
    Then the dropdown should display options "Daily", "Monthly", "One-Off"
    When the user enters "Test System" in the "Source System" input field
    Then the "Source System" field should contain "Test System"

  Scenario: Submit batch processing information
    Given the user is on the "Metadata Batch Processing" page
    When the user selects "Daily" from the "Frequency" dropdown
    And the user enters "Test System" in the "Source System" input field
    And the user clicks the "Submit" button
    Then a success message should be displayed
    And the new batch entry should be added to the batch processing table

  Scenario: Reset batch processing form
    Given the user is on the "Metadata Batch Processing" page
    When the user enters "Test System" in the "Source System" input field
    And the user clicks the "Reset" button
    Then the "Frequency" dropdown should be reset
    And the "Source System" input field should be empty

  Scenario: Navigate through batch processing table pages
    Given the user is on the "Metadata Batch Processing" page
    When the user clicks the "Next Page" button
    Then the next set of batch entries should be displayed
    When the user clicks the "Previous Page" button
    Then the previous set of batch entries should be displayed
