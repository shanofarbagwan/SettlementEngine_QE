Feature: Metadata Rule Mapping

  Scenario: Verify that the Metadata Rule Mapping page loads successfully
    Given I am logged into the BNP Paribas system as an admin
    When I navigate to the "Rule Mapping" section
    Then I should see the "Metadata Update for Rule Mapping" form

  Scenario: Add a new Metadata Rule
    Given I am on the "Metadata Rule Mapping" page
    When I enter "NEW_RULE" in the Attribute Name field
    And I select "RID999" as the Record Identifier
    And I enter "1" as the Attribute Order
    And I enter "5" as the Attribute Start Position
    And I select "TXT" as the Attribute Data Type
    And I click the "Save" button
    Then I should see "NEW_RULE" added to the metadata rule list

  Scenario: Edit an existing Metadata Rule
    Given I am on the "Metadata Rule Mapping" page
    When I click the edit button for "SEQ_NO"
    And I update the Attribute Order to "4"
    And I click the "Save" button
    Then I should see "SEQ_NO" with Attribute Order "4"

  Scenario: Delete an existing Metadata Rule
    Given I am on the "Metadata Rule Mapping" page
    When I click the delete button for "AGREI-NO"
    And I confirm the deletion
    Then "AGREI-NO" should no longer be in the metadata rule list

  Scenario: Upload a Metadata Rule File
    Given I am on the "Metadata Rule Mapping" page
    When I click the "Upload" button
    And I select a valid metadata rule file
    And I confirm the upload
    Then I should see a success message
