*** Settings ***
Library  RequestsLibrary
Library     JSONLibrary
Library     Collections
Library    ../ReadContent/ReadContentJson.py

*** Variables ***
${url}  http://thetestingworldapi.com/

*** Keywords ***
 #keyword are use for re useability and are exctaly same as function in other language
Fetch Request Content
      ${json_body}=   read_requestContent
      [Return]      ${json_body}
