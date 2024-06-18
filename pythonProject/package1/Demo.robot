*** Settings ***
# Setting section is used to define the libraary which we will using for our current project
Library     RequestsLibrary
Library     JSONLibrary
Library     Collections
#collections library is used to manipulate list data type
Resource    ../Resources/Library.robot

Documentation   This robot file consists of API Automation test cases
*** Variables ***
${url}  http://thetestingworldapi.com/
${id}   1147032
${child_url}   api/studentsDetails
${reqres_url}   https://reqres.in/

*** Test Cases ***
TC_GETRequest
    [Documentation]  This test case will automate the Get Request containing Parameters
    create session  FetchData   ${url}
    ${response}=    get on session     FetchData   api/studentsDetails
    log to console  ${response.status_code}
    log to console  ${response.content}
    #${prateek}=      Set Variable   ${response.content}
    ${actual_code}=    convert to string  ${response.status_code}
    should be equal    ${actual_code}   200
    ${json_response}=  To Json  ${response.content}
    #${json_responsee}=   Set Variable       ${prateek.json()}
    #Loop-----------
    ${id_list}=     Get Value From Json     ${json_response}     $.[1].id
    #${idLists}=     convert to string  ${id_list}
    ${id}=  get from list  ${id_list}   0
    #${id}=  get from list   ${id_list}   0
    log to console  ${id}
    ${int_id}=  convert to string  ${id}
    should be equal  ${int_id}  1149248

TC_GETRequest Students_details
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

TC_PostRequest_StudentsDetails
    Create Session  PostData    ${url}
    &{body}=    Create Dictionary   first_name=Juhi     middle_name=Chauhan    last_name=Rajput    date_of_birth=4-06-1999
    &{header}=      Create Dictionary   Content-Type=application/json   #Accept=application/json
    ${response}=    POST REQUEST     PostData   api/studentsDetails  data=${body}    headers=${header}
    log to console      ${response.status_code}
    log to console      ${response.content}

TC_PutRequest_StudentsDetails
    Create Session  PostData    ${url}
    &{body}=    Create Dictionary       id=1150581    first_name=Chhavi     middle_name=Chauhan    last_name=Rajput   date_of_birth=4-06-1999
    &{header}=      Create Dictionary   Content-Type=application/json   #Accept=application/json
    ${response}=    PUT REQUEST     PostData   api/studentsDetails/1150581  data=${body}    headers=${header}
    log to console      ${response.status_code}
    log to console      ${response.content}

TC_PostRequest_reqres
    Create Session  CreateData  ${reqres_url}
    &{body}=    CREATE DICTIONARY   name=morphus   job=manager
    &{header}=    create dictionary  Content-Type=application/json   #Accept=application/json
    ${response}=    POST REQUEST  CreateData     /api/users      data=${body}    headers=${header}
    log to console      ${response.status_code}
    log to console      ${response.content}

TC_PostRequest_Register_reqres
    Create Session  Register_Successfull  ${reqres_url}
    &{body}=    CREATE DICTIONARY   email=juhi.rajput.004@gmail.com    password=pistol
    &{header}=    create dictionary  Content-Type=application/json   #Accept=application/json
    ${response}=    POST REQUEST  Register_Successfull     /api/register      data=${body}    headers=${header}
    log to console      ${response.status_code}
    log to console      ${response.content}

TC_PostRequest_RegisterUnsuccessfully_reqres
    Create Session  Register_Unsuccessfull  ${reqres_url}
    &{body}=    CREATE DICTIONARY   email=prateekc231@gmail.com      #password=juhirajput
    &{header}=    create dictionary  Content-Type=application/json   #Accept=application/json
    ${response}=    POST REQUEST  Register_Unsuccessfull     /api/register      data=${body}    headers=${header}
    log to console      ${response.status_code}
    log to console      ${response.content}

TC_PostRequest_Login_reqres
    Create Session  Login  ${reqres_url}
    &{body}=    CREATE DICTIONARY   email=eve.holt@reqres.in    password=cityslicka
    &{header}=    create dictionary  Content-Type=application/json   #Accept=application/json
    ${response}=    POST REQUEST  Login     /api/login      data=${body}    headers=${header}
    log to console      ${response.status_code}
    log to console      ${response.content}

TC_PostRequest_LoginUnsuccessfully_reqres
    Create Session  Login_Unsuccessfully  ${reqres_url}
    &{body}=    CREATE DICTIONARY   email=eve.holt@reqres.in    #password=cityslicka
    &{header}=    create dictionary  Content-Type=application/json   #Accept=application/json
    ${response}=    POST REQUEST  Login_Unsuccessfully     /api/login      data=${body}    headers=${header}
    log to console      ${response.status_code}
    log to console      ${response.content}

TC_PutRequest_reqres
    Create Session  UpdateData  ${reqres_url}
    &{body}=    CREATE DICTIONARY   id=528  name=prateek   job=manager
    &{header}=    create dictionary  Content-Type=application/json   #Accept=application/json
    ${response}=    PUT REQUEST  UpdateData     /api/users/528      data=${body}    headers=${header}
    log to console      ${response.status_code}
    log to console      ${response.content}

TC_DeleteRequest
    Create Session      DeleteData      ${url}
    ${response}=    delete request      DeleteData      ${child_url}/1147000
    log to console  ${response.status_code}
    log to console  ${response.content}

TC_RequestChainig
    [Documentation]  This test case will automate of request chaining with student details
    Create Session  requestChaining     ${url}
    &{data}=    create dictionary   first_name=Prateek     last_name=chauhan   date_of_birth=4-02-1999
    &{header}=  create dictionary  Content-Type=application/json
    ${post_response}=     post request  requestChaining   ${child_url}    data=${data}     headers=${header}
    log to console  ${post_response.status_code}
    log to console  ${post_response.content}
    ${json_response}=   To Json  ${post_response.content}
    ${id_list}=     get value from json     ${json_response}    id
    ${id}=  get from list  ${id_list}     0
    log to console  ${id}

    &{data1}=    create dictionary   id=${id}   first_name=Prateek    last_name=chauhan  date_of_birth=8-02-1999
    ${put_response}=    put request  requestChaining   ${child_url}/${id}    data=${data1}     headers=${header}
    log to console  ${put_response.status_code}
    log to console    ${put_response.content}

    ${get_response}=    get on session      requestChaining     ${child_url}/${id}
    log to console  ${get_response.content}

    ${delete_response}=     delete request      requestChaining     ${child_url}/${id}
    log to console  ${delete_response}

TC_PostRquestWithPythonCode
    [Documentation]  For handling bigger json fie we will use the python
    Create Session  PostData    ${url}
    &{body}=    Create Dictionary   first_name=Juhi     middle_name=Chauhan    last_name=Rajput    date_of_birth=4-06-1999
    &{header}=      Create Dictionary   Content-Type=application/json   #Accept=application/json
    ${response}=    POST REQUEST     PostData   api/studentsDetails  data=${body}    headers=${header}
    log to console      ${response.status_code}
    log to console      ${response.content}

TC_PostRquestWithFile
    [Documentation]  For handling bigger json fie we will use the python
    Create Session  PostData    ${url}
    ${json_contents}=    Fetch Request Content
    &{header}=      Create Dictionary   Content-Type=application/json   #Accept=application/json
    ${response}=    POST REQUEST     PostData   api/studentsDetails  data=${json_contents}    headers=${header}
    log to console      ${response.status_code}
    log to console      ${response.content}
    ${json_response}=   To Json  ${response.content}
    ${id_list}=     get value from json     ${json_response}    id
    ${id}=  get from list  ${id_list}     0
    log to console  ${id}
#     log to console    ${json_response}

