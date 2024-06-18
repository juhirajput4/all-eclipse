*** Settings ***
Library  OperatingSystem
Library  RequestsLibrary
Library     JSONLibrary
Library     Collections

*** Variables ***
${url}  http://thetestingworldapi.com/

*** Test Cases ***
TC_1
    Create Session      postJson    ${url}
    ${jsonFile}=     get file  C:/Users/Cloud Analogy/Desktop/request.json
    &{header}=      Create Dictionary   Content-Type=application/json   #Accept=application/json
    ${jsonData}=    Convert String To Json  ${jsonFile}
    ${response}=    Post Request    postJson    api/studentsDetails     data=${jsonData}       headers=${header}
    log to console  ${response.status_code}
    log to console  ${response.content}
    log to console  ${jsonData}

