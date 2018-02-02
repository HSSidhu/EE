Feature: Hotel booking Regression scripts

  Scenario Outline: Successfully booking in the hotel
    Given we are able to access the url <url>
    When I am able to save the details <First_Name> <Surname> <Price> <deppaid><url>
    Then Application works fine

    Examples: Bookin In
      |url|First_Name|Surname|Price|deppaid|
      |http://hotel-test.equalexperts.io/|Test1|User|120|Yes|


#  Scenario Outline: Successfully delete the booking
#    Given we are able to access the url <url>
#    Then I am able to delete the details <First_Name> <Surname> <Price>
#
#    Examples: Bookin Out
#      |url|First_Name|Surname|Price|
#      |http://hotel-test.equalexperts.io/|Test1|User|120|
##      |http://hotel-test.equalexperts.io/|Test2|User|120|
##      |http://hotel-test.equalexperts.io/|Test3|User|120|
##      |http://hotel-test.equalexperts.io/|Test4|User|120|
##      |http://hotel-test.equalexperts.io/|Test5|User|120|
