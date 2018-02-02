# Created by HArwinder at 02/02/2018
Feature: Hotel booking Regression scripts

  Scenario Outline: Successfully delete the booking
    Given we are able to access the url
    Then I am able to delete the details <First_Name> <Surname> <Price>

    Examples: Bookin Out
      | First_Name | Surname | Price |
      | Test5      | User    | 120   |
