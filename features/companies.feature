Feature: Add new company
  Background:
    Given user on login page
    When user input it.qa@edot.id and it.QA2025

  Scenario:User add new companies
    When user choose companies button
    Then user complete form companies

