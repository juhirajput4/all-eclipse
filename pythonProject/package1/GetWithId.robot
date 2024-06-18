*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Documentation   This robot file consists of API Automation test cases
*** Variables ***
${url}  http://thetestingworldapi.com/
${id}   1147032
${child_url}   api/studentsDetails
${reqres_url}   https://reqres.in/
*** Test Cases ***
TC_GETRequest
    [Documentation]  This test case will automate the Get Request containing Parameters
    Create Session  FetchOneId  ${url}
    ${response}=    GET On Session  FetchOneId  ${child_url}/${id}
    log to console  ${response.status_code}
    log to console  ${response.content}
    ${actual_code}=    convert to string  ${response.status_code}
    should be equal    ${actual_code}   200
    ${json_response}=  To Json  ${response.content}
    ${id_list}=     Get Value From Json     ${json_response}     data.id
    ${id}=  get from list  ${id_list}   0
    log to console  ${id}
    ${int_id}=  convert to string  ${id}
    should be equal  ${int_id}  1147032

TC_Get_Request_with_Parameters
    [Documentation]  This test case will automate the Get Request containing Parameters
    Create Session      FetchwitchParameters    ${reqres_url}
    # Parameters are in form of key and value pair so we will be using dictonary
    &{parameters}=    Create Dictionary   page=2
    ${response}=    GET On Session      FetchwitchParameters    api/users   params=&{parameters}
    log to console  ${response.status_code}
    log to console  ${response.content}
    ${actual_code}=    convert to string  ${response.status_code}
    should be equal    ${actual_code}   200
    ${json_response}=  To Json  ${response.content}
    ${email_list}=     Get Value From Json     ${json_response}     data[0].email
    ${email}=  get from list  ${email_list}   0
    log to console  ${email}
    should be equal  ${email}   michael.lawson@reqres.in
