*** Settings ***
Documentation  Genderize REST API related keywords


*** Keywords ***
Get Genderize Gender
  [Documentation]  Request gender for a name
  [Arguments]  ${name}  ${expected_status_code}=200
  ${res}=  REST Get Genderize Gender  ${name}  ${expected_status_code}
  [Return]  ${res}
