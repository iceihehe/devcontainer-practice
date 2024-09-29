*** Settings ***
Library    RequestsLibrary

*** Variables ***
${host}     http://webserver:5000

*** Keywords ***

PING

    ${response}=     GET    ${host}

    Should Be Equal   Yeah!  ${response.text}
