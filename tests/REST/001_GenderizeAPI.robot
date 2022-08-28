*** Settings ***
Documentation  Test cases for Genderize REST API

Resource  ../../resources/REST/rest-genderize-keywords.robot
Library  ../../resources/REST/library/RestAPI.py
Test Timeout  5 minutes

*** Test Cases ***
GenderizeAPI 01 - Single Name
  [Documentation]  Verifies that proper response is received with single name parameter
  [Tags]  GenderizeAPI  REST  SchibstedDemo
  ${res}=  Get Genderize Gender  Peter
  Should Be Equal As Strings  ${res['gender']}  male  error=Wrong gender returned

GenderizeAPI 02 - Unprocessable Entity, Name Missing
  [Documentation]  Verifies that proper error response is received if name parameter is missing
  [Tags]  GenderizeAPI  REST  SchibstedDemo
  ${res}=  Get Genderize Gender  ${EMPTY}  expected_status_code=422

# More tests be here
