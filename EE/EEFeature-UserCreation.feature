# Created by Harwinder at 02/02/2018
Feature: Hotel booking Regression scripts

  Scenario Outline: Successfully booking in the hotel
    Given we are able to access the url
    When I am able to save the details <First_Name> <Surname> <Price> <deppaid>
    Then Application works fine

    Examples: Bookin In
      | First_Name | Surname | Price | deppaid |
      | Test1      | User    | 120   | Yes     |
      | Test2      | User    | 120   | Yes     |
      | Test3      | User    | 120   | Yes     |
      | Test4      | User    | 120   | Yes     |
      | Test5      | User    | 120   | Yes     |

