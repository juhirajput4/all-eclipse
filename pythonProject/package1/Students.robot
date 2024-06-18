*** Settings ***
# Setting section is used to define the libraary which we will using for our current project
Library     RequestsLibrary
Library     JSONLibrary
Library     Collections
Documentation   This robot file consists of API Automation test cases
*** Variables ***
${url}  http://thetestingworldapi.com/
*** Test Cases ***
TC_Request
    Create Session  FetchTechnicalSkills    ${url}
    ${response}=    GET On Session  FetchTechnicalSkills    api/Students
    log to console  ${response.status_code}
    log to console  ${response.content}
#    ${status_code}=    convert to string  ${response.status_code}
#    should be equal  ${status_code}    200
#    ${json_response}=    To Json  ${response.content}
#    ${language_list}=    Get Value From Json     ${json_response}    $.data[0].language[0]
#    ${language}=    GET FROM LIST  ${language_list}     0
#    should be equal  ${language}    Java
#    log to console  ${language}
