Feature:eSuite Web Apps
  Background:
     Given user on login page

  Scenario Outline:User login to website
    When user input <username> and <password>
    Then user <status> logged in
    Examples:
      | username | password | status |
      | it.qa@edot.id | it.QA2025 |successfully|
      | it.qa@edot.id | 12345678  |failed|

  Scenario: User login with unregistered user
    When user click textbox_username
    And user input unregistered random
    Then user gets popup message to register

  Scenario: User login with invalid format email
    When user input invalid format email
    Then user get error message
