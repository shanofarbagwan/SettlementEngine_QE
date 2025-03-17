Feature: Login functionality on SauceDemo

  Scenario: Login with valid credentials
    Given I open the SauceDemo login page
    When I enter valid username and password
    And I click the login button
    Then I should be redirected to the inventory page

  Scenario: Login with invalid credentials
    Given I open the SauceDemo login page
    When I enter invalid username and password
    And I click the login button
    Then I should see an error message
