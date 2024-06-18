*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${url}      http://thetestingworldapi.com/

*** Test Cases ***
TC_RequestChaining
        Create Session    fetchData     ${url}
        &{body}=        create dictionary       first_name=Juhi     middle_name=rajput      last_name=chauhan       date_of_birth=04/06/1999
        &{header}=          create dictionary       Content-Type=application/json      Accept=application/json
        ${response}=    post request        fetchData       api/studentsDetails     data=${body}    headers=${header}
        log to console    ${response.status_code}
        log to console    ${response.content}
        ${json_response}=   To Json    ${response.content}
        ${value_id}=    Get Value From Json    ${json_response}     id
        ${id}=      get from list    ${value_id}    0
        log to console    ${id}
        ${actual_id}=       convert to string    ${id}
        should be equal    ${actual_id}     1207396
