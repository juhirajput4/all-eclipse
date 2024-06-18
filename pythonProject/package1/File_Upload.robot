*** Settings ***
# Setting section is used to define the libraary which we will using for our current project
Library     RequestsLibrary
Library     JSONLibrary
Library     Collections
*** Variables ***
${url}  http://thetestingworldapi.com/
*** Test Cases ***
TC_Request
    Create Session  FetchTechnicalSkills    ${url}
    ${response}=    GET On Session  FetchTechnicalSkills    api/FileUpload
    log to console  ${response.status_code}
    log to console  ${response.content}
    ${status_code}=    convert to string  ${response.status_code}
    should be equal  ${status_code}    500

